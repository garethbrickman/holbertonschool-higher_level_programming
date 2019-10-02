#!/usr/bin/python3
def list_division(ml1, ml2, length):
        newlist = []
        for i in range(length):
                try:
                        ans = ml1[i] / ml2[i]
                except TypeError:
                        ans = 0
                        print("wrong type")
                except ZeroDivisionError:
                        ans = 0
                        print("division by 0")
                except IndexError:
                        ans = 0
                        print("out of range")
                finally:
                        newlist.append(ans)
        return newlist
