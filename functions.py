def add(a,b): #compute the sum of a and b
	return a + b

def sub(a,b): #compute the difference of a and b
	return a - b

def mul(a,b): #compute the product of a and b
	return a * b

def div(a,b): #compute the quotient of a and b
	return a / b

def hours_from_seconds(seconds): #convert seconds into hours 
	return seconds/3600

def circle_area(radius): #finds the area of a circle
 	return math.pi(radius)**2

def sphere_volume(radius): #finds the volume of a sphere
	return 4/3 * math.pi(radius)**3

def avg_volume(a,b): #computes the average volume of two spheres
	float(a)
	float(b)
	average = ((4/3 * math.pi(a)**3)+(4/3 * math.pi(b)**3))/2
	return float(average)

def area(a, b, c): #finds the area of a triangle using the lenth of three sides
	p =(a+b+c)/2
	return (p*(p-a)*(p-b)*(p-c))**0.5

def right_allign(word):# defines a function that takes a string as an argument and returns that word with additional spaces so that it is perfectly right aligned on the screen
	return (80 - len(word))*(" ") + word

def center(word):#defines a function that takes a string as an argument and returns that word with additional spaces so that it is perfectly centered on the screen.
	return (30 - len(word))*(" ") + word

def msg_box(word): #Define a function that takes a string as an argument and returns a message box
return 




