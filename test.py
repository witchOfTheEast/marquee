from getopt import getopt
from sys import argv

def usage():
    print """FORGOT TO ADD USAGE"""

def main():
    try:
        opts, args = getopt(argv[1:], 'hi:', ['help', 'input='])
    except GetoptError as err:
        # print help info and exit:
        print(err)
        usage()
        exit(2)

    input = None

    for option, value in opts:
        if option in ('-h', '--help'):
            print 'option totally was: ', option
            usage()
            exit()

        elif option in ('-i', '--input'):
            input = value
            print 'value of %s totally was: ' % option, value

        else:
            assert False, 'unhandled option'

if __name__ == '__main__':
    main()
