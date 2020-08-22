# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: LeadTech
# Team Number: P074
# Problem Number: 16

import array
import math
import re
import string

# Class and function definitions:

# Main program:

def main():
    tempNum = int(input())
    print(largestPrime(tempNum))

def largestPrime(num):
    for x in range(num-1, 2, -1):
        if (isPrime(x)):
            return x 
    return 2

def isPrime(num): 
    if num <= 1:
        return False
    for divide in range(2, num):
        if (num % divide) == 0:
            return False 
    return True

main()