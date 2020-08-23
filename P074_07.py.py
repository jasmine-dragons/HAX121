# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: LeadTech
# Team Number: P074
# Problem Number: 7

import array
import math
import re
import string

# Class and function definitions:
def main():
    nums = []
    tempNums = input().split()
    tempNums = list(map(int, tempNums))
    resultNums = asscendSort(tempNums)
    result = ""
    for tempNum in resultNums:
        result += str(tempNum) + " "
    print(result)

def asscendSort(nums):
    tempNums = []
    for x in range(len(nums)):
        tempNums.append(x)
    return sorted(tempNums, key=lambda x:nums[x])

# Main program:
main()
