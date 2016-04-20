def count_up(n):
    if n >= 10:
        print "Blastoff!"
    else:
        print n
        countup(n+1)

def main():
    countup(1)
    return
main()


