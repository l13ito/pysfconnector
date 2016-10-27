# -*- coding: utf-8 -*-
def line_count_field(str, char):
    cont = 0
    quoteFound = False
    for i in str:
        if str[i] == '"' and quoteFound is False:
            quoteFound = True
        elif str[i] == '"' and quoteFound is True:
            quoteFound = False
        elif str[i] == char and quoteFound is False:
        # , or ;can be selected noted for
            cont += 1
    return cont + 1

def change_separator(char1, char2):

    quoteFound = False
    for i in str:
        if str[i] == '"' and quoteFound is False:
            quoteFound = True
        elif str[i] == '"' and quoteFound is True:
            quoteFound = False
        elif str[i] == char1 and quoteFound is False:
            str[i] = char2