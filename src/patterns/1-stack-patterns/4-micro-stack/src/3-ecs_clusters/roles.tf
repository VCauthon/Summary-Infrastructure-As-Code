# Define the resources that the ecs cluster will handle to throw some task
data "aws_ssm_parameter" "base_image" {
  name = "/aws/service/ecs/optimized-ami/amazon-linux-2023/recommended/image_id"
}
resource "aws_iam_role" "ecs_instance_role" { # Defines a role to allows EC2 resource to perform as ECS instances
  name = "ecsInstanceRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect    = "Allow",
      Principal = { Service = "ec2.amazonaws.com" },
      Action    = "sts:AssumeRole"
    }]
  })
}
resource "aws_iam_role_policy_attachment" "ecs_ec2_policy" { # The EC2 instance wil be able to function as an ECS container instance
  role       = aws_iam_role.ecs_instance_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
}
resource "aws_iam_role_policy_attachment" "ssm_core" { # Allows access to the instance 
  role       = aws_iam_role.ecs_instance_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}
resource "aws_iam_instance_profile" "ecs_instance_profile" { # Profile that EC2 will use
  name = "ecsInstanceProfile"
  role = aws_iam_role.ecs_instance_role.name
}