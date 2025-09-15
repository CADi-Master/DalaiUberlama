
import unittest
import os
import main

class SmokeTest(unittest.TestCase):
    def test_log_writes_to_ledger(self):
        # Ensure function runs and writes to ledger.txt
        if os.path.exists('ledger.txt'):
            os.remove('ledger.txt')
        main.log('test entry')
        self.assertTrue(os.path.exists('ledger.txt'))
        with open('ledger.txt', 'r', encoding='utf-8') as f:
            data = f.read()
        self.assertIn('test entry', data)

if __name__ == "__main__":
    unittest.main()
