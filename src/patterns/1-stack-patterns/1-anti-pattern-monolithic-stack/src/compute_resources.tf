

# Defines the launch template that the containers will be using
data "aws_ssm_parameter" "base_image" {
    name = "/aws/service/ecs/optimized-ami/amazon-linux-2023/recommended/image_id"
}
resource "aws_launch_template" "ecs_lt" {
    name_prefix = "webpage-url"
    image_id = aws_ssm_parameter.base_image.value
    instance_type = "t3.micro"

    key_name = "ec2ecsglog"
    vpc_security_group_ids = [aws_security_group.security_group.security_group.id]
    iam_instance_profile {
        name = "ecsInstanceRole"
    }

    block_device_mappings {
        device_name = "/dev/xvda"
        ebs {
            volume_size = 5
            volume_type = "gp3"
        }
    }
    user_data = filebase64("${path.module}/ecs.sh")
}

# Sets how will scale the solution based on the demand
resource "aws_autoscaling_group" "ecs_asg" {
    vpc_zone_identifier = [aws_subnet.subnet]
    desired_capacity = 1
    max_size = 1
    min_size = 0

    launch_template {
      id = aws_launch_template.ecs_lt.id
      version = "$Latest"
    }
}
