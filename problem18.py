# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: LeadTech
# Team Number: P074
# Problem Number: 18

import array
import math
import re
import string

# Class and function definitions:
def biggest():
    input_string = input('input: ')
    split = input_string.split(' ')
    digits = int(split[0])
    sum = int(split[1])
    max = 0
    count = 0
    for i in range(10 ** (digits)):
        digit_sum = 0
        for dig in str(i):
            digit_sum += int(dig)
        if digit_sum == sum:
            max = i
    print(max)

# Main program:
biggest()
