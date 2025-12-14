# ECS service definition (wraps everything up)
resource "aws_ecs_service" "ecs_service" {
  name            = "web-page"
  cluster         = data.terraform_remote_state.ecs_cluster.outputs.cluster_id
  task_definition = aws_ecs_task_definition.ecs_task_definition.arn

  force_delete = true

  desired_count = 1

  network_configuration {
    subnets         = [data.terraform_remote_state.network.outputs.subnet_1_id, data.terraform_remote_state.network.outputs.subnet_2_id]
    security_groups = [data.terraform_remote_state.network.outputs.security_group_id]
  }

  # Enforces the creation of a new instance when a new image its been deployed
  force_new_deployment = true
  placement_constraints {
    type = "distinctInstance"
  }

  capacity_provider_strategy {
    capacity_provider = data.terraform_remote_state.ecs_cluster.outputs.capacity_provider_name
    weight            = 100
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.ecs_tg.arn
    container_name   = "dockergs"
    container_port   = 5000
  }

  triggers = {
    redeployment = timestamp() # For now it will only redeploy when this task its been executed
  }
}
# ECS service definition (wraps everything up)
resource "aws_ecs_service" "ecs_service_back_office" {
  name            = "web-backoffice"
  cluster         = data.terraform_remote_state.ecs_cluster.outputs.cluster_id
  task_definition = aws_ecs_task_definition.ecs_task_definition_backoffice.arn

  force_delete = true

  desired_count = 1

  network_configuration {
    subnets         = [data.terraform_remote_state.network.outputs.subnet_1_id, data.terraform_remote_state.network.outputs.subnet_2_id]
    security_groups = [data.terraform_remote_state.network.outputs.security_group_id]
  }

  # Enforces the creation of a new instance when a new image its been deployed
  force_new_deployment = true
  placement_constraints {
    type = "distinctInstance"
  }

  capacity_provider_strategy {
    capacity_provider = data.terraform_remote_state.ecs_cluster.outputs.capacity_provider_name
    weight            = 100
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.ecs_tg_backoffice.arn
    container_name   = "dockergs"
    container_port   = 5000
  }

  triggers = {
    redeployment = timestamp() # For now it will only redeploy when this task its been executed
  }

  depends_on = [
    aws_lb_listener_rule.ecs_alb_listener_rule_backoffice
  ]
}