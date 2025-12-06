from typing import Dict, List, Any

import boto3
from mypy_boto3_dynamodb import ServiceResource


class DynamoDB:
    def __init__(self, table: str) -> None:
        self._resource: ServiceResource = boto3.resource("dynamodb")
        self._table = self._resource.Table(table)

    def get_all_items(self) -> List[Dict[str, Any]]:
        """Get all items from the table"""
        items = self._table.scan()
        return items["Items"] if "Items" in items else []

    def set_items(self, values: List[Dict[str, Any]]) -> None:
        """Create or update an item."""
        with self._table.batch_writer() as batch:
            for value in values:
                batch.put_item(Item=value)

    def delete_item(self, key: Dict[str, Any]) -> None:
        """Delete an item by key."""
        self._table.delete_item(Key=key)
