import math
import random

def main():
    minimumnumber = int(raw_input( "What is the minimum number?: "))
    maximumnumber = int(raw_input( "What is the maximum number?: "))
    targetnumber = random.randint(minimumnumber, maximumnumber)
    output = """
I'm thinking of a number from {} to {}
""".format(minimumnumber, maximumnumber)

    print output

    guessing = int(raw_input("What do you think it is?: "))
    if  targetnumber == guessing:
        print """
The target was {}.
Your guess was {}.
That's correct! You must be psychic!
""".format(targetnumber, guessing)

    elif targetnumber < guessing:
        difference = abs(guessing - targetnumber)
        print """
The target was {}.
Your guess was {}.
That's under by {}.
""".format(targetnumber, guessing, difference)

    elif targetnumber > guessing:
        difference = abs(targetnumber - guessing)
        print """
The target was {}.
Your guess was {}.
That's over by {}.
""".format(targetnumber, guessing, difference)

main()
