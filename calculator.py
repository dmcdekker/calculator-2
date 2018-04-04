"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator_2():
    calculating = True

    while calculating:
        user_input = raw_input()
        user_input = user_input.split(" ")

        for each in range(1,len(user_input)):
            user_input[each] = int(user_input[each])
        
        print user_input
        if user_input[0] == "+":
            result = add(user_input[1], user_input[2])
        elif user_input[0] == "-":
            result = subtract(user_input[1], user_input[2])
        elif user_input[0] == "/":
            result = divide(user_input[1], user_input[2])
        elif user_input[0] == "*":
            result = multiply(user_input[1], user_input[2])
        elif user_input[0] == "square":
            result = square(user_input[1])        
        elif user_input[0] == "cube":
            result = cube(user_input[1])
        elif user_input[0] == "pow":
            result = power(user_input[1], user_input[2])
        elif user_input[0] == "mod":
            result = mod(user_input[1], user_input[2])
        elif user_input[0] == "q" or user_input[0] == "quit":
            print "Quitting Program"
            calculating = False
        else:
            print "Please input valid things"

        print result  

calculator_2()           
