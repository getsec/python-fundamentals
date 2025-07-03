import unittest
import io
import sys
from contextlib import redirect_stdout

class TestListsAndTuples(unittest.TestCase):

    def setUp(self):
        self.held_stdout = sys.stdout
        self.new_stdout = io.StringIO()
        sys.stdout = self.new_stdout
        self.original_globals = dict(globals())

    def tearDown(self):
        sys.stdout = self.held_stdout
        for key in list(globals().keys()):
            if key not in self.original_globals:
                del globals()[key]

    def test_list_operations(self):
        # Execute the exercise file
        try:
            with open('4-collections-lists-and-tuples/lists_and_tuples_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing lists_and_tuples_exercise.py: {e}")

        # Check if portfolio_holdings exists and is correct
        self.assertIn('portfolio_holdings', globals(), "Variable 'portfolio_holdings' not found.")
        expected_list = ["AAPL", "TSLA", "AMZN", "NVDA"]
        self.assertEqual(globals()['portfolio_holdings'], expected_list, "List operations resulted in an incorrect list.")

        # Check if print statements are present (basic check)
        output = self.new_stdout.getvalue()
        self.assertIn("AAPL", output, "First item not printed.")
        self.assertIn("AMZN", output, "Last item not printed.")
        self.assertIn(str(expected_list), output, "Final list not printed correctly.")

    def test_tuple_creation_and_access(self):
        # Execute the exercise file
        try:
            with open('4-collections-lists-and-tuples/lists_and_tuples_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing lists_and_tuples_exercise.py: {e}")

        # Check if q1_2024 exists and is correct
        self.assertIn('q1_2024', globals(), "Variable 'q1_2024' not found.")
        self.assertEqual(globals()['q1_2024'], (2024, 1), "Tuple 'q1_2024' is incorrect.")

        # Check if print statements are present (basic check)
        output = self.new_stdout.getvalue()
        self.assertIn(str((2024, 1)), output, "Tuple not printed correctly.")
        self.assertIn("2024", output, "Year from tuple not printed.")
        self.assertIn("1", output, "Quarter from tuple not printed.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
