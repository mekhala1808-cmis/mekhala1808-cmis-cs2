#Section 1: Terminology
# 1) What is a recursive function?
# A function that calls itself repeatedly. 
#
#
# 2) What happens if there is no base case defined in a recursive function?
# It will go on infinitely. 
#
#
# 3) What is the first thing to consider when designing a recursive function?
# The base case.
#
#
# 4) How do we put data into a function call?
# raw_inuput
#
# 
# 5) How do we get data out of a function call?
# logical operations (if, elid, else) and relational operaters (==, => etc.)
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 1 + (2, 5)
#a2 = 1 + (6, 1)
#a3 = -1

#b1 = 2
#b2 = 1 + (1, 0)
#b3 = 1 + (-1, 4)

#c1 = 1 + (-2, 2)
#c2 = 4
#c3 = 10 + (5, 4)

#d1 = 6
#d2 = 1 + (3, 1, 3)
#d3 = 1 - (2, 2, 1)

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def averageodd(number):
    number = raw_input("Next number: ")
#BASE CASE
    if number == "":
        print averageodd
#RECURSIVE CASE
    elif number == not bool(number):
        return print "The average of the odd numbers are " + str(averageodd(odds))
    odds = not bool(number)
    averageodd = odds/ odds
average(number)



def main():
    print "The average of the odd numbers are " + str(out)
main()



