import unittest
import io
import sys
from contextlib import redirect_stdout

class TestControlFlow(unittest.TestCase):

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

    def test_simple_if_else(self):
        # Execute the exercise file
        try:
            with open('6-control-flow-if-elif-else/control_flow_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing control_flow_exercise.py: {e}")

        output = self.new_stdout.getvalue()
        self.assertIn("Balance is healthy.", output, "Incorrect output for simple if/else.")

    def test_if_elif_else(self):
        # Execute the exercise file
        try:
            with open('6-control-flow-if-elif-else/control_flow_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing control_flow_exercise.py: {e}")

        output = self.new_stdout.getvalue()
        self.assertIn("Medium Transaction", output, "Incorrect output for if/elif/else.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
