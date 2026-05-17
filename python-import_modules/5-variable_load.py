# /path/to/your/python-import_modules/5-variable_load.py

def import_variable(module_name, var_name):
    module = __import__(module_name)
    return getattr(module, var_name)

if __name__ == "__main__":
    a = import_variable("variable_load_5", "a")
    print(a)