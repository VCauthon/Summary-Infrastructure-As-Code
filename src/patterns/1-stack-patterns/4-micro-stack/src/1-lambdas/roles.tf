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
  name = "lambda-task-dynamodb-policy"

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
          "arn:aws:dynamodb:${local.region}:${data.aws_caller_identity.current.account_id}:table/${data.terraform_remote_state.database.outputs.table_name_related_news}"
        ]
      }
    ]
  })
}
# Create the role that will be applied to the lambda
resource "aws_iam_role" "role_execute_lambda" {
    name               = "lambda_execution_role"
    assume_role_policy = data.aws_iam_policy_document.assume_role.json
}
# Attach policies into the role
resource "aws_iam_role_policy_attachment" "lambda_dynamodb_attach" {
    role = aws_iam_role.role_execute_lambda.name
    policy_arn = aws_iam_policy.lambda_task_dynamodb_policy.arn
}
