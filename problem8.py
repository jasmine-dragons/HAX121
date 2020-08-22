# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name:LeadTech
# Team Number:P074
# Problem Number:8

import array
import math
import re
import string

# Class and function definitions:

def range():
    num_list = input("input the data, separated by a space between each value: ")
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
