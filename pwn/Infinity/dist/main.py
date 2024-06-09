#!/bin/python3
import math

with open("flag.txt", "r") as f:
    flag = f.readline()

try:
    while True:
        inp = input("What is bigger than infinity? ")
        if(len(inp) > 100):
            print("I'm not processing that big of a number")
            continue
        
        if(not inp[0].isdigit()):
            print("Thats not a number >:(")
            continue

        inp = float(inp)

        if(inp >= math.inf):
            print("Wow that's a really big number!")
            print(flag)
            break
        else:
            print("Nuh uh that ain't bigger than infinity.")
except:
    print("Oops something went wrong")