#!/usr/bin/python3
"""
    prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    prints text followed by 2 new lines after ".", "?", or ":"

    @text: the text to be printed
    """
    if not isinstance(text, str) or text is None or len(text) <= 0:
        raise TypeError('text must be a string')
    signal = 1
    for i in text:
        if i == '?' or i == ':' or i == '.':
            print(i, end="\n\n")
            signal = 0
        else:
            if signal == 1:
                if i == '\t' or i == '\n' or i == '\v':
                    pass
                else:
                    print(i, end="")
            else:
                if i == ' ' or i == '\t':
                    pass
                else:
                    print(i, end="")
                    signal = 1
