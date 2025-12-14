# Create a zip file about the python script
data "archive_file" "python_script" {
  type        = "zip"
  source_dir = local.local_dir_etl_workflow
  output_path = local.temp_dir
}

# Lambda definition
resource "aws_lambda_function" "etl_news_extractor" {
    function_name   = "etl_workflow"
    role            = aws_iam_role.role_execute_lambda.arn
    package_type    = "Zip"
    filename        = data.archive_file.python_script.output_path
    handler       = "app.lambda_handler"
    runtime       = "python3.12"

    memory_size = 512
    timeout     = 30

    architectures = ["arm64"]
}