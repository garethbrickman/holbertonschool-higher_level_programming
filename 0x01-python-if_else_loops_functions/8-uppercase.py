#!/usr/bin/python3
def uppercase(str):
    strup = ''
    for i in range(len(str)):
        if(str[i] >= 'a' and str[i] <= 'z'):
            strup = strup + chr((ord(str[i]) - 32))
            if(len(strup) != len(str)):
                pass
            else:
                print(strup)
        else:
            strup = strup + str[i]
