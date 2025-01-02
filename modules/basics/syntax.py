"""
Python Syntax and Comments

This module provides an in-depth explanation of Python syntax, including:
- Comments
- Indentation
- Variables
- Data types
- Conditionals
- Loops
- Functions
- Expressions and statements
"""

def comments_and_docstrings():
    """
    Explains how to use comments and docstrings in Python.
    """
    print("\n1. Comments and Docstrings:")
    # Single-line comment
    print("This is a single-line comment.")  # Comment at the end of a line

    """
    Multi-line comments are typically written using triple double-quotes
    or triple single-quotes.
    """
    print("Multi-line comments can also serve as documentation strings (docstrings).")


def indentation():
    """
    Demonstrates the importance of indentation in Python.
    """
    print("\n2. Indentation:")
    print("Python uses indentation to define blocks of code.")
    if True:
        print("This block is correctly indented.")
        print("Each level of indentation must be consistent.")


def variables_and_datatypes():
    """
    Explains variables and their types in Python.
    """
    print("\n3. Variables and Data Types:")
    name = "Alice"       # String
    age = 25             # Integer
    height = 5.5         # Float
    is_student = True    # Boolean
    print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")


def conditionals():
    """
    Demonstrates if-else statements in Python.
    """
    print("\n4. Conditionals:")
    num = 10
    if num > 0:
        print("The number is positive.")
    elif num == 0:
        print("The number is zero.")
    else:
        print("The number is negative.")


def loops():
    """
    Explains loops: for and while.
    """
    print("\n5. Loops:")
    print("For loop:")
    for i in range(5):
        print(f"Iteration {i+1}")

    print("While loop:")
    count = 0
    while count < 3:
        print(f"Count is {count}")
        count += 1


def functions():
    """
    Explains how to define and call functions in Python.
    """
    print("\n6. Functions:")

    def greet(name):
        """Function to greet a person."""
        return f"Hello, {name}!"

    print(greet("Alice"))


def expressions_and_statements():
    """
    Covers the basics of expressions and statements.
    """
    print("\n7. Expressions and Statements:")
    x = 10
    y = 20
    sum_result = x + y  # This is an expression
    print(f"The sum of {x} and {y} is {sum_result}")


def special_characters():
    """
    Demonstrates the use of escape characters in Python strings.
    """
    print("\n8. Special Characters:")
    print("Newline: Hello\nWorld!")
    print("Tab: Hello\tWorld!")
    print("Backslash: Hello\\World!")


def important_points():
    """
    Summarizes important points about Python syntax.
    """
    print("\n9. Important Points to Remember:")
    points = [
        "1. Python is case-sensitive.",
        "2. Statements are typically written on separate lines.",
        "3. Use a backslash (\\) to continue a statement on the next line.",
        "4. Indentation is mandatory; no braces are used for blocks.",
        "5. Use # for comments and \"\"\" for docstrings."
    ]
    for point in points:
        print(point)


if __name__ == "__main__":
    print("Welcome to Python Syntax!")
    comments_and_docstrings()
    indentation()
    variables_and_datatypes()
    conditionals()
    loops()
    functions()
    expressions_and_statements()
    special_characters()
    important_points()
