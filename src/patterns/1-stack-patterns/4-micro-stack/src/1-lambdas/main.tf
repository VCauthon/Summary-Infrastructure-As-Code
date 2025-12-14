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
      PatternName = "MicroStack"
      GitProject = "SummaryInfrastructureAsCode"
    }
  }
}

data "aws_caller_identity" "current" {}

data "terraform_remote_state" "database" {
  backend = "local"
  config = {
    path = "../0-databases/terraform.tfstate"
  }
}
