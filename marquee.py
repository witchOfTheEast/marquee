#!/usr/bin/python

# Create vertical scrolling marquee (cli)
from data.lexicon import codex
from data.lexicon import lex 
from getInput import get_input

user_input = get_input("\nEnter your message: ")

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

msg3 = Msg(user_input)
msg3.make_msg_by_codex()
msg3.print_msg()
