from general_functions import read_data

"""
paper > rock
rock > scissors
scissors > paper
"""
day = 2
data = read_data(day, test=False)
data_original = [x.split(' ') for x in data]
map = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
ranking = {'rock': 1, 'paper': 2, 'scissors': 3}

data = [(map[x[0]], map[x[1]]) for x in data_original]


def calc_score(data):
    score = 0
    for pair in data:

        # score for option choice
        score += ranking[pair[1]]

        # draw
        if pair[0] == pair[1]:
            score += 3

        # win
        if pair[1] == 'rock' and pair[0] == 'scissors':
            score += 6
        elif pair[1] == 'paper' and pair[0] == 'rock':
            score += 6
        elif pair[1] == 'scissors' and pair[0] == 'paper':
            score += 6

    return score

# day2 A
print(calc_score(data))

maps = {'X': 'lose', 'Y': 'draw'}
maps2 = {'rock': {'win': 'paper', 'draw': 'rock', 'lose': 'scissors'},
         'paper': {'win': 'scissors', 'draw': 'paper', 'lose': 'rock'},
         'scissors': {'win': 'rock', 'draw': 'scissors', 'lose': 'paper'}}

data = list([list((map[x[0]], x[1])) for x in data_original])

for pair in data:
    if pair[1] == 'X':
        pair[1] = maps2[pair[0]]['lose']
    elif pair[1] == 'Y':
        pair[1] = (maps2[pair[0]]['draw'])
    elif pair[1] == 'Z':
        pair[1] = (maps2[pair[0]]['win'])
    # pair[1] = maps2[pair[0]['lose']]

print(calc_score(data))