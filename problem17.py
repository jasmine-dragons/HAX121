# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: LeadTech
# Team Number: P074
# Problem Number: 17

import array
import math
import re
import string

# Class and function definitions:

def isPrime(num):
    if num <= 1:
        return False
    for divide in range(2, num):
        if (num % divide) == 0:
            return False
    return True

def binaryPrime(nums):
    nums = sorted(nums)
    largestPrime = None
    for x in range (len(nums)-1, 0, -1):
        if (isPrime(nums[x])):
            largestPrime = nums[x]
            break

    left = 0
    right = len(nums) -1
    count = 0
    while (left <= right) :
        count += 1
        mid = (left +right)//2
        tempNum = nums[mid]

        if(nums[mid] == largestPrime):
            return count
        elif(nums[mid] < largestPrime):
            left = mid + 1
        else:
            right = mid-1


# Main program:

def main():
    nums = []
    tempNums = input('input: ').split()
    tempNums = map(int, tempNums)
    print(binaryPrime(tempNums))

main()
