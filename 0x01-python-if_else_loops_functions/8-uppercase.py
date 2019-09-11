#!/usr/bin/python3
def uppercase(str):
    strup = ''  # Define variable to store uppercase change

    for i in range(len(str)):  # Loop through string in range of length

        if(str[i] >= 'a' and str[i] <= 'z'):  # Lowercase check
            strup = strup + chr((ord(str[i]) - 32))  # Uppercase change

            if(len(strup) != len(str)):
                pass  # Skip printing until loop is fully complete
            else:
                print(strup)
        else:
            strup = strup + str[i]  # Includes existing uppercase
