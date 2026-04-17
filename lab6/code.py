import cv2
import numpy as np
import matplotlib.pyplot as plt

def to_binary(img):
    new_img = img.copy()
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            new_img[i][j] = 1 if img[i][j] > 150 else 0
    return new_img

def to_binary_color(img):
    new_img = img.copy()
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            new_img[i][j] = 255 if img[i][j] == 1 else 0
    return new_img

def erosion(a, b):
    dh, dw = b.shape
    h, w = a.shape
    img = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            flag = 0
            for k in range(dh):
                for l in range(dw):
                    u = i - dh // 2 + k
                    v = j - dw // 2 + l
                    if 0 <= u < h and 0 <= v < w:
                        if a[u][v] == 0 and b[k][l] == 1:
                            flag = 1
                            break

                    else:
                        flag = 1
                        break
            if flag == 0:
                img[i][j] = 1
    return img

def dilation(a, b):
    dh, dw = b.shape
    h, w = a.shape
    img = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            flag = 0
            for k in range(dh):
                for l in range(dw):
                    u = i - (-dh // 2 + k)
                    v = j - (-dw // 2 + l)
                    if 0 <= u < h and 0 <= v < w:
                        if a[u][v] == 1 and b[k][l] == 1:
                            flag = 1
            if flag == 1:
                img[i][j] = 1
    return img

# main
a = to_binary(cv2.imread(r"D:\3-2\Digital Image Processing\LAB\lab6\img.jpg", 0))
b = np.ones((3, 3), dtype=np.uint8)

e = erosion(a, b)
d = dilation(a, b)
opening = dilation(e, b)
closing = erosion(d, b)

images = [to_binary_color(a), to_binary_color(e), to_binary_color(d), to_binary_color(opening), to_binary_color(closing)]
titles = ["Original", "Erosion", "Dilation", "Opening", "Closing"]

plt.figure(figsize=(18, 6))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")
plt.show()