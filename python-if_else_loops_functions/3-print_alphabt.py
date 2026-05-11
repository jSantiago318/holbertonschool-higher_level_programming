#!/usr/bin/python3
print("{}".format(''.join(chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) not in ('q', 'e'))), end="")
