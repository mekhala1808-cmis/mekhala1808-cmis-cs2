def clapYourHands():
	    print "clap clap"
def stompYourFeet():
	    print "stomp stomp"
def main():
	    youreHappy=raw_input("Are you happy?") == "yes"
	    youKnowIt=raw_input("Do you know it?") == "yes"
	    
	    youreHappy = True
	    youKnowIt = True
	
	    if youreHappy and youKnowIt:
	        clapYourHands()
	        stompYourFeet()
	
	    print "Good bye"
main()
