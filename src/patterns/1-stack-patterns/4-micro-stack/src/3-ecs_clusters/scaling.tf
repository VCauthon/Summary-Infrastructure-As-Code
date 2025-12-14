# Sets how will scale the solution based on the demand
resource "aws_autoscaling_group" "ecs_asg" {
  name                = "asg-cluster-instances"
  vpc_zone_identifier = [data.terraform_remote_state.networking.outputs.subnet_1_id, data.terraform_remote_state.networking.outputs.subnet_2_id]
  desired_capacity    = 2
  max_size            = 3
  min_size            = 1

  force_delete = true

  tag {
    key                 = "AmazonECSManaged"
    value               = ""
    propagate_at_launch = true
  }

  launch_template {
    id      = aws_launch_template.ecs_lt.id
    version = "$Latest"
  }

  lifecycle {
    ignore_changes = [ desired_capacity ]
  }
}

# Sets how the request will be balanced between its instances
resource "aws_lb" "ecs_alb" {
  name = "ecs-alb"

  internal           = false
  load_balancer_type = "application"

  security_groups = [data.terraform_remote_state.networking.outputs.security_group_id]
  subnets         = [data.terraform_remote_state.networking.outputs.subnet_1_id, data.terraform_remote_state.networking.outputs.subnet_2_id]
}