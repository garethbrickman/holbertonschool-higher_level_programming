#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absnum = abs(number)
modnum = absnum % 10

if number == 0:
    print('Last digit of {} is {} and is 0'.format(number, modnum))
elif modnum == 0:
    print('Last digit of {} is {} and is 0'.format(number, modnum))
elif modnum > 5:
    print('Last digit of {} is {} and is greater than 5'
          .format(number, modnum))
elif modnum < 6 and modnum != 0:
    print('Last digit of {} is {} and is less than 6 and not 0'
          .format(number, modnum))

# if number == 0:
#     print('Last digit of {} is {} and is 0'.format(number, number % 10))

# elif number < 0:

#     posnumber = number * -1
#     if (posnumber % 10) == 0:
#         print('Last digit of {} is {} and is 0'
#               .format(number, posnumber % 10))
#     elif (posnumber % 10) > 5:
#         print('Last digit of {} is {} and is greater than 5'
#               .format(number, posnumber % 10))
#     elif (posnumber % 10) < 6:
#         print('Last digit of {} is {} and is less than 6 and not 0'
#               .format(number, posnumber % 10))

# elif number > 0:

#     if (number % 10) == 0:
#         print('Last digit of {} is {} and is 0'.format(number, number % 10))
#     elif (number % 10) > 5:
#         print('Last digit of {} is {} and is greater than 5'
#               .format(number, number % 10))
#     elif (number % 10) < 6:
#         print('Last digit of {} is {} and is less than 6 and not 0'
#               .format(number, number % 10))
