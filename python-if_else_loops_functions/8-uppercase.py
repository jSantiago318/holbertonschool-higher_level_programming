#!/usr/bin/python3

def uppercase(str):
    result = ""
    for c in str:
        o = ord(c)
        if 97 <= o <= 122:
            result += chr(o - 32)
        else:
            result += c
    print("{}".format(result))
