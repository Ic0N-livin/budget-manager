from dataclasses import dataclass
from typing import List
from datetime import datetime

@dataclass
class Expense:
    """
    Reprezentuje pojedynczy wydatek w systemie.
    
    W momencie tworzenia obiektu sprawdzana jest poprawność danych.
    Jeśli kwota jest ujemna lub tytuł pusty, zostanie zgłoszony błąd ValueError.
    """
    title: str
    amount: float
    date: datetime = datetime.now()

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Kwota musi być dodatnia")
        if not self.title:
            raise ValueError("Tytuł nie może być pusty")
        
class BudgetManager:
    """
    Główna klasa systemu, odpowiedzialna za zarządzanie globalnym saldem 
    i listą zarejestrowanych wydatków. 
    """
    def __init__(self, balance: float = 0.0):
        self.balance = balance
        self.expenses: List[Expense] = []

    def add_expense(self, title: str, amount: float) -> None:
        """
        Rejestruje nowy wydatek i odejmuje kwotę od salda.
        Wyrzuca błąd ValueError, jeśli brakuje środków.
        """
        expense = Expense(title, amount)
        if amount > self.balance:
            raise ValueError("Niewystarczające środki")
        self.expenses.append(expense)
        self.balance -= amount