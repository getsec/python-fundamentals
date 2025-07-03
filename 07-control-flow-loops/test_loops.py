import unittest
import io
import sys
from contextlib import redirect_stdout

class TestLoops(unittest.TestCase):

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

    def test_for_loop_transaction_processing(self):
        # Execute the exercise file
        try:
            with open('7-control-flow-loops/loops_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing loops_exercise.py: {e}")

        # Check if total_revenue exists and is correct
        self.assertIn('total_revenue', globals(), "Variable 'total_revenue' not found.")
        self.assertAlmostEqual(globals()['total_revenue'], 725.75, places=2, msg="Incorrect value for 'total_revenue'.")

        # Check if print statements are present (basic check)
        output = self.new_stdout.getvalue()
        self.assertIn("725.75", output, "Final total revenue not printed correctly.")

    def test_while_loop_capital_growth(self):
        # Execute the exercise file
        try:
            with open('7-control-flow-loops/loops_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing loops_exercise.py: {e}")

        # Check if years and capital are correct
        self.assertIn('years', globals(), "Variable 'years' not found.")
        self.assertEqual(globals()['years'], 9, "Incorrect number of years to reach target.")
        self.assertAlmostEqual(globals()['capital'], 1551.33, places=2, msg="Incorrect final capital value.")

        # Check if print statements are present (basic check)
        output = self.new_stdout.getvalue()
        self.assertIn("Year 9: Capital is $1551.33", output, "Yearly capital not printed correctly.")
        self.assertIn("It will take 9 years to reach the target of $1500.", output, "Final years message not printed correctly.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
