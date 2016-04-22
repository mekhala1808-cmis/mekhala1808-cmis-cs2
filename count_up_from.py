def count_up_from(start, stop):
    if start > stop:
        print "Blastoff"
    else:
        print start
        count_up_from(start + 1, stop)


def main():
    count_up_from(5, 10)
    return
main()
