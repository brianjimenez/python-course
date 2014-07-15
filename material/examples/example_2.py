import sys


def usage():
    print 'usage: %s message' % sys.argv[0]


def say(message):
    """Says something"""
    print message


if __name__ == "__main__":
    if len(sys.argv[1:]) != 1:
        usage()
        raise SystemExit('Wrong command line')
    say(sys.argv[1])
