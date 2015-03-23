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
    ----""")
    }

class Char(object):
    def __init__(self, char):
        self.char = char

    def disp_char(self):
        print lex[self.char]
        #for line in lex[self.char]
        #    print line

class Msg(object):
    def __init__(self, *args):
        self.char_set = []
        for i in range(len(args)):
            temp = Char(args[i])
            self.char_set.append(temp)

    def print_msg(self):
        for i in range(len(self.char_set)):
            self.char_set[i].disp_char()
msg1 = Msg('a', 'b', 'c')
msg1.print_msg()

char1 = Char('a')
char2 = Char('b')
char3 = Char('c')
print 'char is ', type(char1)
#char1.disp_char()
