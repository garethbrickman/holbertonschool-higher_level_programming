#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
        if idx < 0:
                return my_list
        elif idx >= len(my_list):
                return my_list
        else:
                my_list.insert(idx, element)
                my_list.remove(idx + 1)
                return my_list
