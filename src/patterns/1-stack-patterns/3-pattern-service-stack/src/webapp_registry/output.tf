output "vpc_id" {
    value = aws_vpc.main.id
    description = "VPC id"
}
output "ecs_lb_arn" {
    value = aws_lb_listener.ecs_alb_listener.arn
    description = "Load balancer used by the ECS cluster"
}
output "ecs_execution_role" {
    value = aws_iam_role.ecs_task_execution_role.arn
    description = "Permissions needed to start the ecs task"
}
output "ecs_task_role" {
    value = aws_iam_role.ecs_task_role.arn
    description = "Permissions needed by the task to work"
}
output "cluster_id" {
    value = aws_ecs_cluster.ecs_cluster.id
    description = "ECS Cluster id"
}
output "ecs_capacity_provider_name" {
    value = aws_ecs_capacity_provider.ecs_capacity_provider.name
    description = "ECS capacity provider name"
}
output "vpc_subnet_1_id" {
    value = aws_subnet.subnet_1.id
}
output "vpc_subnet_2_id" {
    value = aws_subnet.subnet_2.id
}
output "security_group_id" {
    value = aws_security_group.security_group.id
}
