# Schedule the Lambda every day at 23:59
resource "aws_cloudwatch_event_rule" "daily_etl_schedule" {
  name                = "etl-workflow-daily-schedule"
  description         = "Runs the ETL workflow Lambda every day at 23:59"
  schedule_expression = "cron(59 23 * * ? *)"
}

resource "aws_cloudwatch_event_target" "daily_etl_target" {
  rule      = aws_cloudwatch_event_rule.daily_etl_schedule.name
  target_id = "etl-workflow-lambda"
  arn       = aws_lambda_function.etl_news_extractor.arn
}

resource "aws_lambda_permission" "allow_eventbridge_to_invoke" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.etl_news_extractor.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.daily_etl_schedule.arn
}
