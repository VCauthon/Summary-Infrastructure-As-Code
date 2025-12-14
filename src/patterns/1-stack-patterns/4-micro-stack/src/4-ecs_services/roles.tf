# EXECUTION POINT OF VIEW
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect    = "Allow",
      Principal = { Service = "ecs-tasks.amazonaws.com" }, # IMPORTANT
      Action    = "sts:AssumeRole"
    }]
  })
}
# Allow the use of CloudFormation and Downloading of images
resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}
# RUNNING POINT OF VIEW
resource "aws_iam_role" "ecs_task_role" {
  name = "my-ecs-task-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect    = "Allow",
      Principal = { Service = "ecs-tasks.amazonaws.com" },
      Action    = "sts:AssumeRole"
    }]
  })
}
# Allow the use of DynamoDB
resource "aws_iam_policy" "ecs_task_dynamodb_policy" {
  name = "ecs-task-dynamodb-policy"

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
          "dynamodb:DescribeTable",
          "dynamodb:Scan",
        ],
        Resource = [
          "arn:aws:dynamodb:${local.region}:${data.aws_caller_identity.current.account_id}:table/${data.terraform_remote_state.database.outputs.table_name_web_display}"
        ]
      }
    ]
  })
}
resource "aws_iam_role_policy_attachment" "ecs_task_role_dynamodb_attach" {
  role       = aws_iam_role.ecs_task_role.name
  policy_arn = aws_iam_policy.ecs_task_dynamodb_policy.arn
}