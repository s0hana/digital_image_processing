import cv2

def read_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found!")
    return img

def write_image(image_array, output_path):
    cv2.imwrite(output_path, image_array)

def main():
    input_image = r"D:\3-2\Digital Image Processing\LAB\lab1\images.jpg"
    output_image = "output.jpg"

    image_array = read_image(input_image)

    if image_array is None:
        return

    print("Array Shape:", image_array.shape)
    print(image_array)

    write_image(image_array, output_image)
    cv2.imshow("Output Image", image_array)
    cv2.waitKey(0)

main()
