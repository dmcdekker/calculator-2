"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def calculator_2():

    """calculator function takes input from the user in format
    operator, number, number and returns result"""

    calculating = True

    while calculating:
        user_input = raw_input('Please enter an operator followed by numbers:\n')
        user_input = user_input.split(" ")
        operator = user_input[0]

        if validate_operator(operator, ['+', '-', '/', '*', 'pow', 'mod']) and len(user_input[1:]) >= 2 and validate_digits(user_input):

            for each in range(1, len(user_input)):
                user_input[each] = float(user_input[each])

            if operator == "+":
                result = reduce(lambda x, y: add(x, y), user_input[1:])
            elif operator == "-":
                result = reduce(lambda x, y: subtract(x, y), user_input[1:])
            elif operator == "/":
                result = reduce(lambda x, y: divide(x, y), user_input[1:])
            elif operator == "*":
                result = reduce(lambda x, y: multiply(x, y), user_input[1:])
            elif operator == "pow":
                result = reduce(lambda x, y: power(x, y), user_input[1:])
            elif operator == "mod":
                result = reduce(lambda x, y: mod(x, y), user_input[1:])
            print result
        elif validate_operator(operator, ['square', 'cube']) and validate_list_length(user_input, 2) and validate_digits(user_input):
            for each in range(1, len(user_input)):
                user_input[each] = float(user_input[each])

            if operator == "square":
                result = square(user_input[1])
            elif operator == "cube":
                result = cube(user_input[1])
            print result
        elif operator == "q" or operator == "quit":
                print "Quitting Program"
                calculating = False
        else:
            print "Please input valid format: operator number number\n"


def validate_operator(op, valid_operators):
    """ensures that the operator entered by the user is valid"""

    if op in valid_operators:
        return True
    else:
        return False


def validate_list_length(user_list, list_length):
    """validates that the length of the user_list is correct"""

    return len(user_list) == list_length


def validate_digits(user_list):
    """validates that the user input is a digit"""

    for each in range(1, len(user_list)):
        if not user_list[each].isdigit():
            return False
    return True

calculator_2()
