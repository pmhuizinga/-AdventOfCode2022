from general_functions import read_data

day = 4
data = read_data(day, test=False)
data = [x.split(',') for x in data]
d = [[[int(z) for z in x.split("-")] for x in y] for y in data]

counter = 0

for x in d:

    max_val = max(x[0][0], x[1][0])
    min_val = min(x[0][1], x[1][1])

    a = [min(min_val, max_val), max(min_val, max_val)]
    if x[0] == a or x[1] == a:
        counter += 1

# day 4 A
print(counter)

counter = 0
for x in d:
    a = range(int(x[0][0]), int(x[0][1])+1)
    b = range(int(x[1][0]), int(x[1][1])+1)
    if set(a).intersection(b):
        counter += 1

# day 4 B
print(counter)