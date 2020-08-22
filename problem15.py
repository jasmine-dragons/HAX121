# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: LeadTech
# Team Number: P074
# Problem Number: 15

import array
import math
import re
import string

# Class and function definitions:
def goodNum():
    num = input("num: ")
    num = str(num)
    length = len(num)

    output = ""
    length1 = length
    for i in range(length):
        if num[i] != '0':
            value = num[i]
            for j in reversed(range(length1-1)):
                value += "0"
            length1-=1
            output += f"{value} "


    print(output)

# Main program:

goodNum()
