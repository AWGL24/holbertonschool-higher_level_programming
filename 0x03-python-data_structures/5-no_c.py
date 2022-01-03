#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for idx in my_string:
        if idx != 'c' and idx != 'C':
            new += idx
    return new
