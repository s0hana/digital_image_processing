import cv2
import numpy as np
import matplotlib.pyplot as plt

img_1 = cv2.imread(r"D:\3-2\Digital Image Processing\LAB\lab3\img2.jpg", 0)
img_ref = cv2.imread(r"D:\3-2\Digital Image Processing\LAB\lab3\img3.jpg", 0)
n1 = img_1.shape[0]
m1 = img_1.shape[1]
nr = img_ref.shape[0]
mr = img_ref.shape[1]

r_k1 = [0 for i in range(256)]
for i in range(n1):
    for j in range(m1):
        r_k1[img_1[i][j]]+=1

p_r1 = []
for i in r_k1:
    a = i/(m1*n1)
    p_r1.append(a)

cdf1 = [0 for i in range(256)]
cdf1[0] = p_r1[0]
for i in range(1, len(cdf1)):
    cdf1[i] = cdf1[i-1]+p_r1[i]

r_k_ref = [0 for i in range(256)]
for i in range(nr):
    for j in range(mr):
        r_k_ref[img_ref[i][j]]+=1

p_r_ref = []
for i in r_k_ref:
    a = i/(nr*mr)
    p_r_ref.append(a)

cdf2 = [0 for i in range(256)]
cdf2[0] = p_r_ref[0]
for i in range(1, len(cdf2)):
    cdf2[i] = cdf2[i-1]+p_r_ref[i]

m = [0 for i in range(256)]

for i in range(256):
    for j in range(256):
        if cdf1[i] >= cdf2[j]:
            m[i] = j
        else:
            break
img_out = img_1.copy()

for i in range(n1):
    for j in range(m1):
        img_out[i][j] = m[img_1[i][j]]

cv2.imshow("Original", img_1)
cv2.imshow("Reference", img_ref)
cv2.imshow("After transformation", img_out)

r_k_out = [0 for i in range(256)]
for i in range(n1):
    for j in range(m1):
        r_k_out[img_out[i][j]]+=1

p_r_out = []
for i in r_k_out:
    a = i/(mr*nr)
    p_r_out.append(a)

cdf3 = [0 for i in range(256)]
cdf3[0] = p_r_out[0]
for i in range(1, len(cdf3)):
    cdf3[i] = cdf3[i-1]+p_r_out[i]


plt.subplot(1, 3, 1)
plt.bar(range(256), cdf1, align="center")
plt.title("Original")

plt.subplot(1, 3, 2)
plt.bar(range(256), cdf2, align="center")
plt.title("Reference")

plt.subplot(1, 3, 3)
plt.bar(range(256), cdf3, align="center")
plt.title("Output")
plt.show()

cv2.waitKey(0)
