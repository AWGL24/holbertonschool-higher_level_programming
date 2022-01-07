#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            newList[i] = replace
    return (newList)
