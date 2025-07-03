import unittest
import io
import sys
from contextlib import redirect_stdout

class TestLibrariesAndModules(unittest.TestCase):

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

    def test_math_module_usage(self):
        # Execute the exercise file
        try:
            with open('10-introduction-to-libraries-and-modules/libraries_and_modules_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing libraries_and_modules_exercise.py: {e}")

        # Check if math module was imported and used
        self.assertIn('math', sys.modules, "The 'math' module was not imported.")

        # Check if principal_amount exists and is correct
        self.assertIn('principal_amount', globals(), "Variable 'principal_amount' not found.")
        self.assertEqual(globals()['principal_amount'], 2500, "Incorrect value for 'principal_amount'.")

        # Check output for square root and pi
        output = self.new_stdout.getvalue()
        self.assertIn("50.0", output, "Square root of principal_amount not printed correctly.")
        self.assertIn(str(3.14159), output, "Value of math.pi not printed correctly.") # Check for a reasonable approximation

    def test_pandas_import_simulation(self):
        # Execute the exercise file
        try:
            with open('10-introduction-to-libraries-and-modules/libraries_and_modules_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing libraries_and_modules_exercise.py: {e}")

        # This test primarily checks if the import statement itself is present in the file.
        # It does not attempt to actually import pandas, as it might not be installed.
        with open('10-introduction-to-libraries-and-modules/libraries_and_modules_exercise.py', 'r') as f:
            content = f.read()
            self.assertIn("import pandas as pd", content, "The 'import pandas as pd' statement was not found.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
