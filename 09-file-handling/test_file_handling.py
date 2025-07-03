import unittest
import io
import sys
import os
from contextlib import redirect_stdout

class TestFileHandling(unittest.TestCase):

    def setUp(self):
        self.held_stdout = sys.stdout
        self.new_stdout = io.StringIO()
        sys.stdout = self.new_stdout
        self.original_globals = dict(globals())
        self.file_path = '9-file-handling/treasury_report.txt'

    def tearDown(self):
        sys.stdout = self.held_stdout
        for key in list(globals().keys()):
            if key not in self.original_globals:
                del globals()[key]
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_write_and_read_file(self):
        # Execute the exercise file
        try:
            with open('9-file-handling/file_handling_exercise.py', 'r') as f:
                exec(f.read(), globals())
        except Exception as e:
            self.fail(f"Error executing file_handling_exercise.py: {e}")

        # Check if the file was created
        self.assertTrue(os.path.exists(self.file_path), "treasury_report.txt was not created.")

        # Check content of the written file
        with open(self.file_path, 'r') as f:
            content = f.read()
        expected_content = (
            "Daily Treasury Report\n"
            "Date: 2024-07-03\n"
            "-------------------\n"
            "Total Assets: $1,500,000\n"
            "Total Liabilities: $800,000\n"
        )
        self.assertEqual(content, expected_content, "Content written to file is incorrect.")

        # Check console output for write confirmation and read content
        output = self.new_stdout.getvalue()
        self.assertIn("Report written to treasury_report.txt", output, "Write confirmation message not found.")
        self.assertIn("--- Content of treasury_report.txt ---", output, "Read header not found.")
        self.assertIn(expected_content.strip(), output.strip(), "Read content not printed correctly.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
