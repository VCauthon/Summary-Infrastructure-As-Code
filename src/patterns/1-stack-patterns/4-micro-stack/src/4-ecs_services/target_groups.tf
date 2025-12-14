resource "aws_lb_target_group" "ecs_tg" { # LB request destination
  name     = "ecs-target-group"
  port     = 80
  protocol = "HTTP"

  target_type = "ip"
  vpc_id      = data.terraform_remote_state.network.outputs.vpc_id

  health_check {
    path = "/"
  }
}
resource "aws_lb_target_group" "ecs_tg_backoffice" { # LB request destination
  name     = "ecs-target-group-backoffice"
  port     = 80
  protocol = "HTTP"

  target_type = "ip"
  vpc_id      = data.terraform_remote_state.network.outputs.vpc_id

  health_check {
    path = "/"
  }
}