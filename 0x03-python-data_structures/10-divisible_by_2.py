#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return
    new_list1 = my_list.copy()
    for i in range(len(new_list1)):
        if new_list1[i] == 0:
            new_list1[i] = False
        elif (abs(new_list1[i]) % 2) == 0:
            new_list1[i] = True
        else:
            new_list1[i] = False
    return(new_list1)
