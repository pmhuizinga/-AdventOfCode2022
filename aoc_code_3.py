from general_functions import read_data
import string
import numpy as np

day = 3
data = read_data(day, test=False)

letter = list(string.ascii_lowercase)+list(string.ascii_uppercase)
prio = np.arange(1, len(letter)+1)
d = dict(zip(letter, prio))
nr = 0

for item in data:
    lenght = int(len(item))
    first_part = item[0:int(lenght/2)]
    second_part = item[int(lenght/2):lenght]
    matching_char = list(set(first_part).intersection(second_part))
    nr += d[matching_char[0]]

# day 3 A
print(nr)


chunks = [data[x:x+3] for x in range(0, len(data), 3)]

nr = 0
for chunk in chunks:
    matching_char = list(set(chunk[0]).intersection(chunk[1]).intersection(chunk[2]))
    nr += d[matching_char[0]]

print(nr)