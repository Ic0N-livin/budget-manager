import unittest
from budget import Expense, BudgetManager

class TestBudgetApp(unittest.TestCase):
    def test_expense_creation(self):
        exp = Expense("Kawa", 12.0)
        self.assertEqual(exp.amount, 12.0)

    def test_expense_validation(self):
        with self.assertRaises(ValueError):
            Expense("Error", -5)

    def test_manager_integration(self):
        SALDO_STARTOWE = 100
        manager = BudgetManager(SALDO_STARTOWE)
        manager.add_expense("Jedzenie", 30)
        self.assertEqual(manager.balance, 70)
        self.assertEqual(len(manager.expenses), 1)

    def test_insufficient_funds(self):
        SALDO_STARTOWE = 50
        manager = BudgetManager(SALDO_STARTOWE)
        with self.assertRaises(ValueError):
            manager.add_expense("Zegarek", 100)

    def test_multiple_expanses(self):
        SALDO_STARTOWE = 150
        manager = BudgetManager(SALDO_STARTOWE)
        manager.add_expense("Jedzenie", 30)
        manager.add_expense("Prezenty", 70)
        self.assertEqual(len(manager.expenses), 2)

    def test_free_expanse(self):
        with self.assertRaises(ValueError):
            Expense("Darmowa rzecz", 0)


if __name__ == '__main__':
    unittest.main()