{
  "name": "create_new_file",
  "arguments": {
    "filepath": "python-data_structures/0-print_list_integer.py",
    "contents": "def print_list_integer(my_list=[]):\n    for i in my_list:\n        try:\n            print(\"{:d}\".format(i))\n        except ValueError:\n            raise ValueError('List contains non-integer values')"
  }
}