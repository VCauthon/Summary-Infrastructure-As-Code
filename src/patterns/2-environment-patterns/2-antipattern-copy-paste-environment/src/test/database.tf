data "aws_caller_identity" "current" {}


resource "aws_dynamodb_table" "aws_dynamodb_table_rn" {
    name = "RelatedNews${title(local.environment)}"

    billing_mode = "PROVISIONED"
    read_capacity = 1
    write_capacity = 1

    hash_key = local.hash_key_news_loader
    attribute {
      name = local.hash_key_news_loader
      type = "S"
    }
}
