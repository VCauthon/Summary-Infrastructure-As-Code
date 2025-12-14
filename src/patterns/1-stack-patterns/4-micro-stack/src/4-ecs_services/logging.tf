resource "aws_cloudwatch_log_group" "ecs_web_logs" {
  name              = "/ecs/web-page"
  retention_in_days = 7
}
resource "aws_cloudwatch_log_group" "ecs_web_backoffice_logs" {
  name              = "/ecs/web-page-back-office"
  retention_in_days = 7
}