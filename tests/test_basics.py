import unittest
from io import StringIO
from contextlib import redirect_stdout

# Importing functions from basics module
from modules.basics.intro import (hello_world, python_features, print_example,
                                  input_example, comments_example)
from modules.basics.syntax import (indentation_example, conditional_statements,
                                    loops_example)
from modules.basics.variables import (variable_declaration_and_assignment, data_types,
                                       mutable_vs_immutable, scope_and_lifetime,
                                       naming_conventions, type_conversion,
                                       unpacking_variables)

class TestIntroModule(unittest.TestCase):
    def test_hello_world(self):
        """
        Test the hello_world function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            hello_world()
            output = buf.getvalue().strip()
        self.assertEqual(output, "Hello, World!", "hello_world function failed")

    def test_python_features(self):
        """
        Test python_features function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            python_features()
            output = buf.getvalue()
        self.assertIn("Easy to Learn", output, "python_features function failed to include 'Easy to Learn'")
        self.assertIn("Interpreted", output, "python_features function failed to include 'Interpreted'")

    def test_print_example(self):
        """
        Test the print_example function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            print_example()
            output = buf.getvalue()
        self.assertIn("The sum of 5 and 3 is 8", output, "print_example function failed")

    def test_comments_example(self):
        """
        Ensure comments_example executes without error.
        """
        try:
            comments_example()
        except Exception as e:
            self.fail(f"comments_example function raised an exception: {e}")


class TestSyntaxModule(unittest.TestCase):
    def test_indentation_example(self):
        """
        Test indentation_example function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            indentation_example()
            output = buf.getvalue().strip()
        self.assertIn("x is greater than 5", output, "indentation_example function failed")

    def test_conditional_statements(self):
        """
        Test conditional_statements function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            conditional_statements()
            output = buf.getvalue()
        self.assertIn("Positive number", output, "conditional_statements function failed")

    def test_loops_example(self):
        """
        Test loops_example function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            loops_example()
            output = buf.getvalue()
        self.assertIn("Current number is", output, "loops_example function failed")


class TestVariablesModule(unittest.TestCase):
    def test_variable_declaration_and_assignment(self):
        """
        Test variable_declaration_and_assignment function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            variable_declaration_and_assignment()
            output = buf.getvalue()
        self.assertIn("Name: Alice", output, "variable_declaration_and_assignment function failed")

    def test_data_types(self):
        """
        Test data_types function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            data_types()
            output = buf.getvalue()
        self.assertIn("Integer: 10", output, "data_types function failed for integer")
        self.assertIn("Float: 20.5", output, "data_types function failed for float")

    def test_mutable_vs_immutable(self):
        """
        Test mutable_vs_immutable function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            mutable_vs_immutable()
            output = buf.getvalue()
        self.assertIn("Immutable Example - Original: Hello", output, "mutable_vs_immutable function failed")
        self.assertIn("Mutable Example - Original: [1, 2, 3, 4]", output, "mutable_vs_immutable function failed")

    def test_scope_and_lifetime(self):
        """
        Test scope_and_lifetime function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            scope_and_lifetime()
            output = buf.getvalue()
        self.assertIn("Inside function: 10", output, "scope_and_lifetime function failed")
        self.assertIn("Outside function: 5", output, "scope_and_lifetime function failed")

    def test_type_conversion(self):
        """
        Test type_conversion function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            type_conversion()
            output = buf.getvalue()
        self.assertIn("Integer: 100", output, "type_conversion function failed")
        self.assertIn("Float: 100.0", output, "type_conversion function failed")

    def test_unpacking_variables(self):
        """
        Test unpacking_variables function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            unpacking_variables()
            output = buf.getvalue()
        self.assertIn("Unpacked Values - a: 1, b: 2, c: 3", output, "unpacking_variables function failed")
    
    def test_naming_conventions(self):
        """
        Test naming_conventions function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            naming_conventions()
            output = buf.getvalue()
        self.assertIn("Variable Name: my_variable", output, "naming_conventions function failed")
        self.assertIn("Function Name: my_function", output, "naming_conventions function failed")
        self.assertIn("Class Name: MyClass", output, "naming_conventions function failed")
    
    def test_input_example(self):
        """
        Test input_example function output.
        """
        with StringIO() as buf, redirect_stdout(buf):
            input_example()
            output = buf.getvalue()
        self.assertIn("Enter your name:", output, "input_example function failed")


if __name__ == "__main__":
    unittest.main()
