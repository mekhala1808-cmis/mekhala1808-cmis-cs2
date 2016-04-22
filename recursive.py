def adder(stuff, total):
    if stuff == "":
        return total
    else:
        total += float(stuff) 
        stuff = raw_input("Running total: " + str(total) + "\nNext number: ")
        return adder(stuff, total)

def main():
    out = adder(0, 0)
    print "The sum is " + str(out)
main()
    
