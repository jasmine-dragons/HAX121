# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name:LeadTech
# Team Number:P074
# Problem Number:1

import array
import math
import re
import string

# Class and function definitions:
def alphabet (num) :
    letters = string.ascii_lowercase
    letter_list = list(letters)
    out = " "

    for x in range(0, num):
        out += letter_list[x]

    print(out)


# Main program:

def main():
    alphabet(4)
    alphabet(8)
