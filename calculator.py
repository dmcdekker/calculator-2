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
        user_input = raw_input('Please enter an operator followed by numbers:\n')
        user_input = user_input.split(" ")
        operator = user_input[0]

        if validate_operator(operator, ['+', '-', '/', '*', 'pow', 'mod']) and validate_list_length(user_input, 3) and validate_digits(user_input):

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
            
            elif operator == "pow":
                result = power(user_input[1], user_input[2])
            elif operator == "mod":
                result = mod(user_input[1], user_input[2])
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
    

    if op in valid_operators:
        return True
    else:
        return False


def validate_list_length(user_list, list_length):
    return len(user_list) == list_length


def validate_digits(user_list):
    for each in range(1, len(user_list)):
        if not user_list[each].isdigit():
            return False
    return True

calculator_2()
