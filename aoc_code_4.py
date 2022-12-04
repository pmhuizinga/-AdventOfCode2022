from general_functions import read_data
import numpy as np

day = 4
data = read_data(day, test=True)
data = [x.split(',') for x in data]
# [['2-4', '6-8'], ['2-3', '4-5'], ['5-7', '7-9'], ['2-8', '3-7'], ['6-6', '4-6'], ['2-6', '4-8']]
[[[int(z) for z in x.split("-")] for x in y] for y in data]
# [[[2, 4], [6, 8]], [[2, 3], [4, 5]], [[5, 7], [7, 9]], [[2, 8], [3, 7]], [[6, 6], [4, 6]], [[2, 6], [4, 8]]]

# [int(x) for x in a.split("-")]