from typing import List

from adapter.dynamodb import DynamoDB
from service.models.page_items import WebPage


TABLE_NAME = "WebDisplay"


class Database:
    def __init__(self):
        self._connection = DynamoDB(TABLE_NAME)

    def get_pages(self) -> List[WebPage]:
        return [WebPage(
                page=val.get("page"),
                url=val.get("url"),
                counter=val.get("counter"),
            ) for val in self._connection.get_all_items()]

    def update_value(self, record: WebPage) -> None:
        self._connection.set_value(record.to_dict())
