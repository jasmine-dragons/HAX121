# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name:LeadTech
# Team Number:P074
# Problem Number:3

import array
import math
import re
import string

# Class and function definitions:

def relprime():
    inp = input("input: ").split(" ")
    num1 = int(inp[0])
    num2 = int(inp[1])

    result = math.gcd(num1,num2)
    if result == 1:
        print(0)
    else:
        print(result)

# Main program:
relprime()
