# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: LeadTech
# Team Number: 
# Problem Number: 7 

import array
import math
import re
import string

# Class and function definitions:

# Main program:

def main():
    nums = []
    tempNums = input().split()
    tempNums = map(int, tempNums)
    resultNums = asscendSort(tempNums)
    result = ""
    for tempNum in resultNums:
        result += str(tempNum) + " "
    print(result)

def asscendSort(nums):
    return sorted(nums, reverse=True)

main()