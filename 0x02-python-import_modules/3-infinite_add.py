#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    my_sum = 0
    for i in range(1, len(argv)):
        my_sum += int(argv[i])
    print("{}".format(my_sum))
