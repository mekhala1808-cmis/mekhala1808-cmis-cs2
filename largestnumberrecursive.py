#LARGEST NUMBER STUFF
def largest(lastnumber):
    number = raw_input("Next number: ")
    if number == "":
        return lastnumber
    elif lastnumber < float(number):
        lastnumber = float(number)
        return largest(lastnumber)
    else:
        return largest(lastnumber)


def main():
    out = largest(-float('Inf'))
    print "The largest number is " + str(out)
main()


