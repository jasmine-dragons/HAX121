# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name:LeadTech
# Team Number:P074
# Problem Number: 6

import array
import math
import re
import string

# Class and function definitions:
def getArea(nums):
    nums = list(nums)
    return .5 * nums[0] * nums[1]

def checkForTriple(nums):  #Run this program
    a = nums[0]
    b = nums[1]
    c = nums[2]
    if not a*a + b*b == c*c:
        print(0)
    else:
        print(getArea(nums))

# Main program:
def main():
    nums = input("each number separated by spaces: ").split()
    nums = list(map(int, nums))
    nums = sorted(nums)
    return(checkForTriple(nums))

main()
