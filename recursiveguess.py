
import random

def rounds(numberrounds, c): 
	if numberrounds == 0: 
		return "You got " + str(c) + " rounds correct." 
	else:
		print "Starting round" + str(numberrounds)
		c += guess(random.randint(1, 100), 6)
		return rounds(numberrounds - 1, c)
def guess(random, attempt): 
	input = int(raw_input("Guess a number: "))
	if input == random: 
		print "That's correct!"
		return 1 
	elif attempt == 1: 
		print "The answer was " + str(random) + " You aren't that good at this game"
		return 0
	elif input > random: 
		print "That's too high." 
		return guess(random, attempt -1) 
	elif input < random: 
		print "That's too low."
		return guess(random, attempt -1)  
def main(): 
	result = rounds(1,0) 
	print result
main()
 

