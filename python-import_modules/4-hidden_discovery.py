# /tmp/4-hidden_discovery.py

import importlib.util
import os
import sys

def get_defined_names(pyc_file):
    spec = importlib.util.spec_from_file_location("hidden_4", pyc_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    defined_names = [name for name in dir(module) if not name.startswith('__')]
    
    return sorted(defined_names)

if __name__ == "__main__":
    pyc_file = "/tmp/hidden_4.pyc"
    names = get_defined_names(pyc_file)
    
    for name in names:
        print(name)