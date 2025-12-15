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
      TypePattern = "environment-patterns"
      PatternName = "MultipleEnvironmentPattern"
      GitProject = "SummaryInfrastructureAsCode"
    }
  }
}

data "aws_caller_identity" "current" {}

# Create a zip file about the python script
data "archive_file" "python_script" {
  type        = "zip"
  source_dir = local.local_dir_etl_workflow
  output_path = local.temp_dir
}