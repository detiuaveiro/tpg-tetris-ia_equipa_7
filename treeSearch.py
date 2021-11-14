import math

#Search Node
class Node:
    #Constructor
    def __init__(self, state, parent, cost):
        self.state = state
        self.parent = parent
        self.cost = cost
    def __str__(self):
        return "no(" + str(self.state) + "," + str(self.parent) + ")"
    def __repr__(self):
        return str(self) 