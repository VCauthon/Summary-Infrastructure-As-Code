output "table_name_related_news" {
    value = aws_dynamodb_table.aws_dynamodb_table_rn.name
}
output "table_name_web_display" {
    value = aws_dynamodb_table.web_display.name
}
