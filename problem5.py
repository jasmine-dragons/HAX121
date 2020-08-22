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
def vowels():
    input_string = input('string: ')
    output_string = ''
    for character in input_string:
        letter = character
        if ord(character) == 97 or ord(character) == 101 or ord(character) == 105 or ord(character) == 111 or ord(character) == 117:
            letter = chr(ord('*'))
        elif ord(character) == 65 or ord(character) == 69 or ord(character) == 73 or ord(character) == 79 or ord(character) == 85:
            letter = chr(ord('&'))
        output_string += letter
    print(output_string)

# Main program:
vowels()
