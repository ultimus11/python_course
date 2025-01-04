# test_intermediate.py

import unittest
from intermediate.modules import (
    using_math_module,
    using_datetime_module,
    using_os_module,
    using_requests_module,
    using_pandas_module,
    use_functions_module,
    use_file_handling_module
)
from intermediate.functions import add, multiply, greet, square
from intermediate.file_handling import write_to_file, read_from_file, append_to_file
import os

class TestModules(unittest.TestCase):

    def test_using_math_module(self):
        """Test for math module functions"""
        # Test expected output for some math operations
        self.assertAlmostEqual(math.pi, 3.141592653589793, places=6)
        self.assertEqual(math.sqrt(16), 4)
        self.assertEqual(math.pow(2, 3), 8)

    def test_using_datetime_module(self):
        """Test for datetime module"""
        # Test if the datetime function returns the current datetime
        now = datetime.datetime.now()
        self.assertIsInstance(now, datetime.datetime)
        self.assertTrue(now.year >= 2025)  # Assuming current year is 2025

    def test_using_os_module(self):
        """Test for os module"""
        # Test current working directory
        cwd = os.getcwd()
        self.assertTrue(os.path.isdir(cwd))

    def test_using_requests_module(self):
        """Test for requests module"""
        # Mock the HTTP request to avoid external dependencies (Using unittest.mock)
        with unittest.mock.patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.text = '{"title": "Test Post"}'
            response = requests.get("https://jsonplaceholder.typicode.com/posts")
            self.assertEqual(response.status_code, 200)
            self.assertIn('Test Post', response.text)

    def test_using_pandas_module(self):
        """Test for pandas module"""
        # Test if DataFrame is created correctly
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'Los Angeles', 'Chicago']
        }
        df = pd.DataFrame(data)
        self.assertEqual(len(df), 3)  # Should contain 3 rows
        self.assertEqual(df['Name'][0], 'Alice')  # Check first name

    def test_use_functions_module(self):
        """Test for functions from functions.py"""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(square(5), 25)

    def test_use_file_handling_module(self):
        """Test for file handling functions"""
        file_name = "test_file.txt"
        
        # Test writing to a file
        write_to_file(file_name, "Test content")
        self.assertTrue(os.path.exists(file_name))
        
        # Test reading from a file
        content = read_from_file(file_name)
        self.assertEqual(content, "Test content")
        
        # Test appending to a file
        append_to_file(file_name, "\nAppended content")
        content = read_from_file(file_name)
        self.assertIn("Appended content", content)
        
        # Clean up
        os.remove(file_name)

    # Additional tests for edge cases and error handling can be added here

if __name__ == "__main__":
    unittest.main()
