def add(x,y)
	return x+y

def output(name, x, y, z): 
	out = """
Hey {}!
Did you know:
{} + {} = {}
""".format(name, x, y, z)
	return output

def main():
#Input Section
name = raw_input("What's your name?: ")
x = raw_input("Type a number: ")
y= raw_input("Type another: ")
happy = raw_input("What make you happy?: ")

#Processing Section
z = int(x) + int(y)

#Output Section
out = output(name
output = """
Hey {}!
Did you know:
{} + {} = {}
I think you're cool, {}
{} also make me happy 
""".format(name, x, y, z, name, happy)
print output

main()
