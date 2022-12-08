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

for column in range(0, stack.shape[1], 1):
    print(stack[:, column])

df = pd.DataFrame(stack)

nan_value = float("NaN")
df.replace(" ", nan_value, inplace=True)
df.dropna(how='all', axis=1, inplace=True)


procedure = []
for idx2, x in enumerate(data):
    if idx2 > idx + 1:
        procedure.append(x)
