# The world has been taken over by zombies.The computer will ask where you are and how many zombies are about to attack you.
#Then the computer will respond and tell you to hide and use your gun to protect youself. You have 5 choices of bullets for it. 
#The computer asks what type of bullet you'd like to shoot with.
#You will have to choose and type in the bullet you want for your gun, each bullet has a different fatality rate caused upon the enemy. 
# The computer will respond according to what type of bullet you choose.
# After you choose your bullet and see the outcome of it, you will be asked to choose what to eat so your energy is sustained. Each food also has a different effect upon you. You're then moved to a buliding and are asked about where you want to hide. Depending on what you choose there will be a different outcome on how safe you are from the zombies. Finally, you're asked to choose your final destination. It determines whether you win or lose this game. If you choose to go to the airport you win, if not you stay and get eaten by zombies. 
import math
import random

def main():
    place = raw_input( "Where are you right now?: ")
    amountofzombies = int(raw_input( "About how many zombies are about to attack you?: "))
    output = """
You're at {} !? 
You gotta find a place to hide or you'll get eaten! 
{} zombies? 
that's not good... 
USE YOUR GUN
""".format(place, amountofzombies)
    print output
main()

zombiecure = raw_input("Do you have the cure for turning into a zombie?: ")

def have(zombiecure):
    if zombiecure == "yes":
        print "Good. Use it when needed"
have(zombiecure)

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
shoot(bullet)

def chosen(bullet):
    if bullet == "marshmallow":
	    print "YOU HAVE BEEN EATEN, You are gonna turn into a zombie. Use the zombie cure if you have it. If not find one quickly!"
    elif bullet == "bouncyball":
	    print "You've been bitten."
    elif bullet == "paintball":
	    print "They are grabbing onto you."
    elif bullet == "wood":
	    print "Keep shooting at them, you will get away."
    elif bullet == "titanium":
	    print "You got away!"
    elif bullet == "diamond":
	    print "YOU KILLED THEM!"
chosen(bullet)

food = raw_input("You need some food to eat so you keep your energy up. Here are your options- glue, raw rabit meat, and expired milk. Choose one: ")

def eat(food):
    if food == "glue":
        print "The glue's clogging your lungs! You cant breath! Drink some water NOW!..."
    elif food == "raw rabit meat":
        print "It's full of bacteria, you are gonna get sick. Here's some medicine..."
    elif food == "expired milk":
        print "You've thrown up from the rotten milk, here take the medicine on the table at your right... "
eat(food)

water = raw_input("Are you going to drink some water before you leave? yes or no:")

def drink(water):
    if water == "yes":
        print "GOOD you're hydrated!"
    else:
        print "BAD CHOICE. You have a higher chance of dying."
drink(water)

hide = raw_input("You're at a building now. You've got to find a place to hide now before the zombies find you. Where are you going to hide?- under the table, behind the wall, or in the closet: ")

def spot(hide):
    if hide == "under the table":
        print "You have a high chance of getting caught but you'll survive."
    elif hide == "behind the wall":
        print "You're going to be found by the zombies. RUN as fast as you can."
    else:
        print "They won't find you there! :D "
spot(hide)

leave = raw_input("Did you leave after all the zombies passed?: ")

def building(leave):
    if leave == "yes":
        print "You're completely safe!"
building(leave)

transport = raw_input("How will you get to your next destination?: ")

def find(transport):
    if transport == "car":
        print "Okay you're in the car! Drive fast!"
    else:
        print "That's a bad idea but you'll make it as long as you move fast." 
find(transport)

safety = raw_input("Choose your final destination, this determines whether you live or die. Your options are to go to the- airport or anywhere that isnt the airport: ")

def travel(safety):
    if safety == "airport":
        print "Good choice. From there you can take a plane to another place and get away from the zombies.CONGRATULATIONS YOU WIN" 
    else:
        print "Since you've chosen to stay in the place taken over by zombies, you are going to die. Sorry can't help you anymore.YOU LOSE" 
travel(safety)


 






