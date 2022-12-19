from general_functions import read_data
import numpy as np
import pandas as pd

day = 5
data = read_data(day, test=True)

# split stacks and procedure
stack = []
for idx, x in enumerate(data):
    if x == '':
        break
    stack.append(list(x))

nr_of_stacks = max(stack[-1])
stack = np.array([[x.replace("[", " ").replace("]", " ") for x in y] for y in stack])

# remove blanks
df = pd.DataFrame(stack)
nan_value = float("NaN")
df.replace(" ", nan_value, inplace=True)
df.dropna(how='all', axis=1, inplace=True)
df = df[:-1] # remove bottom row
df.columns = np.arange(1, df.shape[1]+1) # rename columns

procedure = []
for idx2, x in enumerate(data):
    if idx2 >= idx + 1:
        procedure.append(x)

def proces(step):
    input = step.split(" ")
    nr_of_item = input[1]
    source = input[3]
    target = input[5]
    print(f'source: {source}, target: {target}, item: {nr_of_item}')

for step in procedure:
    proces(step)