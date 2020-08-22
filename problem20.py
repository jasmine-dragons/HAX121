# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: LeadTech
# Team Number: P074
# Problem Number: 20

import array
import math
import re
import string

# Class and function definitions:

class Person: 
    population = 0

    def __init__(self, height, weight):
        self._height = height
        self._weight = weight
        Person.setPopulation(Person.getPopulation() + 1)

    def getHeight(self):
        return self._height
    def getWeight(self):
        return self._weight
    def setHeight(self, newHeight):
        self._height = newHeight
    def setWeight(self, newWeight):
        self._weight = newWeight
    def getPopulation():
        return Person.population
    def setPopulation(newPop):
        Person.population = newPop
    
class Student(Person):
    def __init__(self, height, weight, major):
        self._height = height
        self._weight = weight
        self._major = major
        Person.setPopulation(Person.getPopulation() + 1)
    
    def setMajor(self, newMajor):
        self._major = newMajor
    def getMajor(self):
        return self._major

# Main program:
def main():
    people = []
    for x in range(5):
        nums = input().split()
        if (len(nums) == 4):
            if (int(nums[0]) > len(people)):
                people.append(Student(int(nums[1]), int(nums[2]), nums[3]))
            else: 
                people[int(nums[0])-1].setHeight(int(nums[1]))
                people[int(nums[0])-1].setWeight(int(nums[2]))
                people[int(nums[0])-1].setMajor(nums[3])
        else:
            if (int(nums[0]) > len(people)):
                people.append(Person(int(nums[1]), int(nums[2])))
            else:
                people[int(nums[0])-1].setHeight(int(nums[1]))
                people[int(nums[0])-1].setWeight(int(nums[2]))
    for x in people:
        if (isinstance(x, Student)):
            print(x.getHeight(), x.getWeight(), x.getMajor())
        else:
            print(x.getHeight(), x.getWeight())
    print(Person.population)

main()