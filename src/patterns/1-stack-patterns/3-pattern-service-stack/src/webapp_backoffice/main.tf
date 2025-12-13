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
      PatternName = "ServiceStack"
      GitProject = "SummaryInfrastructureAsCode"
    }
  }
}

data "terraform_remote_state" "origin" {
  backend = "local"
  config = {
    path = "../webapp_registry/terraform.tfstate"
  }
}
