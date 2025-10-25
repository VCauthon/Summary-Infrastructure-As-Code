
# Creates the virtual private cloud
resource "aws_vpc" "main" {
    cidr_block = local.network_cidr_block
    enable_dns_hostnames = true
}

# Creates a subnet inside the virtual private cloud
resource "aws_subnet" "subnet_1" {
    vpc_id = aws_vpc.main.id
    cidr_block = cidrsubnet(aws_vpc.main.cidr_block, 8, 1)
    map_public_ip_on_launch = true
    availability_zone = "eu-west-1a"
}

# Creates a subnet inside the virtual private cloud
resource "aws_subnet" "subnet_2" {
    vpc_id = aws_vpc.main.id
    cidr_block = cidrsubnet(aws_vpc.main.cidr_block, 8, 2)
    map_public_ip_on_launch = true
    availability_zone = "eu-west-1b"
}

# Gives to the virtual private cloud access to the internet
resource "aws_internet_gateway" "internet_gateway" {
    vpc_id = aws_vpc.main.id
}

# Routes unknown IP to the internet
resource "aws_route_table" "route_table" {
    vpc_id = aws_vpc.main.id
    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.internet_gateway.id
    }
}

# Binds the route table to the subnet
resource "aws_route_table_association" "subnet_1_route" {
    subnet_id = aws_subnet.subnet_1.id
    route_table_id = aws_route_table.route_table.id
}
resource "aws_route_table_association" "subnet_2_route" {
    subnet_id = aws_subnet.subnet_2.id
    route_table_id = aws_route_table.route_table.id
}

# Security group from for the ECS implemented
# THIS SECURITY GROUP ISN'T SECURE BECAUSE IT ALLOWS ANY REQUEST (PORT/PROTOCOL) TO THE RESOURCES WHICH ARE BOUND
resource "aws_security_group" "security_group" {
    name = "ecs-security-group"
    vpc_id = aws_vpc.main.id

    ingress {
        from_port = 0
        to_port = 0
        protocol = -1
        self = "false"
        cidr_blocks = ["0.0.0.0/0"]
        description = "Any"
    }

    egress {
        from_port = 0
        to_port = 0
        protocol = -1
        cidr_blocks = ["0.0.0.0/0"]
    }
}

