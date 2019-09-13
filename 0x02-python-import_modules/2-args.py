#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    for i in range(len(sys.argv)):
       if len(sys.argv) < 2:
           print("0 arguments.")
           break
       elif len(sys.argv) < 3:
           print("1 argument:")
           print("1: {}".format(sys.argv[1]))
           break
       else:
           print("{} arguments:".format(len(sys.argv)-1))
           print("{}: {}".format(len(sys.argv), sys.argv[1]))
