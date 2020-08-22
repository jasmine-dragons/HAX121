# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: LeadTech
# Team Number: P074
# Problem Number: 11

import array
import math
import re
import string

# Class and function definitions:
def insertion():
    swaps = 0
    list = input('numbers separated by spaces: ').split(' ')
    length = len(list)
    for i in range(1, length):
        position = i
        value = int(list[i])
        while position > 0 and int(list[position - 1]) > value:
            list[position] = list[position - 1]
            position -= 1
            swaps += 1
        list[position] = value
    print(swaps)

# Main program:
insertion()
