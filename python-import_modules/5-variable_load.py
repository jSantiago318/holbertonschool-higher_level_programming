#!/usr/bin/python3

def import_variable(module_name, var_name):
    module = __import__(module_name)
    return getattr(module, var_name)

if __name__ == "__main__":
    try:
        a = import_variable("variable_load_5", "a")
        print(a)
    except ImportError:
        print("Module 'variable_load_5' is not found.")
    except AttributeError:
        print("Variable 'a' is not defined in the module.")
        