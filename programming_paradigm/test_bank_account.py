# test_bank_account.py

import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """Create a fresh account before each test."""
        self.account = BankAccount(100)  # Start with $100

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.account_balance, 150)

    def test_withdraw_success(self):
        result = self.account.withdraw(30)
        self.assertTrue(result)
        self.assertEqual(self.account.account_balance, 70)

    def test_withdraw_failure(self):
        result = self.account.withdraw(200)  # More than balance
        self.assertFalse(result)
        self.assertEqual(self.account.account_balance, 100)  # Balance unchanged

    def test_display_balance(self):
        self.assertEqual(self.account.display_balance(), "Current Balance: $100")

if __name__ == "__main__":
    unittest.main()
