# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: LeadTech
# Team Number: P074
# Problem Number: 14

import array
import math
import re
import string

# Class and function definitions:
def sortStrings():
    list1 = input("input the first list, separated by a space between each value: ").split()
    list2 = input("input the second list, separated by a space between each value: ").split()

    comblist = list1 + list2
    comblist = map(int, comblist)
    print(sorted(comblist))

# Main program:
sortStrings()
