from decimal import Decimal
from copy import deepcopy
from typing import Dict
from dataclasses import dataclass, asdict


@dataclass
class WebPage:
    page: str
    url: str
    counter: int

    def to_dict(self) -> Dict[str, str]:
        value = deepcopy(asdict(self))
        value["counter"] = Decimal(str(value["counter"]))
        return value
