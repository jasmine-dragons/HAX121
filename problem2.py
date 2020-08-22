# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name:LeadTech
# Team Number:P074
# Problem Number:2

import array
import math
import re
import string

# Class and function definitions:
def cipher():
    input_string = str(input('string: '))
    output_string = ''
    if input_string.islower() == False or ' ' in input_string:
        print('invalid string')
    for character in input_string.lower():
        if character >= 'x':
            character = chr(ord(character) - 26)
        letter = chr(ord(character) + 3)
        output_string += letter
    print(output_string)

# Main program:
cipher()
