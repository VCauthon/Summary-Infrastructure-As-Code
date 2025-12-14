resource "aws_dynamodb_table" "web_display" {
    name = "WebDisplay"

    billing_mode = "PROVISIONED"
    read_capacity = 1
    write_capacity = 1

    hash_key = local.hash_key
    attribute {
      name = local.hash_key
      type = "S"
    }
}


resource "aws_dynamodb_table_item" "dynamo_db_record" {
    for_each = local.base_webpages

    table_name = aws_dynamodb_table.web_display.name
    hash_key = aws_dynamodb_table.web_display.hash_key

    item = <<ITEM
{
    "${local.hash_key}": {"S": "${each.value.page}"},
    "url": {"S": "${each.value.url}"},
    "counter": {"N": "0"}
}
    ITEM

    lifecycle {
      ignore_changes = [ item ]
    }
}


resource "aws_dynamodb_table" "aws_dynamodb_table_rn" {
    name = "RelatedNews"

    billing_mode = "PROVISIONED"
    read_capacity = 1
    write_capacity = 1

    hash_key = local.hash_key_news_loader
    attribute {
      name = local.hash_key_news_loader
      type = "S"
    }
}
