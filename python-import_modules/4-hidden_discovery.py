#!/usr/bin/python3
import importlib.util
import os

def print_module_names(filepath):
    # Get the module name from the filepath
    module_name = os.path.splitext(os.path.basename(filepath))[0]

    # Use importlib to load the module
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get the names defined by the module
    names = [name for name in dir(module) if not name.startswith("__")]

    # Sort the names and print them
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    filepath = "hidden_4.pyc"
    print_module_names(filepath)
