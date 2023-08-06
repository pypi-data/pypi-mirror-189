"""This parses HCL files"""
import hcl2
def open_file(file: str) -> dict:
    """
    Opens the terraform file and loads it as a dict
    """
    with open(file, encoding="utf8") as tf_file:
        return hcl2.load(tf_file)


def get_tf_file_type(hcl_dict: dict) -> str:
    """
    Read a HCL dict and determine if its a variable file or a outputs file
    """
    file_types = ["variable", "output"]
    file_type = next(iter(hcl_dict), None)
    if file_type not in file_types:
        raise ValueError("Invalid file type. Expected one of: %s" % file_types)
    return file_type


def parse_hcl(hcl_dict: dict, file_type: str) -> "list[dict]":
    """
    Parses the HCL dict given to the function.
    If output file type, will get the name and description
    """

    # Create a dictionary to store the default values
    default_values = {
        "description": None,
        "type": None,
        "default": None,
        "nullable": False
    }

    final_list = []
    for item in hcl_dict.get(file_type, []):
        name = list(item.keys())[0]
        temp_dict = {
            "name": name,
            "description": item[name].get("description", default_values["description"]),
        }

        if file_type == "variable":
            temp_dict.update({
                "type": item[name].get("type", default_values["type"]),
                "default": item[name].get("default", default_values["default"]),
                "nullable": item[name].get("nullable", default_values["nullable"]),
            })
        final_list.append(temp_dict)
    return final_list
