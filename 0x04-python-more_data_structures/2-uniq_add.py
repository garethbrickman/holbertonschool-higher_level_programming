#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    newlist = set(my_list)
    for x in newlist:
        sum += x
    return sum
