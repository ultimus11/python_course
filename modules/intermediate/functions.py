# functions.py

# A simple function that adds two numbers
def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b

# A function to check if a number is prime
def is_prime(num):
    """Returns True if the number is prime, otherwise False."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# A recursive function that returns the factorial of a number
def factorial(n):
    """Returns the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# A lambda function to calculate the square of a number
square = lambda x: x ** 2

# A decorator function to time how long a function takes
import time
def time_function(func):
    """Decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Example usage of a decorator
@time_function
def slow_function():
    """Function that sleeps for 2 seconds."""
    time.sleep(2)
    return "Finished"

# Function with error handling: Division
def safe_divide(a, b):
    """Safely divides a by b, handling ZeroDivisionError."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
