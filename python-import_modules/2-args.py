#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    args = argv[1:]
    count = len(args)
    if count == 0:
        print("0 arguments.")
    else:
        if count == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(count))
        for i, val in enumerate(args, 1):
            print("{}: {}".format(i, val))
