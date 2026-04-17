import numpy as np
from collections import Counter

# 6x6 image block
image = np.array([
[52,55,61,66,70,61],
[63,59,55,90,109,85],
[62,59,68,113,144,104],
[63,58,71,122,154,106],
[67,61,68,104,126,88],
[68,65,70,106,122,90]
])
# Flatten image
data = image.flatten().tolist()

# Initialize dictionary
dictionary = {tuple([i]): i for i in range(256)}
dict_size = 256

w = ()
result = []

for k in data:
    wk = w + (k,)
    if wk in dictionary:
        w = wk
    else:
        result.append(dictionary[w])
        dictionary[wk] = dict_size
        dict_size += 1
        w = (k,)

if w:
    result.append(dictionary[w])

print("LZW Encoded Output:")
print(result)