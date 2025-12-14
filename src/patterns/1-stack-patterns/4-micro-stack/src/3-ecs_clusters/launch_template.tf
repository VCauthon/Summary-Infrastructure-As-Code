resource "aws_launch_template" "ecs_lt" { # Define the configuration of each instance
  name_prefix   = "webpage-url"
  image_id      = data.aws_ssm_parameter.base_image.value
  instance_type = "t3.micro"

  vpc_security_group_ids = [data.terraform_remote_state.networking.outputs.security_group_id]

  iam_instance_profile {
    arn = aws_iam_instance_profile.ecs_instance_profile.arn
  }

  block_device_mappings {
    device_name = "/dev/xvda"
    ebs {
      volume_size = 30
      volume_type = "gp3"
    }
  }
  user_data = filebase64("${path.module}/ecs.sh")
}