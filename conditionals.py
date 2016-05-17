# The world has been taken over by zombies.The computer will ask where you are and how many zombies are about to attack you.
#Then the computer will respond and tell you to hide and use your gun to protect youself. You have 5 choices of bullets for it. 
#The computer will then ask if you have the zombie cure, you respond with either yes or no. 
#If you have the cure the computer will tell you to use it when needed. If not it will continue on to the next question. 
#The computer asks what type of bullet you'd like to shoot with.
#You will have to choose and type in the bullet you want for your gun, each bullet has a different fatality rate caused upon the enemy. 
# The computer will respond according to what type of bullet you choose.
# After you choose your bullet and see the outcome of it, you will be asked to choose what to eat so your energy is sustained. Each food also has a different effect upon you. 
#Next you're asked whether you are going to drink water before you leave. If you respong with yes, the computer will respong saying that's good. If you type in no, the computer will print out saying that it was a bad choice. 
#You're then moved to a buliding and are asked about where you want to hide. Depending on what you choose there will be a different outcome on how safe you are from the zombies. 
#Next, the computer will ask you if you've left your hiding spot after all the zombies have passed by. If you say yes, you're completely safe. If you say no the computer will move on to the next question.
#The computer then asks how you will get to your final destination. If you type in car, the computer will respond by saying that's good. If you say any other form of transportation, the computer will say it's a bad idea but you'll still be safe either way. 
#Finally, you're asked to choose your final destination. It determines whether you win or lose this game. If you choose to go to the airport you win, if not you stay and get eaten by zombies. 
import math
import random





def zombies(numberofzombies):
    if numberofzombies == 5:
        return True
    else:
        return False

def numberofzombies(amountofzombies):
    if amountofzombies > 100 and amountofzombies <= 1000: 
        return 5
    else:
        return 9


def number(amountofzombies):
    if zombies(numberofzombies(amountofzombies)): 
        print "There are too many zombies! Here's a forcefield that will prtoect you from them until you find safety." 
    elif not amountofzombies > 100:
        print "You will get away safely. Dont worry."
    elif amountofzombies == 0:
        print "You're super safe and lucky!"
    elif amountofzombies < 1000:
        print "You had no chance of surviving, so I teleported you to a safer place."




def have(zombiecure):
    if zombiecure == "yes" or "I have it":
        print "Good. Use it when needed"



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




def eat(food):
    if food == "glue":
        print "The glue's clogging your lungs! You cant breath! Drink some water NOW!..."
    elif food == "raw rabit meat":
        print "It's full of bacteria, you are gonna get sick. Here's some medicine..."
    elif food == "expired milk":
        print "You've thrown up from the rotten milk, here take the medicine on the table at your right... "




def liquid(hydrate):
    print hydrate
def drink(water):
    if water == "yes":
        return "GOOD you're hydrated!"
    else:
        return "BAD CHOICE. You have a higher chance of dying."




def spot(hide):
    if hide == "under the table":
        print "You have a high chance of getting caught but you'll survive."
    elif hide == "behind the wall":
        print "You're going to be found by the zombies. RUN as fast as you can."
    else:
        print "They won't find you there! :D "




def building(leave):
    if leave == "yes":
        print "You're completely safe!"




def find(transport):
    if transport == "car":
        print "Okay you're in the car! Drive fast!"
    else:
        print "That's a bad idea but you'll make it as long as you move fast." 




def travel(safety):
    if safety == "airport":
        print "Good choice. From there you can take a plane to another place and get away from the zombies.CONGRATULATIONS YOU WIN" 
    else:
        print "Since you've chosen to stay in the place taken over by zombies, you are going to die. Sorry can't help you anymore.YOU LOSE" 


def main():
    place = raw_input( "Where are you right now?: ")
    output = """
You're at {} !? 
You gotta find a place to hide or you'll get eaten! 
Hopefully not too may zombies are around you. 
If you need to defend youself from them...
USE YOUR GUN
""".format(place)
    print output  
    amountofzombies = int(raw_input( "About how many zombies are about to attack you?: "))
    number(amountofzombies)
    zombiecure = raw_input("Do you have the cure for turning into a zombie?: ")
    have(zombiecure)
    bullet = raw_input( "Choose what bullet you want to use with your gun- marshmallow, bouncyball, paintball, wood, titanium, or diamond: ")
    shoot(bullet)
    chosen(bullet)
    food = raw_input("You need some food to eat so you keep your energy up. Here are your options- glue, raw rabit meat, and expired milk. Choose one: ")
    eat(food)
    water = raw_input("Are you going to drink some water before you leave? yes or no:")
    liquid(drink(water))
    hide = raw_input("You're at a building now. You've got to find a place to hide now before the zombies find you. Where are you going to hide?- under the table, behind the wall, or in the closet: ")
    spot(hide)
    leave = raw_input("Did you leave after all the zombies passed?: ")
    building(leave)
    transport = raw_input("How will you get to your next destination?: ")
    find(transport)
    safety = raw_input("Choose your final destination, this determines whether you live or die. Your options are to go to the- airport or anywhere that isnt the airport: ")
    travel(safety)  
main()
 






