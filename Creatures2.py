from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Creatures(ABC):
    name: str
    kind: str
    hp: int
    