#!/usr/bin/python3
import importlib.util
import os

def print_variable_value(filepath, variable_name):
    # Get the module name from the filepath
    module_name = os.path.splitext(os.path.basename(filepath))[0]

    # Use importlib to load the module
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get the variable value
    variable_value = getattr(module, variable_name)
    print(variable_value)

if __name__ == "__main__":
    filepath = "variable_load_5.py"
    variable_name = "a"
    print_variable_value(filepath, variable_name)
