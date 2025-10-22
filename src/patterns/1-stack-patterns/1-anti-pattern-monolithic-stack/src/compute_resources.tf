

# Define the resources that the ecs cluster will handle to throw some task
data "aws_ssm_parameter" "base_image" {
    name = "/aws/service/ecs/optimized-ami/amazon-linux-2023/recommended/image_id"
}
resource "aws_launch_template" "ecs_lt" {  # Define the configuration of each instance
    name_prefix = "webpage-url"
    image_id = aws_ssm_parameter.base_image.value
    instance_type = "t3.micro"

    key_name = "ec2ecsglog"
    vpc_security_group_ids = [aws_security_group.security_group.security_group.id]
    iam_instance_profile {
        name = "ecsInstanceRole"
    }

    block_device_mappings {
        device_name = "/dev/xvda"
        ebs {
            volume_size = 5
            volume_type = "gp3"
        }
    }
    user_data = filebase64("${path.module}/ecs.sh")
}

# Sets how will scale the solution based on the demand
resource "aws_autoscaling_group" "ecs_asg" {
    vpc_zone_identifier = [aws_subnet.subnet]
    desired_capacity = 1
    max_size = 1
    min_size = 0

    launch_template {
      id = aws_launch_template.ecs_lt.id
      version = "$Latest"
    }
}

# Sets how the request will be balanced between its instances
resource "aws_lb" "ecs_alb" {
    name = "ecs-alb"

    internal = false
    load_balancer_type = "application"

    security_groups = [aws_security_group.security_group.id]
    subnets         = [aws_subnet.subnet.id]
}
resource "aws_lb_target_group" "ecs_tg" { # LB request destination
    name = "ecs-target-group"
    port = 80
    protocol = "HTTP"

    target_type = "id"
    vpc_id = aws_vpc.main.id

    health_check {
      path = "/"
    }
}
resource "aws_lb_listener" "ecs_alb_listener" { # LB entry point
    load_balancer_arn = aws_lb.ecs_alb.arn
    port = 80
    protocol = "HTTP"

    default_action {
      type = "forward"
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

      managed_scaling {
        maximum_scaling_step_size = 5
        minimum_scaling_step_size = 0
        status = "ENABLED"
        target_capacity = 100
      }
    }
}
resource "aws_ecs_cluster_capacity_providers" "ecs_bind_cp_and_cluster" { # Binds the capacity provider with the ecs cluster
    cluster_name = aws_ecs_cluster.ecs_cluster.name
    capacity_providers = [aws_ecs_capacity_provider.ecs_capacity_provider.name]

    default_capacity_provider_strategy {
      base = 1
      weight = 100
      capacity_provider = aws_ecs_capacity_provider.ecs_capacity_provider.name
    }
}

# ECS instance definition
data "aws_caller_identity" "current" {}
resource "aws_ecs_task_definition" "ecs_task_definition" { # Define the task that will run in each instance
    family = "my-ecs-task"
    network_mode = "awsvpc"
    execution_role_arn = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:role/ecsTaskExecutionRole"

    cpu = 256
    runtime_platform {
      operating_system_family = "LINUX"
      cpu_architecture = "X86_64"
    }

    container_definitions = jsonencode([{
        name = "dockergs"
        image = "public.ecr.aws/f9n5f1l7/dgs:latest"
        cpu = 256
        memory = 512
        essential = true
        portMappings = [{
            containerPort = 80
            hostPort = 80
            protocol = "tcp"
        }]
    }])
}
