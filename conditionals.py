# The world has been taken over by zombies and you have a gun and 5 choices of bullets for it.
#The computer will ask where you are and how many zombies are about to attack you.
#Then the computer will respond and tell you to hide and use your gun to protect youself.
#Next, the computer asks what type of bullet you'd like to shoot with.
#You will have to choose and type the bullet you want for your gun, each bullet has a different fatality rate caused upon the enemy. 
# The computer will respond according to what type of bullet you choose.

import math
import random

def main():
    place = raw_input( "Where are you?: ")
    amountofzombies = raw_input( "About how many zombies are about to attack you?: ")
    output = """
You're at {} !? 
You gotta find a place to hide or you'll get eaten! 
{} zombies? 
that's not good... 
USE YOUR GUN
""".format(place, amountofzombies)
    print output

    bullet = raw_input( "Choose what bullet you want to use with your gun- marshmallow, bouncyball, paintball, wood, titanium, or diamond: ")

def shoot(bullet):

    if bullet == "marshmallow":
	fatality = 0    
    elif bullet == "bouncyball":
	fatality = 1
    elif bullet == "paint ball":
	fatality = 2
    elif bullet == "wood":
        fatality = 3
    elif bullet == "titanium":
        fatality = 4
    elif bullet == "diamond":
        fatality = 5
    else:
        fatality = random.randint(0,5)
    return fatality * random.random()

def chosen(bullet):
    if bullet == marshmallow:
	    print "YOU HAVE BEEN EATEN, You are gonna turn into a zombie"
    elif bullet == bouncyball:
	    print "You've been bitten."
    elif bullet == paintball:
	    print "They are grabbing onto you."
    elif bullet == wood:
	    print "Keep shooting at them, you will get away."
    elif bullet == titanium:
	    print "You got away!"
    elif bullet == diamond:
	    print "YOU KILLED THEM!"
chosen(bullet)

food = raw_input("You need some food to eat so you keep your energy up. Here are your options- glue, raw rabit meat, and expired milk. Choose one: "

def eat(food):
	if food == glue
        print "The glue's clogging your lungs! You cant breath! Drink some water NOW!..."
    if food == raw rabit meat 
        print "It's full of bacteria, you are gonna get sick. Here's some medicine..."
    if food == expired milk
        print "You've thrown up from the rotten milk, here take the medicine on the table at your right..."
 


main()



