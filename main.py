import numpy as np


vals = np.array([0,1,2,4,5,6])
dice = np.zeros(5)  # dummy


def policy(dice):
    return np.argmin(dice)


score = 0
while len(dice) > 0:
    # roll
    dice = vals[np.random.randint(0,6,len(dice))]
    print(dice)
    # keep dice
    keeping = policy(dice)
    score += dice[keeping]
    dice = np.delete(dice,keeping)
    print(keeping)
    print(score)



'''
while g.state.all() != -1:
    print(g.state)
    action = a.get_action(g.state)
    print(action)
    g.step(action)
'''