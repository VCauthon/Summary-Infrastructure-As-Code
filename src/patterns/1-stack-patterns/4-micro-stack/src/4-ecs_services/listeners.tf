resource "aws_lb_listener" "ecs_alb_listener" { # LB entry point
  load_balancer_arn = data.terraform_remote_state.ecs_cluster.outputs.load_balancer_arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.ecs_tg.arn
  }
}
resource "aws_lb_listener_rule" "ecs_alb_listener_rule_backoffice" {
  listener_arn = aws_lb_listener.ecs_alb_listener.arn
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
