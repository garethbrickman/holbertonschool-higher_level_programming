#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argc = len(argv)
    ops = ['+', '-', '*', '/']

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    user_op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if user_op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if user_op == '+':
        print("{:d} {} {:d} = {:d}".format(a, user_op, b, add(a, b)))
    if user_op == '-':
        print("{:d} {} {:d} = {:d}".format(a, user_op, b, sub(a, b)))
    if user_op == '*':
        print("{:d} {} {:d} = {:d}".format(a, user_op, b, mul(a, b)))
    if user_op == '/':
        print("{:d} {} {:d} = {:d}".format(a, user_op, b, div(a, b)))
