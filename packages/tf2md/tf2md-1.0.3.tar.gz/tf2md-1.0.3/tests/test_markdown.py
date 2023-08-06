import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tf2md.markdown import create_output_file, tf_var_type_cleaner, create_variables_file


def test_create_output_file():
    outputs = [{"name": "output1", "description": "This is output1"},
               {"name": "output2", "description": "This is output2"}]
    output_file = "Outputs"
    create_output_file(outputs, output_file)

    # Check if the markdown file was created
    assert os.path.exists(f"{output_file}.md")

    # Clean up
    os.remove(f"{output_file}.md")


def test_tf_var_type_cleaner():
    # Test a string with all characters to be removed
    input_string = "${string}"
    expected_output = "string"
    assert tf_var_type_cleaner(input_string) == expected_output

    # Test a string with no characters to be removed
    input_string = "string"
    expected_output = "string"
    assert tf_var_type_cleaner(input_string) == expected_output

    # Test an empty string
    input_string = ""
    expected_output = ""
    assert tf_var_type_cleaner(input_string) == expected_output

    # Test a string with multiple instances of characters to be removed
    input_string = "${string} with ${extra} characters"
    expected_output = "string with extra characters"
    assert tf_var_type_cleaner(input_string) == expected_output




def test_create_variables_file():
    variables = [
        {"name": "variable_1", "description": "Description of variable_1", "type": "string", "nullable": "yes", "default": "default_1"},
        {"name": "variable_2", "description": "Description of variable_2", "type": "int", "nullable": "no", "default": None},
        {"name": "variable_3", "description": "Description of variable_3", "type": "bool", "nullable": "yes", "default": "true"}
    ]
    variable_file = "TestVariables"
    create_variables_file(variables, variable_file)
    assert os.path.exists(f"{variable_file}.md")

    # Clean up created file
    os.remove(f"{variable_file}.md")

def test_create_variables_file_default_variable_file_name():
    variables = [
        {"name": "variable_1", "description": "Description of variable_1", "type": "string", "nullable": "yes", "default": "default_1"},
        {"name": "variable_2", "description": "Description of variable_2", "type": "int", "nullable": "no", "default": None},
        {"name": "variable_3", "description": "Description of variable_3", "type": "bool", "nullable": "yes", "default": "true"}
    ]
    create_variables_file(variables)
    assert os.path.exists("Variables.md")

    # Clean up created file
    os.remove("Variables.md")