def add(a, b): #compute the sum of a and b
	return a + b
a1=add(3, 4)
a2=add(9,10)

def sub(a, b): #compute the difference of a and b
	return a - b
b1=sub(5, 3)
b2=sub(7, 8)

def mul(a,b): #compute the product of a and b
	return a * b
c1=(4, 4)
c2=(5, 9)

def div(a,b): #compute the quotient of a and b
	return a / b
d1=div(2, 3)
d2=div(6, 3)

def hours_from_seconds(seconds): #convert seconds into hours 
	return seconds/3600
f1=hours_from_seconds(86400)
f2=hours_from_seconds(25000)

import math

def circle_area(radius): #finds the area of a circle
 	return math.pi * (radius)**2
e1=circle_area(5)**2
e2=circle_area(8)**2

def sphere_volume(radius): #finds the volume of a sphere
    return 1.33333333333 * math.pi * (radius**3) 
g1=sphere_volume(5)**3
g2=sphere_volume(7)**3

def avg_volume(a,b): #computes the average volume of two spheres
    m= a/2
    n= b/2
    y= 1.3333333333333*math.pi*c*c*c
    z= 1.333333333333*math.pi*d*d*d
    return (y+z)/2
h1=avg_volume(10, 20)
h2=avg_volume(5, 15)

def area(a, b, c): #finds the area of a triangle using the lenth of three sides
	p =(a+b+c)/2
	return (p*(p-a)*(p-b)*(p-c))**0.5
i1=area(1, 2, 2.5)
i2=area(3, 4, 4.5)

def right_allign(word):# defines a function that takes a string as an argument and returns that word with additional spaces so that it is perfectly right aligned on the screen
	return (80 - len(word))*(" ")+word
j1=right_allign("Hi")
j2=right_allign("Hello")

def center(word):#defines a function that takes a string as an argument and returns that word with additional spaces so that it is perfectly centered on the screen.
	return (40 - len(word))*(" ")+word
k1=center("Hello")
k2=center("Hi")

def msg_box(word): #Define a function that takes a string as an argument and returns a message box
	return "+" + ((len(word)+4)*"-")+"+"+"\n"+"|"+(2*"")+(word)+(2*"")+"|"+"\n"+"+"+((len(word)+4)*"-")+"+"
#call all functions again
l1=msg_box("Hello")
l2=msg_box("I eat cats!")




