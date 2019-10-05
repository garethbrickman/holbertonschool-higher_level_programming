#!/usr/bin/python3
"""
     Module for say_my_name functions


"""


def say_my_name(first_name, last_name=""):
    """ Say name function

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name is "" and last_name is "":
        raise TypeError("You must enter a string for first_name or last_name")
    if first_name is " " and last_name is " ":
        raise TypeError("You must enter a string for first_name or last_name")

    print("My name is {} {}".format(first_name, last_name))
