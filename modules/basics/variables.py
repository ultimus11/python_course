"""
Python Variables and Data Types

This module provides an in-depth explanation of variables in Python, including:
- Variable declaration and assignment
- Data types
- Mutable and immutable variables
- Scope and lifetime of variables
- Naming conventions
- Type conversion
"""

def variable_declaration_and_assignment():
    """
    Demonstrates how to declare and assign variables.
    """
    print("\n1. Variable Declaration and Assignment:")
    name = "Alice"       # String
    age = 25             # Integer
    height = 5.5         # Float
    is_student = True    # Boolean
    print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")


def data_types():
    """
    Explains common data types in Python.
    """
    print("\n2. Data Types:")
    integer = 10            # Integer
    floating_point = 20.5   # Float
    string = "Hello"        # String
    boolean = True          # Boolean
    list_type = [1, 2, 3]   # List
    tuple_type = (1, 2, 3)  # Tuple
    set_type = {1, 2, 3}    # Set
    dict_type = {"key": "value"}  # Dictionary

    print(f"Integer: {integer}, Type: {type(integer)}")
    print(f"Float: {floating_point}, Type: {type(floating_point)}")
    print(f"String: {string}, Type: {type(string)}")
    print(f"Boolean: {boolean}, Type: {type(boolean)}")
    print(f"List: {list_type}, Type: {type(list_type)}")
    print(f"Tuple: {tuple_type}, Type: {type(tuple_type)}")
    print(f"Set: {set_type}, Type: {type(set_type)}")
    print(f"Dictionary: {dict_type}, Type: {type(dict_type)}")


def mutable_vs_immutable():
    """
    Discusses mutable and immutable variables.
    """
    print("\n3. Mutable vs Immutable Variables:")
    # Immutable: String
    string1 = "Hello"
    string2 = string1
    string2 = "World"
    print(f"Immutable Example - Original: {string1}, Modified: {string2}")

    # Mutable: List
    list1 = [1, 2, 3]
    list2 = list1
    list2.append(4)
    print(f"Mutable Example - Original: {list1}, Modified: {list2}")


def scope_and_lifetime():
    """
    Explains the scope and lifetime of variables.
    """
    print("\n4. Scope and Lifetime:")

    def local_scope():
        x = 10  # Local variable
        print(f"Inside function: {x}")

    x = 5  # Global variable
    local_scope()
    print(f"Outside function: {x}")


def naming_conventions():
    """
    Explains naming conventions for variables.
    """
    print("\n5. Naming Conventions:")
    valid_variable = "Valid"
    _private_variable = "Private"
    camelCaseVariable = "CamelCase"
    snake_case_variable = "SnakeCase"

    print(f"Valid: {valid_variable}")
    print(f"Private: {_private_variable}")
    print(f"Camel Case: {camelCaseVariable}")
    print(f"Snake Case: {snake_case_variable}")

    # Avoid using keywords as variable names
    # For example: `for = 10` is invalid


def type_conversion():
    """
    Demonstrates type conversion in Python.
    """
    print("\n6. Type Conversion:")
    num_str = "100"  # String
    num_int = int(num_str)  # Convert to integer
    num_float = float(num_str)  # Convert to float
    print(f"String: {num_str}, Integer: {num_int}, Float: {num_float}")

    num = 42  # Integer
    num_to_str = str(num)  # Convert to string
    print(f"Integer: {num}, String: {num_to_str}")


def unpacking_variables():
    """
    Explains unpacking variables in Python.
    """
    print("\n7. Variable Unpacking:")
    numbers = (1, 2, 3)
    a, b, c = numbers
    print(f"Unpacked Values - a: {a}, b: {b}, c: {c}")

def input_example():
    """
    Demonstrates how to take user input in Python.
    """
    print("\n8. Input Example:")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Name: {name}, Age: {age}")


if __name__ == "__main__":
    print("Welcome to Python Variables and Data Types!")
    variable_declaration_and_assignment()
    data_types()
    mutable_vs_immutable()
    scope_and_lifetime()
    naming_conventions()
    type_conversion()
    unpacking_variables()
