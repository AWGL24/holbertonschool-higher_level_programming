#!/usr/bin/python3
from unittest import result


def list_division(my_list_1, my_list_2, list_lenght):
    my_list_3 = []
    result = None
    for i in range(list_lenght):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            my_list_3.append(result)
    return my_list_3