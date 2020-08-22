# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name:LeadTech
# Team Number:P074
# Problem Number: 10

import array
import math
import re
import string

# Class and function definitions:
def removeExtraLetters(word):
    repeatedIndexes = []
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            repeatedIndexes.append(i)
    offset = 0
    for i in repeatedIndexes:
        word = word[0 : i-offset : ] + word[i+1-offset : :]
        offset = offset+1
    print(word)

def main():
    word = input("Enter Word: ").split()
    removeExtraLetters(word[0])

# Main program:
main()
