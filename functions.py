def add(a,b): #compute the sum of a and b
	return a + b
 print add(3, 4)

def sub(a,b): #compute the difference of a and b
	return a - b
print sub(5, 3)

def mul(a,b): #compute the product of a and b
	return a * b
print(4, 4)

def div(a,b): #compute the quotient of a and b
	return a / b
print div(2, 3)

def hours_from_seconds(seconds): #convert seconds into hours 
	return seconds/3600
print hours_from_seconds(86400)

def circle_area(radius): #finds the area of a circle
 	return math.pi(radius)**2
print circle_area (5)

def sphere_volume(radius): #finds the volume of a sphere
	return 4/3 * math.pi(radius)**3
print sphere_volume(5)

def avg_volume(a,b): #computes the average volume of two spheres
	float(a)
	float(b)
	average = ((4/3 * math.pi(a)**3)+(4/3 * math.pi(b)**3))/2
	return float(average)
print avg_volume(10, 20)

def area(a, b, c): #finds the area of a triangle using the lenth of three sides
	p =(a+b+c)/2
	return (p*(p-a)*(p-b)*(p-c))**0.5
print area(1, 2, 2.5)

def right_allign(word):# defines a function that takes a string as an argument and returns that word with additional spaces so that it is perfectly right aligned on the screen
	return (80 - len(word))*(" ")+word
print right_allign("Hello")

def center(word):#defines a function that takes a string as an argument and returns that word with additional spaces so that it is perfectly centered on the screen.
	return (40 - len(word))*(" ")+word
print center("Hello")

def msg_box(word): #Define a function that takes a string as an argument and returns a message box
	return "+" + ((len(word)+4)*"-")+"+"+"\n"+"|"+(2*"")+(word)+(2*"")+"|"+"\n"+"+"+((len(word)+4)*"-")+"+"
#call all functions again
print msg_box("Hello")
print msg_box("I eat cats!)



