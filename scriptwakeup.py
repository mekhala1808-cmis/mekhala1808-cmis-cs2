def wakeup():
    print "This program will ask you for 5 integer or float values." + "\n" + "It will calculate the average of all values from 0 inclusive to 10 exclusive." + "\n" + "It will print out whether the resulting average is even or odd."
   
def numbers():
    n1 = float(raw_input("n0: "))
    n2 = float(raw_input("n1: "))
    n3 = float(raw_input("n2: "))
    n4 = float(raw_input("n3: "))
    n5 = float(raw_input("n4: "))
numbers ()

def main():
    if n1 < 0 or n1 >= 10:
        print str(n1)+(" is out of range")
    if n2 < 0 or n1 >= 10:
        print str(n2)+(" is out of range")
    if n3 < 0 or n1 >= 10:
        print str(n3)+(" is out of range")
    if n4 < 0 or n1 >= 10:
        print str(n4)+(" is out of range")
    if n5 < 0 or n1 >= 10:
        print str(n5)+(" is out of range")
main ()


def avgvalue():
    avgvalue = int(n1) + int(n2) + int(n3) + int(n4) + int(n5) / 5
avgvalue()

def evenodd():
	greatestnumber == bool(str(greatestnumber))

def result(avgvalue, intpart, evenodd):
	result + """
The average is {}
The intger part of the average is {}.
THe integer part is {}.
""".format(avgvalue, intpart, evenodd)
	return result
	
	

