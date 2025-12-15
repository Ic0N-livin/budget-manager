import unittest
from budget import Expense, BudgetManager

class TestBudgetApp(unittest.TestCase):
    def test_expense_creation(self):
        exp = Expense("Kawa", 12.0)
        self.assertEqual(exp.amount, 12.0)

    def test_expense_validation(self):
        # Test: sprawdź, czy ujemna kwota powoduje błąd
        with self.assertRaises(ValueError):
            Expense("Error", -5)

    def test_manager_integration(self):
        # Test integracyjny: Menedżer + Koszty
        manager = BudgetManager(100)
        manager.add_expense("Jedzenie", 30)
        self.assertEqual(manager.balance, 70)
        self.assertEqual(len(manager.expenses), 1)

    def test_insufficient_funds(self):
        manager = BudgetManager(50)
        with self.assertRaises(ValueError):
            manager.add_expense("Zegarek", 100)

if __name__ == '__main__':
    unittest.main()