#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) >
#b) <
#c) ==
#
#2) What does 'return' do?
#Return spits out the value of a function.
#
#
#
#3) What are 2 ways indentation is important in python code?
#a)Indentation tells you where the code begins.
#b)Indentation tells you where the code ends. 
#Also makes the code more organized and readable. 
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) 36
#problem1_b) square root of 3
#problem1_c) square root of 0
#problem1_d) 5
#
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) True
#
#problem3_a) c
#problem3_b) b
#problem3_c) a
#problem3_d) b
#
#problem4_a) 7
#problem4_b) 5
#problem4_c) 0.125
#problem4_d) 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

import math

print "Type in 3 different numbers (decimals are ok)"

def main():
    N1 = float(raw_input("A: "))
    N2 = float(raw_input("B: "))
    N3 = float(raw_input("C: "))
    if N1 > N2 and N1 > N3:
        print "The largest number is " + str(N1) + "."
    elif N1 == N2 or N1 == N3:
        print "You didn't follow directions."
    elif N2 > N1 and N2 > N3:
        print "The largest number is " + str(N2) + "."
    elif N2 == N1 or N2 == N3:
        print "You didn't follow directions."
    else:
        print "The largest number is " + str(N3) + "."
main()



 
