from typing import List

from adapter.dynamodb import DynamoDB
from service.models.page_items import WebPage


TABLE_NAME = "WebDisplay"


class Database:
    def __init__(self):
        self._connection = DynamoDB(TABLE_NAME)

    def get_pages(self) -> List[WebPage]:
        items = self._connection.get_all_items()
        pages: List[WebPage] = []

        for val in items:
            pages.append(
                WebPage(
                    page=val.get("page"),
                    url=val.get("url"),
                    # DynamoDB returns Decimal; convert to int if needed
                    counter=int(val.get("counter", 0)),
                )
            )
        return pages

    def save_page(self, record: WebPage) -> None:
        """Create or update a page."""
        self._connection.set_value(record.to_dict())

    def delete_page(self, page_name: str) -> None:
        """Delete a page by its primary key."""
        self._connection.delete_item({"page": page_name})
