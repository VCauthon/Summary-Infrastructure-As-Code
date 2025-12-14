# Creates the virtual private cloud
resource "aws_vpc" "main" {
  cidr_block           = local.network_cidr_block
  enable_dns_hostnames = true
}

# Gives to the virtual private cloud access to the internet
resource "aws_internet_gateway" "internet_gateway" {
  vpc_id = aws_vpc.main.id
}