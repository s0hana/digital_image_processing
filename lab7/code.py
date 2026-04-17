import cv2
import numpy as np
from collections import Counter
import heapq

img = cv2.imread(r"D:\3-2\Digital Image Processing\LAB\lab7\img.png", 0) 
data = np.array(img)

def lzw_encode(data):
    data_lst = data.flatten().tolist()

    dictionary = {tuple([i]): i for i in range(256)}
    dict_size = 256

    w = ()
    result = []

    for i in data_lst:
        wk = w + (i,)
        if wk in dictionary:
            w = wk
        else:
            result.append(dictionary[w])
            dictionary[wk] = dict_size
            dict_size += 1
            w = (i,)

    if w:
        result.append(dictionary[w])

    return result


def lzw_decode(compressed):
    dictionary = {i: (i,) for i in range(256)}
    dict_size = 256

    w = (compressed[0],)
    result = list(w)

    for k in compressed[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + (w[0],)
        else:
            raise ValueError("Bad compressed k")

        result.extend(entry)
        dictionary[dict_size] = w + (entry[0],)
        dict_size += 1
        w = entry

    return result

def huffman_encode(data):
    freq = Counter(data)

    heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huff_dict = dict(heapq.heappop(heap)[1:])
    encoded = ''.join(huff_dict[i] for i in data)

    return encoded, huff_dict

def huffman_decode(encoded, huff_dict):
    reverse_dict = {v: k for k, v in huff_dict.items()}

    decoded = []
    temp = ""

    for bit in encoded:
        temp += bit
        if temp in reverse_dict:
            decoded.append(reverse_dict[temp])
            temp = ""

    return decoded

lzw_encoded = lzw_encode(data)
huff_encoded, huff_dict = huffman_encode(lzw_encoded)

with open(r"D:\3-2\Digital Image Processing\LAB\lab7\encoded.txt", "w") as f:
    f.write(huff_encoded)

with open(r"D:\3-2\Digital Image Processing\LAB\lab7\dict.txt", "w") as f:
    for k, v in huff_dict.items():
        f.write(f"{k}:{v}\n")

with open(r"D:\3-2\Digital Image Processing\LAB\lab7\shape.txt", "w") as f:
    f.write(f"{data.shape[0]} {data.shape[1]}")

print("Compression Done!")

with open(r"D:\3-2\Digital Image Processing\LAB\lab7\encoded.txt", "r") as f:
    encoded_data = f.read()

huff_dict_loaded = {}
with open(r"D:\3-2\Digital Image Processing\LAB\lab7\dict.txt", "r") as f:
    for line in f:
        k, v = line.strip().split(":")
        huff_dict_loaded[int(k)] = v

with open(r"D:\3-2\Digital Image Processing\LAB\lab7\shape.txt", "r") as f:
    h, w = map(int, f.read().split())

decoded_lzw = huffman_decode(encoded_data, huff_dict_loaded)
original_flat = lzw_decode(decoded_lzw)

recovered_image = np.array(original_flat).reshape((h, w)).astype(np.uint8)

cv2.imwrite(r"D:\3-2\Digital Image Processing\LAB\lab7\output.png", recovered_image)

print("Decompression Done! output.png saved")