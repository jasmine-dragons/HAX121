# HAX 121 2020 Python (3.6.0) Submission Template
# Please fill out the info fields below for identification
# Do not modify any part of the template

# Team Name:
# Team Number:
# Problem Number:

import array
import math
import re
import string

# Class and function definitions:
def prime_factorization():
    number = int(input('number: '))
    output_string = ''
    while number % 2 == 0:
        output_string += '2 '
        number /= 2
    sqrt = int(math.sqrt(number))
    for i in range(3, sqrt + 1, 2):
        while number % i == 0:
            output_string += f'{int(i)} '
            number /= i
    if number > 2:
        output_string += f'{int(number)}'
    print(output_string)

# Main program:
prime_factorization()
