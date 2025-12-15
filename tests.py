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

if __name__ == '__main__':
    unittest.main()