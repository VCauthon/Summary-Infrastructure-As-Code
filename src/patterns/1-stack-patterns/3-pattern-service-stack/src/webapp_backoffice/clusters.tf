resource "aws_lb_target_group" "ecs_tg_backoffice" { # LB request destination
  name     = "ecs-target-group-backoffice"
  port     = 80
  protocol = "HTTP"

  target_type = "ip"
  vpc_id      = data.terraform_remote_state.origin.outputs.vpc_id  

  health_check {
    path = "/"
  }
}
resource "aws_lb_listener_rule" "ecs_alb_listener_rule_backoffice" {
  listener_arn = data.terraform_remote_state.origin.outputs.ecs_lb_arn
  priority     = 10

  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.ecs_tg_backoffice.arn
  }

  condition {
    path_pattern {
      values = ["/backoffice/*"]
    }
  }
}