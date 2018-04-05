"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def calculator_2():

    """ calculator function takes input from the user in format
    operator, number, number and returns result"""

    calculating = True

    while calculating:
        user_input = raw_input('Please enter an operator followed by numbers:')
        user_input = user_input.split(" ")
        operator = user_input[0]

        if validate_operator(operator) and validate_list_length(user_input) and validate_digits(user_input):

            for each in range(1, len(user_input)):
                    user_input[each] = float(user_input[each])

            if operator == "+":
                result = add(user_input[1], user_input[2])
            elif operator == "-":
                result = subtract(user_input[1], user_input[2])
            elif operator == "/":
                result = divide(user_input[1], user_input[2])
            elif operator == "*":
                result = multiply(user_input[1], user_input[2])
            elif operator == "square":
                result = square(user_input[1])
            elif operator == "cube":
                result = cube(user_input[1])
            elif operator == "pow":
                result = power(user_input[1], user_input[2])
            elif operator == "mod":
                result = mod(user_input[1], user_input[2])
            elif operator == "q" or operator == "quit":
                print "Quitting Program"
                calculating = False
            print result
        elif operator == "q" or operator == "quit":
                print "Quitting Program"
                calculating = False
        else:
            print "Please input valid format: operator number number"


def validate_operator(op):
    valid_operators = ['+', '-', '/', '*', 'square', 'cube', 'pow', 'mod']

    if op in valid_operators:
        return True
    else:
        return False


def validate_list_length(user_list):
    return len(user_list) <= 3


def validate_digits(user_list):
    for each in range(1, len(user_list)):
        if not user_list[each].isdigit():
            return False
    return True

calculator_2()
