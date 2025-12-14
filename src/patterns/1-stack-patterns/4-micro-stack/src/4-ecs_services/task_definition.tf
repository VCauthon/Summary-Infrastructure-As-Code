resource "aws_ecs_task_definition" "ecs_task_definition" { # Define the task that will run in each instance
  family                   = "my-ecs-task-front-end"
  requires_compatibilities = ["EC2"]
  network_mode             = "awsvpc"

  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn
  task_role_arn = aws_iam_role.ecs_task_role.arn
  cpu = 256

  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "X86_64"
  }

  container_definitions = jsonencode([{
    name      = "dockergs"
    image     = "docker.io/joeyratt/webapp-aws:latest"
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
        awslogs-group         = aws_cloudwatch_log_group.ecs_web_logs.name
        awslogs-stream-prefix = "ecs"
        awslogs-create-group = "true"
      }
    }
  }])
}

###### WEBPAGE BACKOFFICE
resource "aws_ecs_task_definition" "ecs_task_definition_backoffice" { # Define the task that will run in each instance
  family                   = "my-ecs-task-back-office"
  requires_compatibilities = ["EC2"]
  network_mode             = "awsvpc"

  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn
  task_role_arn = aws_iam_role.ecs_task_role.arn
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
