# New York City has been taken over by zombies and you have a gun and 5 choices of bullets for it.
#The computer will ask which type of bullet you'd like to shoot with.
#The player will have to choose and type the bullet they want for their gun, each bullet has a different fatality rate caused upon the enemy. 

import math
import random

def main():
    place = raw_input( "Where in NewYork City are you?: ")
    amountofzombies = raw_input( "About how many zombies are about to attack you?: ")
    output = """
You're in {} !? You gotta find a place to hide or you'll get eaten! {} zombies? that's not good... USE YOUR GUN
""".format(place, amountofzombies)
    print output
typeofbullet = raw_input( "Choose what bullet you want to use with your gun: ")
if bullet == marshmallow:
	print "YOU HAVE BEEN EATEN"
elif bullet== bouncyball:
	print "You've been bitten."
elif bullet == paintball:
	print "They are grabbing onto you."
elif bullet == wood:
	print "Keep shooting at them, you will get away."
elif bullet == titanium:
	print "You got away!"
elif bullet == diamond:
	print "YOU KILLED THEM!"

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



