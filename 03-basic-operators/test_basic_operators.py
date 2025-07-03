import unittest
import io
import sys
from contextlib import redirect_stdout

class TestBasicOperators(unittest.TestCase):

    def setUp(self):
        self.held_stdout = sys.stdout
        self.new_stdout = io.StringIO()
        sys.stdout = self.new_stdout
        self.original_globals = dict(globals())

    def tearDown(self):
        sys.stdout = self.held_stdout
        # Clean up globals to prevent interference between tests
        for key in list(globals().keys()):
            if key not in self.original_globals:
                del globals()[key]

    def test_arithmetic_operations(self):
        # Execute the exercise file
        try:
            with open('3-basic-operators/basic_operators_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing basic_operators_exercise.py: {e}")

        # Check if variables exist and have correct values
        self.assertIn('total_assets', globals(), "Variable 'total_assets' not found.")
        self.assertEqual(globals()['total_assets'], 85000, "Incorrect value for 'total_assets'.")

        self.assertIn('net_profit', globals(), "Variable 'net_profit' not found.")
        self.assertEqual(globals()['net_profit'], 13000, "Incorrect value for 'net_profit'.")

        self.assertIn('quarterly_growth', globals(), "Variable 'quarterly_growth' not found.")
        self.assertEqual(globals()['quarterly_growth'], 102000.0, "Incorrect value for 'quarterly_growth'.")

        self.assertIn('average_return', globals(), "Variable 'average_return' not found.")
        self.assertEqual(globals()['average_return'], 150.0, "Incorrect value for 'average_return'.")

        self.assertIn('remainder_funds', globals(), "Variable 'remainder_funds' not found.")
        self.assertEqual(globals()['remainder_funds'], 15000, "Incorrect value for 'remainder_funds'.")

        # Check if print statements are present (basic check)
        output = self.new_stdout.getvalue()
        self.assertIn("85000", output, "Output for total_assets not found.")
        self.assertIn("13000", output, "Output for net_profit not found.")
        self.assertIn("102000.0", output, "Output for quarterly_growth not found.")
        self.assertIn("150.0", output, "Output for average_return not found.")
        self.assertIn("15000", output, "Output for remainder_funds not found.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
