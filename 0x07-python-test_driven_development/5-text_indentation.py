#!/usr/bin/python3
"""
     Module for text_indentation functions


"""


def text_indentation(text):
    """ Text indentation function

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text is "":
        raise TypeError("text must be a string")

    newtext = ""
    delims = ".?:"
    space = " "

    for i in range(len(text)):
        newtext += text[i]
        if text[i] in space:
            if text[i-1] in delims:
                continue
        if text[i] in delims:
            newtext += "\n\n"
    print(newtext)

    # indent1 = text.split(':')
    # indent2 = ':\n\n'.join(indent1)
    # indent3 = indent2.split('?')
    # indent4 = '?\n\n'.join(indent3)
    # indent5 = indent4.split('.')
    # indent6 = '.\n\n'.join(indent5)
    # print(indent6)
