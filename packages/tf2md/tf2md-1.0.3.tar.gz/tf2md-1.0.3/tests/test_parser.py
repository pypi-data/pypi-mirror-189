import sys
import pytest
from tf2md.parser import get_tf_file_type, open_file, parse_hcl
sys.path.append("..")

def test_variable_file_type():
    hcl_dict = {"variable": {}}
    file_type = get_tf_file_type(hcl_dict)
    assert file_type == "variable"

def test_output_file_type():
    hcl_dict = {"output": {}}
    file_type = get_tf_file_type(hcl_dict)
    assert file_type == "output"

def test_invalid_file_type():
    hcl_dict = {"invalid": {}}
    with pytest.raises(ValueError):
        get_tf_file_type(hcl_dict)


def test_open_file_with_valid_file():
    file_path = "tests/outputs.tf"
    # You will need to create the file with some valid HCL content and make sure the file path is correct
    hcl_dict = open_file(file_path)
    assert isinstance(hcl_dict, dict)

def test_open_file_with_nonexistent_file():
    file_path = "nonexistent_file.tf"
    with pytest.raises(FileNotFoundError):
        open_file(file_path)


import pytest

def test_parse_hcl_variable_file():
    hcl_dict = {
        "variable": [
            {
                "foo": {
                    "description": "The description of foo",
                    "type": "string",
                    "default": "bar",
                    "nullable": False
                }
            },
            {
                "baz": {
                    "description": "The description of baz",
                    "type": "number",
                    "default": 42,
                    "nullable": True
                }
            }
        ]
    }
    file_type = "variable"

    result = parse_hcl(hcl_dict, file_type)

    assert len(result) == 2
    assert result == [
        {
            "name": "foo",
            "description": "The description of foo",
            "type": "string",
            "default": "bar",
            "nullable": False
        },
        {
            "name": "baz",
            "description": "The description of baz",
            "type": "number",
            "default": 42,
            "nullable": True
        }
    ]

def test_parse_hcl_output_file():
    hcl_dict = {
        "output": [
            {
                "foo": {
                    "description": "The description of foo"
                }
            },
            {
                "baz": {
                    "description": "The description of baz"
                }
            }
        ]
    }
    file_type = "output"

    result = parse_hcl(hcl_dict, file_type)

    assert len(result) == 2
    assert result == [
        {
            "name": "foo",
            "description": "The description of foo",
        },
        {
            "name": "baz",
            "description": "The description of baz",
        }
    ]
