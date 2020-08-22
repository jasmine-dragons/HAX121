# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name:
# Team Number:
# Problem Number:

import array
import math
import re
import string

# Class and function definitions:

def relprime():
    num1 = input("num1: ")
    num1 = int(num1)
    num2 = input("num2: ")
    num2 = int(num2)
    if int(math.gcd(num1, num2)) == 1:
        print(0)
    else:
        print(math.gcd(num1, num2))

# Main program:
