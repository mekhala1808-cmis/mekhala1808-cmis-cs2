def add(x, y):
	return x + y
def output(name, x, y, z): 
	out = """
def main():
name = raw input("What's your name?: ")
x = raw_input("Type your lucky number: ")
y= raw_input("Type your lucky number: ")
happy= raw_input(What makes you happy?: ")

z = int(x) + int(y)

out = output(name)
output = """
Hey {}!
Did you know:
{} + {} = {}
I think you're cool, {}

""".format(name, x, y, z, name)
	return output
