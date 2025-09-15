
import unittest, os

class SmokeTest(unittest.TestCase):
    def test_repo_has_ledger(self):
        self.assertTrue(os.path.exists("ledger.txt"))

if __name__ == "__main__":
    unittest.main()
