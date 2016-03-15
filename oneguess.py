import math
import random

minimumnumber= raw_input( "What is the minimum number?: ")
maximumnumber= raw_input( "What is the maximum number?: ")

print "I'm thinking of a number from " + str(minimumnumber) + " to " + str(maximumnumber) + "."

targetnumber= raw_input( "What do you think it is?: ")

def output(minimumnumber, maximumnumber, targetnumber):
	out = """

