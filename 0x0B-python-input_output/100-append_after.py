#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    list2 = []
    with open(filename, mode='r', encoding='utf-8') as f:
        x = f.readlines()
        for line in x:
            list2.append(line)
            if search_string in line:
                list2.append(new_string)
    with open(filename, mode='w', encoding='utf-8') as f:
        for line in list2:
            f.write(line)
