#!/usr/bin/python3

def search_replace(my_list, search, replace):

    new_list = my_list[:]
    for i in range(len(new_list)):
        if nre_list[i] == search:
            nre_list[i] = replace
    return (new_list)
