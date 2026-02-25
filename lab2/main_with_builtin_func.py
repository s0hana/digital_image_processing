import cv2
import numpy as np
img_A = cv2.imread(r"D:\3-2\Digital Image Processing\LAB\lab2\img2.jpg", 0)
print(f"Initial array: {img_A}")
img_B = 255 - img_A
print(f"Negative image array: {img_B}")
added_1 = img_A + 1.0
log_img_B = np.log(added_1)
log_img_scl = 255 * (log_img_B - log_img_B.min()) / (log_img_B.max() - log_img_B.min())
log_img_scl = log_img_scl.astype(np.uint8)
print(f"Logged image array: {log_img_scl}")
cv2.imshow("Initial image", img_A)
cv2.imshow("Negative image", img_B)
cv2.imshow("Final image", log_img_scl)
cv2.waitKey(0)
cv2.destroyAllWindows()
