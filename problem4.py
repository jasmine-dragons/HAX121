# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name: LeadTech
# Team Number: P074
# Problem Number: 6

import array
import math
import re
import string

# Class and function definitions:
def bank():
    balance = 100
    for i in range(5):
        trans = str(input('transaction: '))
        list = trans.split(' ')
        amount = int(list[1])
        if list[0] == 'deposit':
            balance += amount
        elif list[0] == 'withdraw':
            balance -= amount
    print(balance)

# Main program:
bank()
