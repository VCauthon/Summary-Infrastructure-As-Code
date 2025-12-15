resource "aws_dynamodb_table" "aws_dynamodb_table_rn_pro" {
    name = "RelatedNewsPro"

    billing_mode = "PROVISIONED"
    read_capacity = 1
    write_capacity = 1

    hash_key = local.hash_key_news_loader
    attribute {
      name = local.hash_key_news_loader
      type = "S"
    }
}
# Allows to the role to assume one as a lambda executer
data "aws_iam_policy_document" "assume_role_pro" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}
# Allow the use of DynamoDB
resource "aws_iam_policy" "lambda_task_dynamodb_policy_pro" {
  name = "lambda-task-dynamodb-policy-pro"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "dynamodb:GetItem",
          "dynamodb:BatchGetItem",
          "dynamodb:Query",
          "dynamodb:PutItem",
          "dynamodb:UpdateItem",
          "dynamodb:DeleteItem",
          "dynamodb:BatchWriteItem",
          "dynamodb:BatchWriteItem",
          "dynamodb:DescribeTable",
          "dynamodb:Scan",
        ],
        Resource = [
          "arn:aws:dynamodb:${local.region}:${data.aws_caller_identity.current.account_id}:table/${aws_dynamodb_table.aws_dynamodb_table_rn_pro.name}"
        ]
      }
    ]
  })
}

# Create the role that will be applied to the lambda
resource "aws_iam_role" "role_execute_lambda_pro" {
    name               = "lambda_execution_role_pro"
    assume_role_policy = data.aws_iam_policy_document.assume_role_pro.json
}

# Attach policies into the role
resource "aws_iam_role_policy_attachment" "lambda_dynamodb_attach_pro" {
    role = aws_iam_role.role_execute_lambda_pro.name
    policy_arn = aws_iam_policy.lambda_task_dynamodb_policy_pro.arn
}

# Lambda definition
resource "aws_lambda_function" "etl_news_extractor_pro" {
    function_name   = "etl_workflow_pro"
    role            = aws_iam_role.role_execute_lambda_pro.arn
    package_type    = "Zip"
    filename        = data.archive_file.python_script.output_path
    handler       = "app.lambda_handler"
    runtime       = "python3.12"

    memory_size = 512
    timeout     = 30

    architectures = ["arm64"]
}

# Schedule the Lambda every day at 23:59
resource "aws_cloudwatch_event_rule" "daily_etl_schedule_pro" {
  name                = "etl-workflow-daily-schedule-pro"
  description         = "Runs the ETL workflow Lambda every day at 23:59"
  schedule_expression = "cron(59 23 * * ? *)"
}

resource "aws_cloudwatch_event_target" "daily_etl_target_pro" {
  rule      = aws_cloudwatch_event_rule.daily_etl_schedule_pro.name
  target_id = "etl-workflow-lambda"
  arn       = aws_lambda_function.etl_news_extractor_pro.arn
}

resource "aws_lambda_permission" "allow_eventbridge_to_invoke_pro" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.etl_news_extractor_pro.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.daily_etl_schedule_pro.arn
}
