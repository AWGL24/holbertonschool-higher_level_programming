#!/usr/bin/python3
for c in range(97, 122):
    if c not in [101, 113]:
        print(chr(c), end="")
