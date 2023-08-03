terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.24"
    }
  }
  required_version = ">= 0.2.1"
}

provider "aws" {
  region = "us-east-1"
}
