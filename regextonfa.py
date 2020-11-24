import sys
import re

class Node:
    def __init__(self, string, label, transistions):
        self.string = string
        self.transistions = transistions

class NFA:
    def __init__(self, start, accept, alphabet, nodes):
        self.start = start
        self.accept = accept
        self.alphabet = alphabet
        self.node = node


def print_NFA(regex):
    if len(sys.argv) != 2 or sys.argv is None or type(sys.argv[1]) != str:
        print("An error occured, please enter a string regex expression")
    else:
        
        regexArr = list(re.sub(r'\s+', '', sys.argv[1]))
        print(regexArr)

# print_NFA(sys.argv[1])


def regex_to_NFA(regexArray):
    nodes = []
    for char in regexArray:
        if char == "1":
            
        elif char == "0":
            print(hi)
        elif char == "(":
        elif char == ")":
        elif char == "+":



#Return a list of tuples were the first element is a node and the second element is an array of its transitions
#ex) [(A, [0A, 1B]), (B, [0C, 1D])]

    


    



