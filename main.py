import numpy as np


####
# Init
vals = np.array([0,1,2,4,5,6])
D = np.zeros(5)  # dummy


####
# Aux f'ns
def roll_them(D):
    return vals[np.random.randint(0, 6, len(D))]


####
# Policy f'ns
def policy(D,kind=None):
    '''
    Return the indices of dice to take.
    :param D: sorted int list of dice
    :param kind: string policy kind
    :return: int list of dice indexes to take
    '''
    global force_taketwo

    # forced takes
    if len(D) == 1:
        return [0]
    if force_taketwo:
        force_taketwo = False
        return [0,1]

    if kind is None:
        exit('Error: please select a policy kind.')
    elif kind == 'take_none':
        return []
    elif kind == 'take_one':
        return [0]
    elif kind == 'take_two':
        return [0,1]
    else:
        exit('Error: invalid policy kind.')


####
# Main
score = 0
force_taketwo = False
while len(D) > 0:
    # roll
    print('Roll---------------')
    D = roll_them(D)
    D = np.sort(D)
    print(D)
    # decide which dice to keep
    keeping = policy(D,kind='take_none')
    if len(keeping) > 0:
        print('Keeping: %s' % D[keeping])
        # update score
        score += np.sum(D[keeping])
        # update D
        D = np.delete(D,keeping)
        print('Score: %i' % score)
    else:
        force_taketwo = True

print('-------------------')
print('FINAL SCORE: %i' % score)
