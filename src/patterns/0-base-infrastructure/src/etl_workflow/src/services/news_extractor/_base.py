from typing import List, Dict
from abc import ABC, abstractmethod
from datetime import date
from dataclasses import dataclass, asdict
from copy import deepcopy


@dataclass
class News:
    source: str
    new_id: str
    url: str
    title: str
    date: date

    def to_dict(self) -> Dict[str, str]:
        result = deepcopy(self)
        result.date = result.date.isoformat()
        return asdict(result)


class NewsExtractor(ABC):
    @abstractmethod
    def extract_news(self, limit: str) -> List[News]:
        ...
