from typing import List
from abc import ABC, abstractmethod
from datetime import date
from dataclasses import dataclass


@dataclass
class News:
    source: str
    id: str
    url: str
    title: str
    date: date


class NewsExtractor(ABC):
    @abstractmethod
    def extract_news(self, limit: str) -> List[News]:
        ...
