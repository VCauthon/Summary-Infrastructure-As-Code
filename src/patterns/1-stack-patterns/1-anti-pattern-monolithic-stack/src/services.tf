# ECS instance definition
data "aws_caller_identity" "current" {}
resource "aws_ecs_task_definition" "ecs_task_definition" { # Define the task that will run in each instance
    family = "my-ecs-task"
    network_mode = "awsvpc"
    execution_role_arn = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:role/ecsTaskExecutionRole"

    cpu = 256
    runtime_platform {
      operating_system_family = "LINUX"
      cpu_architecture = "X86_64"
    }

    container_definitions = jsonencode([{
        name = "dockergs"
        image = "docker.io/joeyratt/webpage:latest"
        cpu = 256
        memory = 512
        essential = true
        portMappings = [{
            containerPort = 80
            hostPort = 80
            protocol = "tcp"
        }]
    }])
}


# ECS service definition (wraps everything up)
resource "aws_ecs_service" "ecs_service" {
    name    = "web-page"
    cluster = aws_ecs_cluster.ecs_cluster.id
    task_definition = aws_ecs_task_definition.ecs_task_definition.arn

    desired_count = 1

    network_configuration {
      subnets = [aws_subnet.subnet_1.id, aws_subnet.subnet_2.id]
      security_groups = [aws_security_group.security_group.id]
    }

    # Enforces the creation of a new instance when a new image its been deployed
    force_new_deployment = true
    placement_constraints {
      type = "distinctInstance"
    }

    capacity_provider_strategy {
      capacity_provider = aws_ecs_capacity_provider.ecs_capacity_provider.name
      weight = 100
    }

    load_balancer {
      target_group_arn = aws_lb_target_group.ecs_tg.arn
      container_name = "dockergs"
      container_port = 80
    }

    triggers = {
      redeployment = timestamp()  # For now it will only redeploy when this task its been executed
    }
}
