import cv2
import numpy as np
import matplotlib.pyplot as plt

img_arr = cv2.imread(r"D:\3-2\Digital Image Processing\LAB\lab4\img2.jpg", 0)
rows =  img_arr.shape[0]
cols = img_arr.shape[1]

g_x = img_arr.copy()
g_y = img_arr.copy()
gradient = img_arr.copy()

for i in range(rows-1):
    for j in range(cols-1):
        z5 = img_arr[i, j]        
        z6 = img_arr[i, j+1]     
        z8 = img_arr[i+1, j]      

        g_x[i, j] = z8 - z5
        g_y[i, j] = z6 - z5
        gradient[i, j] = abs(g_x[i, j]) + abs(g_y[i, j]) + z5  

gradient_display = np.clip(gradient, 0, 255).astype(np.uint8)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(img_arr, cmap="gray")
plt.title("Original")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(gradient_display, cmap="gray")
plt.title("After transformation")
plt.axis("off")
plt.show()
