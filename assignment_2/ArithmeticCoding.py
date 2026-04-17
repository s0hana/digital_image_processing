import numpy as np

data = np.array([
[52, 55, 61, 66, 70 ,61],
[63, 59, 55, 90, 109, 85],
[62, 59, 68, 113, 144, 104],
[63, 58, 71, 122, 154, 106],
[67, 61, 68, 104, 126, 88],
[68, 65, 70, 106, 122, 90]
])

data_lst = []
for i in range(6):
    for j in range(6):
        data_lst.append(int(data[i][j]))
total = len(data_lst)

count_dict = {}
for i in data_lst:
    count_dict[i] = count_dict.get(i, 0) + 1

probability_dict = {}
for i, j in count_dict.items():
    probability_dict[i] = j / total

interval_dict = {}
low = 0
for i in sorted(probability_dict):
    high = low + probability_dict[i]
    interval_dict[i] = (low, high)
    low = high

low = 0
high = 1

for i in data_lst:
    l, h = interval_dict[i]
    r = high - low
    high = low + r*h
    low = low + r*l

encoded_value = (low + high)/2
print(encoded_value)