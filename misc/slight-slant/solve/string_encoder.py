#!/usr/bin/python3

def find(a):
    b = ""
    first = True
    for char in a:
        if first == True:
            b += ("().__doc__[" + str(().__doc__.index(char)) + "]")
            first = False
        else:
            b += (" + ().__doc__[" + str(().__doc__.index(char)) + "]")

    return b

print("system: " + find("system"))
print("sh: " + find("sh"))
