import random
import cv2 

# ------------------------------------------------------------------------------------------ #
# ---------------------------------- IMAGE CIPHER ------------------------------------------ #

def image_encipher(input, output, x_left, y_up, width, height):
    img = cv2.imread(input, 0)
    key = []
    for x in range(height):
        for y in range(width):
            rand_num = random.randint(0, 255)
            pixel = img[x_left + x][y_up + y]
            pixel_key = pixel ^ rand_num
            img[x_left + x][y_up + y] = pixel_key
            key.append(rand_num)
    cv2.imwrite(output, img)
    return key


def image_decipher(input, output, x_left, y_up, width, height, key):
    img = cv2.imread(input, 0)
    idx = 0
    for x in range(height):
        for y in range(width):
            pixel = img[x_left + x][y_up + y]
            img[x_left + x][y_up + y] = key[idx] ^ pixel
            idx += 1
    cv2.imwrite(output, img)


# -------------------------------------------------------------------------------- #
# ----------------------------------MAIN------------------------------------------ #

def main():
    key = image_encipher("CD_TestFiles/lena.bmp", "Output/lena_encipher.bmp", 34, 58, 150, 150)
    image_decipher("Output/lena_encipher.bmp", "Output/lena_decipher.bmp", 34, 58, 150, 150, key)


if __name__ == "__main__":
    main()
