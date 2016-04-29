def smallest(lastnumber):
    number = raw_input("Next number: ")
    if number == "":
        return lastnumber
    elif lastnumber > float(number):
        lastnumber = float(number)
        return smallest(lastnumber)
    else:
        return smallest(lastnumber)


def main():
    out = smallest(float('Inf'))
    print "The smallest number is " + str(out)
main()
