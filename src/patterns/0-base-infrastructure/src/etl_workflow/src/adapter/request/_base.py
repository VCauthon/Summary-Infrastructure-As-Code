from abc import ABC, abstractmethod
from typing import Dict


from requests import get


class Request(ABC):

    @property
    @abstractmethod
    def source(self) -> str:
        ...

    @staticmethod
    def _get(url: str) -> Dict[str, str]:
        data = get(
            url=url
        )
        data.raise_for_status()
        return data.json()
