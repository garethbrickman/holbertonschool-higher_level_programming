#!/usr/bin/python3
def uppercase(str):
    strup = ''
    if len(str) < 1:
        print(("{}").format(str))
    for i in range(len(str)):
        if(str[i] >= 'a' and str[i] <= 'z'):
            strup = strup + chr((ord(str[i]) - 32))
            if(len(strup) != len(str)):
                pass
            else:
                print(("{}").format(strup))
        else:
            strup = strup + str[i]
