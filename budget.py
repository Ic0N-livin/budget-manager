from dataclasses import dataclass
from datetime import datetime

@dataclass
class Expense:
    title: str
    amount: float
    date: datetime = datetime.now()

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Kwota musi być dodatnia")
        if not self.title:
            raise ValueError("Tytuł nie może być pusty")