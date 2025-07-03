import unittest
import io
import sys
from contextlib import redirect_stdout

class TestVariablesAndTypes(unittest.TestCase):

    def setUp(self):
        # Capture stdout
        self.held_stdout = sys.stdout
        self.new_stdout = io.StringIO()
        sys.stdout = self.new_stdout

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.held_stdout

    def test_variables_exist_and_types_are_correct(self):
        # Execute the exercise file
        try:
            with open('2-variables-and-data-types/variables_and_types_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing variables_and_types_exercise.py: {e}")

        # Check if variables exist and have correct types
        self.assertIn('client_name', globals(), "Variable 'client_name' not found.")
        self.assertIsInstance(globals()['client_name'], str, "Variable 'client_name' is not a string.")

        self.assertIn('portfolio_size', globals(), "Variable 'portfolio_size' not found.")
        self.assertIsInstance(globals()['portfolio_size'], int, "Variable 'portfolio_size' is not an integer.")

        self.assertIn('current_yield', globals(), "Variable 'current_yield' not found.")
        self.assertIsInstance(globals()['current_yield'], float, "Variable 'current_yield' is not a float.")

        # Check if print statements are present (basic check)
        output = self.new_stdout.getvalue()
        self.assertIn("client_name", output, "Output for client_name not found.")
        self.assertIn("portfolio_size", output, "Output for portfolio_size not found.")
        self.assertIn("current_yield", output, "Output for current_yield not found.")
        self.assertIn("Type of", output, "Type information not printed for variables.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
