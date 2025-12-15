from dataclasses import dataclass
from typing import List
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
        
class BudgetManager:
    def __init__(self, balance: float = 0.0):
        self.balance = balance
        self.expenses: List[Expense] = []

    def add_expense(self, title: str, amount: float) -> None:
        expense = Expense(title, amount)
        if amount > self.balance:
            raise ValueError("Niewystarczające środki")
        self.expenses.append(expense)
        self.balance -= amount