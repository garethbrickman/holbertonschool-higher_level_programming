#!/usr/bin/python3
""" Funcion to find_peak """


def find_peak(list_of_integers):

    if list_of_integers:
        new_list = max(list_of_integers)
        return(new_list)
    else:
        return None

    # if list_of_integers is None:
    #     return None
    #     new_list = list_of_integers.copy()
    #     new_list.sort()
    #     for i in range(0, len(new_list)):
    #         if i == (len(new_list)-1):
    #             return(new_list[i])
