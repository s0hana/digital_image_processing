import cv2
import numpy as np
import matplotlib.pyplot as plt

img_arr = cv2.imread(r"D:\3-2\Digital Image Processing\LAB\lab4\img2.jpg", 0)
row = img_arr.shape[0]
col = img_arr.shape[1]

padded_img = np.zeros((row+2, col+2))
padded_img[1:-1, 1:-1] = img_arr
output = img_arr.copy()

'''mask_value = np.array([[-1,-1,-1],
        [-1,8,-1],
        [-1,-1,-1]])'''
mask_value = np.array([[0, 1, 0],
                       [1, -4, 1],
                       [0, 1, 0]])

for i in range(row):
    for j in range(col):
        img_r = padded_img[i:i+3, j:j+3]
        k = np.sum(img_r*mask_value) + img_arr[i, j] 
        if k > 255:
            output[i][j] = 255
        elif k<0:
            output[i][j] = 0
        else: 
            output[i][j] = k
        
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
