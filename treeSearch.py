
def actions(self, state):
    pass


# resultado de uma accao num estado, ou seja, o estado seguinte
def result(self, state, action):
    #(x,y) = state.piece
    #if action == "a":
       #state.piece=(x-1,y)
    #elif action == "d":
       #state.piece=(x,+1,y)
    #elif action == "w":
       #state.piece.translate()
    pass


# custo de uma accao num estado
def cost(self, state, action):

    pass


# custo estimado de chegar de um estado a outro
def heuristic(self, state, goal):
    pass


# test if the given "goal" is satisfied in "state"
def satisfies(self, state, goal):
    state==goal
    pass
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
