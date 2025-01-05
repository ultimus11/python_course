# error_handling.py

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file {file_name} was not found."
    except IOError:
        return "Error: An issue occurred while reading the file."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Example usage
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Error: Division by zero is not allowed.
print(divide("10", 2))  # Output: Error: Both inputs must be numbers.

file_content = read_file("example.txt")
print(file_content)  # Output will depend on file existence and contents
