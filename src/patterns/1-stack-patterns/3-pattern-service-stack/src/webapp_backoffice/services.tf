resource "aws_cloudwatch_log_group" "ecs_web_backoffice_logs" {
  name              = "/ecs/web-page-back-office"
  retention_in_days = 7
}
###### WEBPAGE BACKOFFICE
resource "aws_ecs_task_definition" "ecs_task_definition_backoffice" { # Define the task that will run in each instance
  family                   = "my-ecs-task-back-office"
  requires_compatibilities = ["EC2"]
  network_mode             = "awsvpc"

  execution_role_arn = data.terraform_remote_state.origin.outputs.ecs_execution_role
  task_role_arn = data.terraform_remote_state.origin.outputs.ecs_task_role
  cpu = 256

  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "X86_64"
  }

  container_definitions = jsonencode([{
    name      = "dockergs"
    image     = "docker.io/joeyratt/webpage-aws-backoffice:latest"
    cpu       = 256
    memory    = 512
    environment = [
      {
        name = "AWS_DEFAULT_REGION",
        value = "eu-west-1"
      }
    ]
    essential = true
    portMappings = [{
      containerPort = 5000
      hostPort      = 5000
      protocol      = "tcp"
    }]
    logConfiguration = {
      logDriver = "awslogs"
      options = {
        awslogs-region = local.region
        awslogs-group         = aws_cloudwatch_log_group.ecs_web_backoffice_logs.name
        awslogs-stream-prefix = "ecs"
        awslogs-create-group = "true"
      }
    }
  }])
}


# ECS service definition (wraps everything up)
resource "aws_ecs_service" "ecs_service_back_office" {
  name            = "web-backoffice"
  cluster         = data.terraform_remote_state.origin.outputs.cluster_id
  task_definition = aws_ecs_task_definition.ecs_task_definition_backoffice.arn

  force_delete = true

  desired_count = 1

  network_configuration {
    subnets         = [data.terraform_remote_state.origin.outputs.vpc_subnet_1_id, data.terraform_remote_state.origin.outputs.vpc_subnet_2_id]
    security_groups = [data.terraform_remote_state.origin.outputs.security_group_id]
  }

  # Enforces the creation of a new instance when a new image its been deployed
  force_new_deployment = true
  placement_constraints {
    type = "distinctInstance"
  }

  capacity_provider_strategy {
    capacity_provider = data.terraform_remote_state.origin.outputs.ecs_capacity_provider_name
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