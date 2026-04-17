import numpy as np

data = np.array([
    [39, 39, 39, 126, 126, 126],
    [39, 39, 39, 126, 126, 126],
    [39, 39, 39, 126, 126, 126],
    [39, 39, 39, 126, 126, 126],
    [39, 39, 39, 126, 126, 126],
    [39, 39, 39, 126, 126, 126],
])

data_lst = []
for i in range(6):
    for j in range(6):
        data_lst.append(int(data[i][j]))

dictionary = {tuple([i]): i for i in range(256)}
dict_size = 256

w = ()
result = []

for i in data_lst:
    wk = w +(i,)
    if wk in dictionary:
        w = wk
    else:
        result.append(dictionary[w])
        dictionary[wk] = dict_size
        dict_size+=1
        w = (i,)
if w:
    result.append(dictionary[w])
print(result)