import cv2
import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
original = cv2.imread(r"D:\3-2\Digital Image Processing\LAB\lab5\img2.jpg", 0)
orig_h, orig_w = original.shape
img = cv2.resize(cv2.imread(r"D:\3-2\Digital Image Processing\LAB\lab5\img2.jpg", 0), (50, 50))
height, width = img.shape
F = np.zeros((height,width), dtype=complex)
G_low = np.zeros((height,width), dtype=complex)
G_high = np.zeros((height,width), dtype=complex)
g_low = np.zeros((height,width), dtype=np.uint8)
g_high = np.zeros((height,width), dtype=np.uint8)
H_low = np.zeros((height, width))
H_high = np.zeros((height, width))
d0 = 15
for u in range(height):
    for v in range(width):
        sum_val = 0
        for x in range(height):
            for y in range(width):
                pixel_value = int(img[x][y]) * ((-1) ** (x + y))
                power = -2j * math.pi * ((u * x) / height + (v * y) / width)
                sum_val += pixel_value * cmath.exp(power)
        F[u][v] = sum_val / (height * width)

for u in range(height):
    for v in range(width):
        d = math.sqrt((u - height / 2) ** 2 + (v - width / 2) ** 2)
        if d <= d0:
            H_low[u][v] = 1
            H_high[u][v] = 0
        else:
            H_low[u][v] = 0
            H_high[u][v] = 1

for u in range(height):
    for v in range(width):
        G_low[u][v] = F[u][v] * H_low[u][v]
        G_high[u][v] = F[u][v] * H_high[u][v]

for x in range(height):
    for y in range(width):
        sum_val_low = 0
        sum_val_high = 0
        for u in range(height):
            for v in range(width):
                angle = 2j * math.pi * ((u * x) / height + (v * y) / width)
                sum_val_low += G_low[u][v] * cmath.exp(angle)
                sum_val_high += G_high[u][v] * cmath.exp(angle)

        low_value = int(sum_val_low.real * ((-1) ** (x + y)))
        high_value = int(sum_val_high.real * ((-1) ** (x + y)))

        if low_value < 0:
            low_value = 0
        elif low_value > 255:
            low_value = 255

        if high_value < 0:
            high_value = 0
        elif high_value > 255:
            high_value = 255

        g_low[x][y] = low_value
        g_high[x][y] = high_value
g_low_resized = cv2.resize(g_low, (orig_w, orig_h))
g_high_resized = cv2.resize(g_high, (orig_w, orig_h))
#g_high_resized = g_high_resized + original

plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1)
plt.imshow(original, cmap="gray")
plt.title("Original")
plt.axis("off")
plt.subplot(1, 3, 2)
plt.imshow(g_low_resized, cmap="gray")
plt.title("Low pass")
plt.axis("off")
plt.subplot(1, 3, 3)
plt.imshow(g_high_resized, cmap="gray")
plt.title("High pass")
plt.axis("off")
plt.show()