import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\3-2\Digital Image Processing\LAB\assignment_1\rose.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, w, ch = img.shape
red_rose = np.zeros((h, w), dtype=np.uint8)

for x in range(h):
    for y in range(w):
        r, g, b = img[x, y]
        if r>150 and g<100 and b<100:
            red_rose[x, y] = 255
        else:
            red_rose[x, y] = 0

karnel = 5
pad = karnel//2

padded_img = np.zeros((h + 2*pad, w + 2*pad, 3), dtype=int)
padded_img[pad: pad+h, pad:pad+w] = img

blur_img = np.zeros_like(img)
for x in range(h):
    for y in range(w):
        for c in range(3):
            r = padded_img[x:x+karnel, y:y+karnel, c]
            total = 0
            for i in range(karnel):
                for j in range(karnel):
                    total+=r[i, j]
            blur_img[x, y, c] = total // (karnel*karnel)
sharp_mask = np.zeros_like(img, dtype=int)
sharp = np.zeros_like(img, dtype=int)
for x in range(h):
    for y in range(w):
        for c in range(3):
            sharp_mask[x, y, c] = int(img[x, y, c]) - int(blur_img[x, y, c])
            sharp[x, y, c] = int(img[x, y, c]) + int(sharp_mask[x, y, c])
            sharp[x, y, c] = max(0, min(255, sharp[x, y, c]))
rose = np.zeros_like(img)
background = np.zeros_like(img)
for x in range(h):
    for y in range(w):
        for c in range(3):
            if red_rose[x, y]==255:
                rose[x, y, c] = sharp[x, y, c]
            else:
                background[x, y, c] = blur_img[x, y, c]
output = rose + background
plt.figure(figsize=(12, 6))
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(output)
plt.title("After Transformation")
plt.axis("off")

plt.show()

