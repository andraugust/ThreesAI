import numpy as np

ndie = 5

class Game:

    def __init__(self):
        self.state = np.zeros(ndie)
        self.roll()

    def step(self,action):
        # remove taken dice
        self.remove_die(action)
        if len(self.state)==0: return [-1]
        # roll
        self.roll()
        return self.state

    def remove_die(self,idxs):
        self.state = np.delete(self.state,idxs)

    def roll(self):
        self.state = np.random.randint(1,6,len(self.state))


class Agent:

    def __init__(self):
        self.first_roll = True

    def get_action(self,gstate):
        take_idxs = np.argmin(gstate)
        return take_idxs