# modules.py

# Importing standard Python modules
import math
import datetime
import os

# Importing third-party modules (ensure these are installed via pip)
import requests
import pandas as pd

# Importing functions from functions.py and file_handling.py (your custom modules)
from intermediate.functions import add, multiply, greet, square
from intermediate.file_handling import write_to_file, read_from_file, append_to_file

# 1. Using Built-in Python Modules
def using_math_module():
    """Demonstrates the usage of the math module."""
    print("Using math module:")
    pi = math.pi
    sqrt_16 = math.sqrt(16)
    power_2_3 = math.pow(2, 3)
    print(f"Pi: {pi}")
    print(f"Square root of 16: {sqrt_16}")
    print(f"2 raised to power 3: {power_2_3}")

def using_datetime_module():
    """Demonstrates the usage of the datetime module."""
    print("\nUsing datetime module:")
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")

def using_os_module():
    """Demonstrates the usage of the os module."""
    print("\nUsing os module:")
    current_directory = os.getcwd()
    print(f"Current working directory: {current_directory}")

# 2. Using Third-Party Modules

def using_requests_module():
    """Demonstrates the usage of the requests module to fetch a website."""
    print("\nUsing requests module:")
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully fetched data from {url}!")
        print(f"First 200 characters of the response:\n{response.text[:200]}")
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")

def using_pandas_module():
    """Demonstrates the usage of the pandas module."""
    print("\nUsing pandas module:")
    # Creating a simple dataframe using pandas
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    print(f"Created a DataFrame:\n{df}")

# 3. Using Custom Modules (functions.py and file_handling.py)
def use_functions_module():
    """Using functions from the functions module."""
    print("\nUsing functions module:")
    print(f"Addition of 5 and 3: {add(5, 3)}")
    print(f"Multiplication of 5 and 3: {multiply(5, 3)}")
    print(greet("Alice"))
    print(f"Square of 5: {square(5)}")

def use_file_handling_module():
    """Using functions from the file handling module."""
    print("\nUsing file handling module:")
    file_name = "example.txt"
    write_to_file(file_name, "Hello, this is a test content.")
    
    content = read_from_file(file_name)
    if content:
        print(f"Content read from {file_name}: {content}")
    
    append_to_file(file_name, "\nThis is appended content.")
    content = read_from_file(file_name)
    if content:
        print(f"Updated Content: {content}")

# Example of how you would use the above functions
if __name__ == "__main__":
    # Using standard built-in modules
    using_math_module()
    using_datetime_module()
    using_os_module()
    
    # Using third-party modules
    using_requests_module()
    using_pandas_module()
    
    # Using custom modules
    use_functions_module()
    use_file_handling_module()
