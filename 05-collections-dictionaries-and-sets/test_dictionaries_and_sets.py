import unittest
import io
import sys
from contextlib import redirect_stdout

class TestDictionariesAndSets(unittest.TestCase):

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

    def test_dictionary_operations(self):
        # Execute the exercise file
        try:
            with open('5-collections-dictionaries-and-sets/dictionaries_and_sets_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing dictionaries_and_sets_exercise.py: {e}")

        # Check if trade_details exists and is correct
        self.assertIn('trade_details', globals(), "Variable 'trade_details' not found.")
        expected_dict = {"trade_id": "T12345", "security": "IBM", "quantity": 100, "price": 146.10, "is_buy": True, "currency": "USD"}
        self.assertEqual(globals()['trade_details'], expected_dict, "Dictionary operations resulted in an incorrect dictionary.")

        # Check if print statements are present (basic check)
        output = self.new_stdout.getvalue()
        self.assertIn("IBM", output, "Security not printed.")
        self.assertIn("146.1", output, "Updated price not printed.")
        self.assertIn(str(expected_dict), output, "Final dictionary not printed correctly.")

    def test_set_operations(self):
        # Execute the exercise file
        try:
            with open('5-collections-dictionaries-and-sets/dictionaries_and_sets_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing dictionaries_and_sets_exercise.py: {e}")

        # Check if unique_currencies exists and is correct
        self.assertIn('unique_currencies', globals(), "Variable 'unique_currencies' not found.")
        expected_set = {'USD', 'EUR', 'JPY', 'GBP'}
        self.assertEqual(globals()['unique_currencies'], expected_set, "Set operations resulted in an incorrect set.")

        # Check if print statements are present (basic check)
        output = self.new_stdout.getvalue()
        self.assertIn(str(expected_set), output, "Unique currencies set not printed correctly.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
