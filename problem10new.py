import array
import math
import re
import string

# Class and function definitions:
def removeExtraLetters(word):
    output = ""
    prevLetter = ""
    for i in range(len(word)-1):

        if(word[i] != prevLetter):
            prevLetter = word[i]
            output = output + word[i]

    print(output)

def main():
    word = input("Enter Word: ").split()
    removeExtraLetters(word[0])

# Main program:
main()
