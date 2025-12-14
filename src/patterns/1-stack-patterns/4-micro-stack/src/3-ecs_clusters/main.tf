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
data "terraform_remote_state" "networking" {
  backend = "local"
  config = {
    path = "../2-networking/terraform.tfstate"
  }
}
