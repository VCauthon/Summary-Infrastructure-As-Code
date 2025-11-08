# Define the resources that the ecs cluster will handle to throw some task
data "aws_ssm_parameter" "base_image" {
  name = "/aws/service/ecs/optimized-ami/amazon-linux-2023/recommended/image_id"
}
resource "aws_iam_role" "ecs_instance_role" { # Defines a role to allows EC2 resource to perform as ECS instances
  name = "ecsInstanceRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect    = "Allow",
      Principal = { Service = "ec2.amazonaws.com" },
      Action    = "sts:AssumeRole"
    }]
  })
}
resource "aws_iam_role_policy_attachment" "ecs_ec2_policy" { # The EC2 instance wil be able to function as an ECS container instance
  role       = aws_iam_role.ecs_instance_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
}
resource "aws_iam_role_policy_attachment" "ssm_core" { # Allows access to the instance 
  role       = aws_iam_role.ecs_instance_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}
resource "aws_iam_instance_profile" "ecs_instance_profile" { # Profile that EC2 will use
  name = "ecsInstanceProfile"
  role = aws_iam_role.ecs_instance_role.name
}
resource "aws_launch_template" "ecs_lt" { # Define the configuration of each instance
  name_prefix   = "webpage-url"
  image_id      = data.aws_ssm_parameter.base_image.value
  instance_type = "t3.micro"

  vpc_security_group_ids = [aws_security_group.security_group.id]

  iam_instance_profile {
    arn = aws_iam_instance_profile.ecs_instance_profile.arn
  }

  block_device_mappings {
    device_name = "/dev/xvda"
    ebs {
      volume_size = 30
      volume_type = "gp3"
    }
  }
  user_data = filebase64("${path.module}/ecs.sh")
}

# Sets how will scale the solution based on the demand
resource "aws_autoscaling_group" "ecs_asg" {
  name                = "asg-cluster-instances"
  vpc_zone_identifier = [aws_subnet.subnet_1.id, aws_subnet.subnet_2.id]
  desired_capacity    = 2
  max_size            = 3
  min_size            = 1

  force_delete = true

  launch_template {
    id      = aws_launch_template.ecs_lt.id
    version = "$Latest"
  }
}

# Sets how the request will be balanced between its instances
resource "aws_lb" "ecs_alb" {
  name = "ecs-alb"

  internal           = false
  load_balancer_type = "application"

  security_groups = [aws_security_group.security_group.id]
  subnets         = [aws_subnet.subnet_1.id, aws_subnet.subnet_2.id]
}
resource "aws_lb_target_group" "ecs_tg" { # LB request destination
  name     = "ecs-target-group"
  port     = 80
  protocol = "HTTP"

  target_type = "ip"
  vpc_id      = aws_vpc.main.id

  health_check {
    path = "/"
  }
}
resource "aws_lb_listener" "ecs_alb_listener" { # LB entry point
  load_balancer_arn = aws_lb.ecs_alb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.ecs_tg.arn
  }
}

# Sets the cluster where the instances with the service will run
resource "aws_ecs_cluster" "ecs_cluster" {
  name = "my-ecs-cluster"
}
resource "aws_ecs_capacity_provider" "ecs_capacity_provider" { # Sets how the demand will be handled by ECS
  name = "service"

  auto_scaling_group_provider {
    auto_scaling_group_arn = aws_autoscaling_group.ecs_asg.arn
    managed_termination_protection = "DISABLED"
    managed_draining = "DISABLED"

    managed_scaling {
      maximum_scaling_step_size = 5
      minimum_scaling_step_size = 1
      status                    = "ENABLED"
      target_capacity           = 100
    }
  }
}
resource "aws_ecs_cluster_capacity_providers" "ecs_bind_cp_and_cluster" { # Binds the capacity provider with the ecs cluster
  cluster_name       = aws_ecs_cluster.ecs_cluster.name
  capacity_providers = [aws_ecs_capacity_provider.ecs_capacity_provider.name]

  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = aws_ecs_capacity_provider.ecs_capacity_provider.name
  }
}