import sys
import re
import json


# https://pysimpleautomata.readthedocs.io/en/latest/tutorial.html

class Node:
    def __init__(self, label, start, transistions):
        self.label = label
        self.start = start
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


def regex_to_nodes(regex):
    nodes = []
    current_operation = []
    for char in regexArray:
        if char == "(":
            current_operation = [
                x for x in regexArray if x != ")" and x != "("]

        # elif char == "1":
        # elif char == "0":
        #     print(hi)

        # elif char == ")":
        # elif char == "+":
    print(current_operation)


# def nodes_to_NFA(nodes):

# regex_to_nodes(list(sys.argv[1]))

st = sys.argv[1]
a = st[st.find("(")+1:st.rfind(")")]
while a.__contains__("("):
    print(a)
    a = a[a.find("(")+1:a.rfind(")")]
