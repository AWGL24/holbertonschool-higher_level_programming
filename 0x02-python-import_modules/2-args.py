#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    argv_len = len(argv) - 1

if argv_len == 0:
    print("{:d} arguments:".format(argv_len))
elif argv_len == 1:
    print("{:d} argument:".format(argv_len))
    print("{:d}: {}".format(argv_len, argv[1]))
else:
    print("{:d} arguments:".format(argv_len))
    for i in range(1, argv_len + 1):
        print("{:d}: {}".format(i, argv[i]))
