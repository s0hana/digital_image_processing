import cv2
import numpy as np
def gamma_transformations(gamma, image):
    img = cv2.imread(image, 0)
    img_a = img/255.0
    img_gamma = np.power(img_a, gamma)
    img_gamma = img_gamma*5
    mini = img_gamma[0][0]
    max_ = img_gamma[0][0]
    for i in range(img_gamma.shape[0]):
        for j in range(img_gamma.shape[1]):
            if mini>img_gamma[i][j]:
                mini = img_gamma[i][j]
            if max_<img_gamma[i][j]:
                max_  = img_gamma[i][j]
    for i in range(img_gamma.shape[0]):
        for j in range(img_gamma.shape[1]):
            img_gamma[i][j] = int(255*(img_gamma[i][j] - mini)/(max_-mini))
    img_gamma = img_gamma.astype(np.uint8)
    cv2.imshow("Output image", img_gamma)
    cv2.imshow("Input image", img)
    cv2.waitKey(0)
gamma_transformations(0.5, r"D:\3-2\Digital Image Processing\LAB\lab3\img1.jpg")
gamma_transformations(4, r"D:\3-2\Digital Image Processing\LAB\lab3\img2.jpg")