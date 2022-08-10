import time
import sys
import random

league_members = [] #input a list of your league members here
draft_order = []

def delay_print(s): #adds a print delay in the terminal
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

random.shuffle(league_members) # randomly shuffles the order of the league_members list

for team in reversed(league_members): # reverses the order of the shuffled list so it can count down in descending order
    draft_order = league_members.index(team) + 1 # adds 1 to the index value to avoid offset indexing in the terminal
    draft_order = str(draft_order) # converts the int value above to a printable string
    delay_print("Pick " + draft_order + " ... ") # Prints index value of draft_order
    time.sleep(2)
    print(team.title() +"\n") # prints team next to corresponding index value
    time.sleep(1)

delay_print("Enjoy the season, everyone!")