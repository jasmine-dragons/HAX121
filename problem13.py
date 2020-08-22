# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: LeadTech
# Team Number: P074
# Problem Number: 13

import array
import math
import re
import string

# Class and function definitions:

class Person:
    def __init__(self, height, weight):
        self._height = height
        self._weight = weight

    def getHeight(self):
        return self._height

    def getWeight(self):
        return self._weight

    def setHeight(self, newHeight):
        self._height = newHeight

    def setWeight(self, newWeight):
        self._weight = newWeight

# Main program:
def main():
    people = []
    for x in range(5):
        nums = input().split()
        nums = list(map(int, nums))
        if (nums[0] > len(people)):
            people.append(Person(nums[1], nums[2]))
        else:
            people[nums[0]-1] = Person(nums[1], nums[2])
    for x in people:
        print(x.getHeight(), x.getWeight())

main()
