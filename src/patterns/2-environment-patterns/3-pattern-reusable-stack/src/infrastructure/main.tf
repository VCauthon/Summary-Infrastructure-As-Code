

data "aws_caller_identity" "current" {}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.18.0"
    }
  }
}

provider "aws" {
  region = local.region
  default_tags {
    tags = {
      TypePattern = "stack-patterns"
      PatternName = "ApplicationGroupStack"
      GitProject = "SummaryInfrastructureAsCode"
    }
  }
}

resource "aws_dynamodb_table" "aws_dynamodb_table_rn" {
    name = "RelatedNews${title(var.environment)}"

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
data "aws_iam_policy_document" "assume_role" {
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
resource "aws_iam_policy" "lambda_task_dynamodb_policy" {
  name = "lambda-task-dynamodb-policy-${var.environment}"

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
          "arn:aws:dynamodb:${local.region}:${data.aws_caller_identity.current.account_id}:table/${aws_dynamodb_table.aws_dynamodb_table_rn.name}"
        ]
      }
    ]
  })
}

# Create the role that will be applied to the lambda
resource "aws_iam_role" "role_execute_lambda" {
    name               = "lambda_execution_role_${var.environment}"
    assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

# Attach policies into the role
resource "aws_iam_role_policy_attachment" "lambda_dynamodb_attach" {
    role = aws_iam_role.role_execute_lambda.name
    policy_arn = aws_iam_policy.lambda_task_dynamodb_policy.arn
}


# Create a zip file about the python script
data "archive_file" "python_script" {
  type        = "zip"
  source_dir = local.local_dir_etl_workflow
  output_path = local.temp_dir
}

# Lambda definition
resource "aws_lambda_function" "etl_news_extractor" {
    function_name   = "etl_workflow_${var.environment}"
    role            = aws_iam_role.role_execute_lambda.arn
    package_type    = "Zip"
    filename        = data.archive_file.python_script.output_path
    handler       = "app.lambda_handler"
    runtime       = "python3.12"

    memory_size = 512
    timeout     = 30

    architectures = ["arm64"]
}

# Schedule the Lambda every day at 23:59
resource "aws_cloudwatch_event_rule" "daily_etl_schedule" {
  name                = "etl-workflow-daily-schedule-${var.environment}"
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
