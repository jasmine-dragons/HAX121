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

def range():
    num_list = input("data: ")
    num_list = num_list.split()
    min = int(num_list[0])
    max = int(num_list[0])

    for x in num_list:
        y = int(x)
        if y < max:
            min = y
        if y > min:
            max = y

    print(max - min)



# Main program:
