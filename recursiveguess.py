import random
def rounds(numberrounds, correct):
    if numberrounds == 0:
        return "You got " + str(correct) + "rounds correct."
    else: 
        print "Starting round " + str(numberrounds)
        correct += guess(random.randint(1, 100), 5)
        return rounds(numberrounds - 1, correct)
def guess(random, attempt):
    inp = int(raw_input("Guess a number: "))
    if inp == random:
        print "That's correct!"
        return 1
    elif attempts == 1:
        print "The answer was " + str(random) + "You aren't that good at this game." 
        return 0
    elif inp > random:
        print "That's too high."
        return guess(random, attempt -1)
    elif inp < random:
        print "That's too low."
        return guess(random, attempt -1)
def main():
    res = rounds(1, 0)
    print res
main()
 

