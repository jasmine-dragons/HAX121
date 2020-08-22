# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: LeadTech
# Team Number: P074
# Problem Number: 12

import array
import math
import re
import string

# Class and function definitions:
def steps():
    distance = input("distance: ")
    distance = int(distance)
    fives = int(distance / 5)
    distance = distance % 5
    threes = int(distance / 3)
    distance = distance % 3

    print(int(fives + threes + distance))
# Main program:
steps()
