from typing import Dict, List


import boto3
from mypy_boto3_dynamodb import ServiceResource



class DynamoDB:
    
    def __init__(self, table: str) -> None:
        self._resource: ServiceResource = boto3.resource("dynamodb")
        self._table = self._resource.Table(table) 

    def get_all_items(self) -> List[Dict[str, str]]:
        """Get all items from the table"""
        items = self._table.scan()
        return items["Items"] if "Items" in items else []

    def set_value(self, value: Dict[str, str]) -> None:
        self._table.put_item(Item=value)
