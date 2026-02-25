import cv2

img = cv2.imread('images.jpg')
cv2.imshow("Main img", img)
both_flips = cv2.flip(img, -1)

cv2.imshow("Flip img", both_flips)

cv2.waitKey(0)
cv2.destroyAllWindows()

