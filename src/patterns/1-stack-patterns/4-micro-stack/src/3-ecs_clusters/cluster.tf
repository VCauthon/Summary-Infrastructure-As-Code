# Sets the cluster where the instances with the service will run
resource "aws_ecs_cluster" "ecs_cluster" {
  name = "my-ecs-cluster"
}
resource "aws_ecs_capacity_provider" "ecs_capacity_provider" { # Sets how the demand will be handled by ECS
  name = "service"

  auto_scaling_group_provider {
    auto_scaling_group_arn = aws_autoscaling_group.ecs_asg.arn
    managed_termination_protection = "DISABLED"
    managed_draining = "DISABLED"

    managed_scaling {
      maximum_scaling_step_size = 5
      minimum_scaling_step_size = 1
      status                    = "ENABLED"
      target_capacity           = 100
    }
  }
}
resource "aws_ecs_cluster_capacity_providers" "ecs_bind_cp_and_cluster" { # Binds the capacity provider with the ecs cluster
  cluster_name       = aws_ecs_cluster.ecs_cluster.name
  capacity_providers = [aws_ecs_capacity_provider.ecs_capacity_provider.name]

  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = aws_ecs_capacity_provider.ecs_capacity_provider.name
  }
}