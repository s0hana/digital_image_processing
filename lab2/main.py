import cv2
import numpy as np
img_A = cv2.imread(r"D:\3-2\Digital Image Processing\LAB\lab2\img3.jpg", 0)
print(f"Array of img A: {img_A}")
print(f"Shape: {np.shape(img_A)}")
img_B = np.copy(img_A)
for i in range(img_B.shape[0]):
    for j in range(img_B.shape[1]):
        img_B[i][j] = 255 - img_B[i][j]
print(f"Array of img B: {img_B}")
print(f"Shape: {np.shape(img_B)}")
log_img_B = np.copy(img_B)
log_img_B = log_img_B.astype(float)
for i in range(log_img_B.shape[0]):
    for j in range(log_img_B.shape[1]):
        log_img_B[i][j] = np.log(img_A[i][j]+1.0)
minimum = log_img_B[0][0]
maximum = log_img_B[0][0]
for i in range(log_img_B.shape[0]):
    for j in range(log_img_B.shape[1]):
        if log_img_B[i][j]>maximum:
            maximum = log_img_B[i][j]
        if log_img_B[i][j]<minimum:
            minimum = log_img_B[i][j]
for i in range(log_img_B.shape[0]):
    for j in range(log_img_B.shape[1]):
        log_img_B[i][j] = int(255*(log_img_B[i][j] - minimum)/(maximum - minimum))
log_img_B = log_img_B.astype(np.uint8)
print(f"Final array: {log_img_B}")
print(f"Shape: {np.shape(log_img_B)}")
cv2.imshow("Original Image", img_A)
cv2.imshow("Negative Image", img_B)
cv2.imshow("After log and scaling", log_img_B)
cv2.waitKey(0)
cv2.destroyAllWindolws()
