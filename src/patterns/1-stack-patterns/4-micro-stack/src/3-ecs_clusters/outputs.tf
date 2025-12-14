output "cluster_id" {
    value = aws_ecs_cluster.ecs_cluster.id
}
output "capacity_provider_name" {
    value = aws_ecs_capacity_provider.ecs_capacity_provider.name
}
output "load_balancer_arn" {
    value = aws_lb.ecs_alb.arn
}