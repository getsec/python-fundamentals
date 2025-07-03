import unittest
import io
import sys
from contextlib import redirect_stdout

class TestFunctions(unittest.TestCase):

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

    def test_greet_treasury_analyst(self):
        # Execute the exercise file
        try:
            with open('8-functions/functions_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing functions_exercise.py: {e}")

        # Check if the function exists
        self.assertIn('greet_treasury_analyst', globals(), "Function 'greet_treasury_analyst' not found.")
        self.assertTrue(callable(globals()['greet_treasury_analyst']), "'greet_treasury_analyst' is not a function.")

        # Call the function and check its output
        globals()['greet_treasury_analyst']()
        output = self.new_stdout.getvalue().strip()
        self.assertEqual(output, "Hello, Treasury Analyst! Welcome to your Python toolkit.", "Incorrect output from greet_treasury_analyst.")

    def test_calculate_bond_future_value(self):
        # Execute the exercise file
        try:
            with open('8-functions/functions_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing functions_exercise.py: {e}")

        # Check if the function exists
        self.assertIn('calculate_bond_future_value', globals(), "Function 'calculate_bond_future_value' not found.")
        self.assertTrue(callable(globals()['calculate_bond_future_value']), "'calculate_bond_future_value' is not a function.")

        # Test the function with sample values
        pv = 5000
        rate = 0.04
        years = 5
        expected_fv = pv * (1 + rate) ** years
        actual_fv = globals()['calculate_bond_future_value'](pv, rate, years)
        self.assertAlmostEqual(actual_fv, expected_fv, places=2, msg="Incorrect future value calculation.")

        # Check if print statement is present (basic check)
        output = self.new_stdout.getvalue()
        self.assertIn(f"{expected_fv:.2f}", output, "Future value not printed correctly.")

    def test_create_simple_trade_record(self):
        # Execute the exercise file
        try:
            with open('8-functions/functions_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing functions_exercise.py: {e}")

        # Check if the function exists
        self.assertIn('create_simple_trade_record', globals(), "Function 'create_simple_trade_record' not found.")
        self.assertTrue(callable(globals()['create_simple_trade_record']), "'create_simple_trade_record' is not a function.")

        # Test the function with sample values
        trade_id = "TRD001"
        ticker = "GOOGL"
        quantity = 10
        price = 1500.75
        expected_record = {"id": trade_id, "stock_ticker": ticker, "amount": quantity, "execution_price": price}
        actual_record = globals()['create_simple_trade_record'](trade_id, ticker, quantity, price)
        self.assertEqual(actual_record, expected_record, "Incorrect trade record dictionary.")

        # Check if print statement is present (basic check)
        output = self.new_stdout.getvalue()
        self.assertIn(str(expected_record), output, "Trade record dictionary not printed correctly.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
