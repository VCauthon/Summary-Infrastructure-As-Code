terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.18.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
  default_tags {
    tags = {
      TypePattern = "stack-patterns"
      PatternName = "MonolithicStack"
    }
  }
}
