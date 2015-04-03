#!/usr/bin/python

def get_input(prompt=None):

    if prompt != None:

        user_input = raw_input(prompt)

    else:
        user_input = raw_input('>')

    return user_input
