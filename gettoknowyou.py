import math
def mul(x, y):
	return x * y

def output(name, x, y, z, happy): 
	out = """

Hey {}!
Did you know if your lucky number were the lenth of a rectangle and your unlucky number the width to find the volume of a rectangular prism would be to do:
4 * ({} * {}) = {}
I think you're cool, {}
{} make me happy too!
""".format(name, x, y, z, happy)
	return out

def main():

	name = raw_input("What's your name?: ")
	x = raw_input("Type your lucky number: ")
	y= raw_input("Type your unlucky number: ")
	happy= raw_input("What makes you happy?: ")

	z = int(x) / int(y)

	out = output(name, x, y, z, happy)
	print out

main()



