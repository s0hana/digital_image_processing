import cv2
import numpy as np
import matplotlib.pyplot as plt
img_1 = cv2.imread(r"D:\3-2\Digital Image Processing\LAB\lab3\img1.jpg", 0)
r_k = [0 for i in range(256)]
n = img_1.shape[0]
m = img_1.shape[1]
for i in range(n):
    for j in range(m):
        r_k[img_1[i][j]]+=1
p_r = []
for i in r_k:
    _s = i/(m*n)
    p_r.append(_s)

plt.subplot(2, 2, 1)
plt.bar(range(256), p_r, align="center")
plt.title("Original")

cdf = [0 for i in range(256)]
cdf[0] = p_r[0]
for i in range(1, len(p_r)):
    cdf[i] = cdf[i-1]+p_r[i]
t_r = []
for i in cdf:
    t_r.append(int(255*i))

new_img = img_1.copy()
for i in range(n):
    for j in range(m):
        new_img[i][j] = t_r[img_1[i][j]]

cv2.imshow("Original", img_1)
cv2.imshow("After Transformation", new_img)

r_k1 = [0 for i in range(256)]
for i in range(n):
    for j in range(m):
        r_k1[new_img[i][j]]+=1
p_s = []
for i in r_k1:
    _s = i/(m*n)
    p_s.append(_s)
plt.subplot(2, 2, 2)
plt.bar(range(256), p_s, align="center")
plt.title("After transformation")
plt.show()
cv2.waitKey(0)