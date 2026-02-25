import cv2
import numpy as np
import matplotlib.pyplot as plt
img_arr = cv2.imread(r"D:\3-2\Digital Image Processing\LAB\lab4\img4.jpg", 0)
row = img_arr.shape[0]
col = img_arr.shape[1]
padded_img = np.zeros((row+2, col+2))
padded_img[1:-1, 1:-1] = img_arr
padded_img[0, 1:-1] = img_arr[0, :]
padded_img[-1, 1:-1] = img_arr[-1, :]
padded_img[1:-1, 0] = img_arr[:, 0]
padded_img[1:-1, -1] = img_arr[:, -1]

padded_img[0, 0] = img_arr[0, 0]
padded_img[0, -1] = img_arr[0, -1]
padded_img[-1, 0] = img_arr[-1, 0]
padded_img[-1, -1] = img_arr[-1, -1]

output = img_arr.copy()
mask_value = 1/9
for i in range(row):
    for j in range(col):
        img_r = padded_img[i:i+3, j:j+3]
        output[i][j] = np.sum(img_r*mask_value)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(img_arr, cmap="gray")
plt.title("Original")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(output, cmap="gray")
plt.title("After transformation")
plt.axis("off")
plt.show()
