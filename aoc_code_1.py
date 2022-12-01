from general_functions import read_data

day = 1
data = read_data(day, test=False)

total_list = []
val = 0

for item in data:
    if item == '':
        total_list.append(val)
        val = 0
    else:
        val = val + int(item)

# day1 A
print(max(total_list))

# day1 B
total_list.sort(reverse=True)
print(sum(total_list[:3]))