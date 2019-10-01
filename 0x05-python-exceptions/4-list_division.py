#!/usr/bin/python3
def list_division(ml1, ml2, length):
        newlist = range(length)
        for i in range(length):
                try:
                        newlist = ml1[i] / ml2[i]
                except TypeError:
                        print("wrong type")
                except ZeroDivisionError:
                        print("division by 0")
                except IndexError:
                        print("out of range")
                finally:
                        return newlist
