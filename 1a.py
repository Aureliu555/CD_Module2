import random
import cv2
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------ #
# ---------------------------------- CAESAR ------------------------------------------ #

def shift_right_byte(byte, offset):
    if (byte + offset > 255):
        return offset - (255-byte)
    else:
        return byte + offset

def shift_left_byte(byte, offset):
    if (byte - offset < 0):
        return 255 - (offset - byte)
    else:
        return byte - offset

def shift_right(char, offset):
    if (ord(char) + offset > 255):
        return chr(offset - (255-ord(char)))
    else:
        return chr(ord(char) + offset)

def shift_left(char, offset):
    if (ord(char) - offset < 0):
        return chr(255 - (offset - ord(char)))
    else:
        return chr(ord(char) - offset)

def caeser(input, output, offset, chipher):
    fin = open(input, "r")
    fout = open(output, "w")
    for c in fin.read():
        if (chipher):
            fout.write(shift_right(c, offset))
        else:
            fout.write(shift_left(c, offset))
    fin.close
    fout.close


# ------------------------------------------------------------------------------------ #
# ---------------------------------- VERNAM ------------------------------------------ #

def vernam_encipher(input, output):
    fin = open(input, "rb")
    fout = open(output, "wb")
    key = []
    bytes = []
    rand_num = None
    for byte in fin.read():
        rand_num = random.randint(0, 255)
        key.append(rand_num)
        bytes.append(byte^rand_num)
    fout.write(bytearray(bytes))
    fin.close
    fout.close
    return key

def vernam_decipher(input, output, key):
    fin = open(input, "rb")
    fout = open(output, "wb")
    bytes = []
    idx = 0
    for byte in fin.read():
        bytes.append(byte^key[idx])
        idx += 1
    fout.write(bytearray(bytes))
    fin.close
    fout.close


# ------------------------------------------------------------------------------------------ #
# ---------------------------------- IMAGE CIPHER ------------------------------------------ #

KEY = []

def image_encipher(input, output, x_left, y_up, width, height):
    img = cv2.imread(input, 0)
    for x in range(height):
        for y in range(width):
            img[x_left+x][y_up+y] = random.randint(0, 255)
    cv2.imshow("grayscale_img", img)       
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

# -------------------------------------------------------------------------------- #
# ----------------------------------MAIN------------------------------------------ #

def main():
    #caeser("CD_TestFiles/a.txt", "Output/a_ccipher.txt", 5, True)
    #caeser("Output/a_ccipher.txt", "Output/a_cdecipher.txt", 5, False)
    #key = vernam_encipher("CD_TestFiles/a.txt", "Output/a_vcipher.txt")
    #vernam_decipher("Output/a_vcipher.txt", "Output/a_vdecipher.txt", key)
    image_encipher("CD_TestFiles/lena.bmp", "", 34, 58, 150, 150)

if __name__ == "__main__":
    main()