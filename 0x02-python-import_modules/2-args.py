#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argc = len(argv)
    if argc < 2:
        print("0 arguments.")
    for i in range(1, argc):
        if argc < 3:
            print("1 argument:")
            print("1: {}".format(argv[1]))
        else:
            if i == 1:
                print("{} arguments:".format(argc-1))
            print("{}: {}".format(i, argv[i]))
