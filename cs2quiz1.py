#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# It's an assignment operator. It puts a value into variable. 
#
#
#2 3pts) Write a technical definition for 'function'
# A sequence of statements that performs an operation.
#
#
#3 1pt) What does the keyword "return" do?
# It spits out the result of the function. 
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: float : 0.1, 5.6
#	2: integer: 3, 100
#	3: string: "hello", "puppies"
#	4: boolean: True, False
#	5: tuple: ("Hello", "Bob", 3, "dog")
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# A function definition is a statement that makes a new function while a function call is a statement that executes a function. 
#
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: Input - Get data from the keyboard, a file, or another device.
#	2: Processing - Works out the data recieved.
#	3: Output - Displays data on the screen or send data to a file or other device.
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math 

def math.sqrt(c1, c2, c3)/ math.pi
    return math.sqrt(c1, c2, c3)/ math.pi

def output(c1, c2, c3):
    out = """

Circle       Diameter
Area of C1   c1
Area of C2   c2
Area of C3   c3
""".format(c1, c2, c3)
    return out

def main(): 
    c1=raw_input("Area of C1: ")
    c2=raw_input("Area of C2: ")
    c3=raw_input("Area of C3: ")
    
out = output(c1, c2, c3)
print out

main()
        
