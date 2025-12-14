output "vpc_id" {
    value = aws_vpc.main.id
}
output "security_group_id" {
    value = aws_security_group.security_group.id
}
output "subnet_1_id" {
    value = aws_subnet.subnet_1.id
}
output "subnet_2_id" {
    value = aws_subnet.subnet_2.id
}
