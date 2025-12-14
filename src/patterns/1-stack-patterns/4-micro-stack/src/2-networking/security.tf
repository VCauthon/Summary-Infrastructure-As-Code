# Allow request to dynamodb
resource "aws_vpc_endpoint" "dynamodb" {
  vpc_id       = aws_vpc.main.id
  service_name = "com.amazonaws.${local.region}.dynamodb"
  vpc_endpoint_type = "Gateway"

  route_table_ids = [
    aws_route_table.route_table.id, # your existing one
  ]

  tags = {
    Name = "dynamodb-endpoint"
  }
}

# Security group from for the ECS implemented
# THIS SECURITY GROUP ISN'T SECURE BECAUSE IT ALLOWS ANY REQUEST (PORT/PROTOCOL) TO THE RESOURCES WHICH ARE BOUND
resource "aws_security_group" "security_group" {
  name   = "ecs-security-group"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    self        = "false"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Any"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }
}
