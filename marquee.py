#!/usr/bin/python

# Create vertical scrolling marquee (cli)

codex = {
    1: '----',
    2: '0---',
    3: '-0--',
    4: '--0-',
    5: '---0',
    6: '00--',
    7: '-00-',
    8: '--00',
    9: '000-',
    10: '-000',
    11: '0000',
    12: '0-0-',
    13: '-0-0',
    14: '0--0',
    15: '-00-',
    16: '0-00',
    17: '00-0'
    }

lex = {'a': (1,15,14,11,14,14,1), 
    'b': (1,9,14,9,14,9,1),
    'c': (1,10,2,2,2,10,1),
    'd': (1,6,12,14,12,6,1),
    'e': (1,11,2,11,2,11,1),
    'f': (1,11,2,11,2,2,1),
    'g': (1,10,2,14,14,10,1),
    'h': (1,14,14,11,14,14,1),
    'i': (1,11,15,15,15,11,1),
    'j': (1,5,5,5,14,15,1),
    'k': (1,14,12,6,12,14,1),
    'l': (1,2,2,2,2,11,1),
    'm': (1,14,17,11,14,14,1),
    'n': (1,14,17,16,14,14,1),
    'o': (1,7,14,14,14,7,1),
    'p': (1,9,14,9,2,2,1),
    'q': (1,7,14,14,16,10,1),
    'r': (1,9,14,9,12,14,1),
    's': (1,11,2,15,5,11,1),
    't': (1,11,15,15,15,15,1),
    'u': (1,14,14,14,14,15,1),
    'v': (1,14,14,14,15,4,1),
    'w': (1,14,14,11,17,14,1),
    'x': (1,14,14,7,14,14,1),
    'y': (1,14,14,14,7,7,1),
    'z': (1,11,5,15,2,11,1),
    ' ': (1,1,1,1,1,1,1)
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
        self.allLines = []
        self.msg_length = 0
        for i in range(len(args)):
            for j in range(len(args[i])):
                temp = Char(args[i][j])
                self.char_set.append(temp)
                self.msg_length += 1
        #make_msg() 

    def make_msg_by_codex(self):
            i = 0
            while i < 7:
                line = ''
                for value in range(self.msg_length):
                    letter = self.char_set[value].char
                    codex_index = lex[letter][i]
                    line_item = codex[codex_index]
                    line += '-' + line_item
                line += '-'
                self.allLines.append(line)
                i += 1 

    def make_msg():
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
        i = 0
        while i < 7:
            print self.allLines[i]
            i += 1

msg3 = Msg('w m')
msg3.make_msg_by_codex()
msg3.print_msg()
