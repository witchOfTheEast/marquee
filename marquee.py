#!/usr/bin/python

# Create vertical scrolling marquee (cli)

lex = {'a': ("""
    ----
    -00-
    0--0
    0000
    0--0
    0--0
    ----"""), 
    'b': ("""
    ----
    000-
    0--0
    000-
    0--0
    000-
    ----"""),
    'c': ("""
    ----
    -000
    0---
    0---
    0---
    -000
    ----"""),
    '1': ("""
    1111
    2222
    3333
    4444
    5555
    6666
    7777
    """)
    }

class Char(object):
    def __init__(self, char):
        self.char = char

    def disp_char(self):
        #print lex[self.char]
        print 'Printing char\n'
        char_pr = lex[self.char]
        print len(char_pr)
        print char_pr[4:9]
        print lex[self.char][4:9]
        #for line in lex[self.char]
        #    print line

    def get_char_line(self, x, y):
        """Take the string index range and return the 'line'"""
        return lex[self.char][x:y]

class Msg(object):
    def __init__(self, *args):
        self.char_set = []
        self.msg_length = len(args)
        for i in range(len(args)):
            temp = Char(args[i])
            self.char_set.append(temp)

        # allLines should be a list of 7, each item containing all the x lines of each letter
        self.allLines = []
        i = 0
        x = 5
        y = 9

        while i < 7:
            line = '' 
            for value in range(self.msg_length):
                item = self.char_set[value].get_char_line(x, y)
                line += '-' + item 
            self.allLines.append(line)
            i += 1
            x += 9
            y += 9
        
    def print_msg(self):
        for i in range(7):
            print self.allLines[i] + '-'

msg1 = Msg('a', 'b', 'c')
msg1.print_msg()
msg2 = Msg('abc')
