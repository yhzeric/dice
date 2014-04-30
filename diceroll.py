#! /usr/bin/env python
import random
import specialinput.py
chances = int_input("how many dices do you want to roll?")
min = 1
max = int_input("how many sides should each dice have?")
while max <= min:
    print "the dice must have at least two sides"
    max = int_input("how many sides should each dice have?")
while chaces != 0:
    print "the result of the dice roll is", random.randint(min, max)
    chances -= 1

