import random
import cv2
#import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------ #
# ---------------------------------- CAESAR ------------------------------------------ #
#import numpy as np
from nltk import entropy
import random
from scipy.stats import entropy
import matplotlib.pyplot as plt
import numpy as np



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
    

# Reads a file and puts all words in an array
def file_read(f):
    file = open(f, "r")
    arr = []
    for i in file.read():
        arr.append(i)
    file.close()
    return arr


# Gets the file entropy
def get_entropy(file):
    array = file_read(file)
    value, counts = np.unique(array, return_counts=True)
    e = entropy(counts, base=None)
    return e


# Gets the file characters
def get_file_characters(file):
    f = open(file, 'r').read()
    characters = []

    for i in f:
        if i != ' ' and i != '' and i != '\n':
            characters += i
    return characters


# Creates a histogram for all file characters
def create_histogram_for_file_chars(f, bins):
    array = get_file_characters(f)
    plt.hist(array, bins=bins)
    plt.show()
# -------------------------------------------------------------------------------- #
# ----------------------------------MAIN------------------------------------------ #

def main():
    #caeser("CD_TestFiles/a.txt", "Output/a_ccipher.txt", 5, True)
    #caeser("Output/a_ccipher.txt", "Output/a_cdecipher.txt", 5, False)
    #key = vernam_encipher("CD_TestFiles/a.txt", "Output/a_vcipher.txt")
    #vernam_decipher("Output/a_vcipher.txt", "Output/a_vdecipher.txt", key)
    #image_encipher("CD_TestFiles/lena.bmp", "", 34, 58, 150, 150)
    # --------------------------- i ------------------------- #
    first_file_entropy = get_entropy("CD_TestFiles/a.txt")
    print("FileA entropy: ", first_file_entropy)

    second_file_entropy = get_entropy("CD_TestFiles/alice29.txt")
    print("FileB entropy: ", second_file_entropy)

    # Histogram for the first text file
    create_histogram_for_file_chars("CD_TestFiles/a.txt", 10)

    # Histogram for the second text file
    create_histogram_for_file_chars("CD_TestFiles/alice29.txt", 10)

    # -----------------------------------------------------------------------------------------------------------------------
    # -------------------------- ii ------------------------ #
    #
    # ------------- Caesar Encipher
    # Generates a file enciphered with caesar method
    num_for_shift = 4
    caeser("CD_TestFiles/a.txt", "fileA_CaesarEncipheredOutput.txt", num_for_shift, True)
    caeser("CD_TestFiles/alice29.txt", "fileB_CaesarEncipheredOutput.txt", num_for_shift, True)

    # Entropy for caesar enciphered text file
    fileA_caesar_enciphered_entropy = get_entropy("fileA_CaesarEncipheredOutput.txt")
    print("Enciphered fileA (Caesar) entropy: ", fileA_caesar_enciphered_entropy)
    fileB_caesar_enciphered_entropy = get_entropy("fileB_CaesarEncipheredOutput.txt")
    print("Enciphered fileB (Caesar) entropy: ", fileB_caesar_enciphered_entropy)

    # Histogram for caesar enciphered text file
    binFC = 10
    create_histogram_for_file_chars("fileA_CaesarEncipheredOutput.txt", binFC)
    create_histogram_for_file_chars("fileB_CaesarEncipheredOutput.txt", binFC)

    # ------------- Vernam Encipher
    # Generates a file enciphered with vernam method and its keys
    fileA_keys = vernam_encipher("CD_TestFiles/a.txt", "fileA_VernamEncipheredOutput.txt")
    fileB_keys = vernam_encipher("CD_TestFiles/alice29.txt", "fileB_VernamEncipheredOutput.txt")

    # Entropy for vernam enciphered text file
    fileA_vernam_enciphered_entropy = get_entropy("fileA_VernamEncipheredOutput.txt")
    print("Enciphered fileA (Vernam) entropy: ", fileA_vernam_enciphered_entropy)
    fileB_vernam_enciphered_entropy = get_entropy("fileB_VernamEncipheredOutput.txt")
    print("Enciphered fileB (Vernam) entropy: ", fileB_vernam_enciphered_entropy)

    # Histogram for vernam enciphered text file
    binFV = 10
    create_histogram_for_file_chars("fileA_VernamEncipheredOutput.txt", binFV)
    create_histogram_for_file_chars("fileB_VernamEncipheredOutput.txt", binFV)
    # -----------------------------------------------------------------------------------------------------------------------

    # -----------------------------------------------------------------------------------------------------------------------
    # ------------------------- iii ----------------------- #
    # ------------- Caesar Decipher
    # Generates a file deciphered with caesar method
    caeser("fileA_CaesarEncipheredOutput.txt", "fileA_CaesarDecipheredOutput.txt", num_for_shift, False)
    caeser("fileB_CaesarEncipheredOutput.txt", "fileB_CaesarDecipheredOutput.txt", num_for_shift, False)

    # Entropy for caesar deciphered text file
    fileA_caesar_deciphered_entropy = get_entropy("fileA_CaesarDecipheredOutput.txt")
    print("Deciphered fileA (Caesar) entropy: ", fileA_caesar_deciphered_entropy)
    fileB_caesar_deciphered_entropy = get_entropy("fileB_CaesarDecipheredOutput.txt")
    print("Deciphered fileB (Caesar) entropy: ", fileB_caesar_deciphered_entropy)

    # Histogram for caesar deciphered text file
    create_histogram_for_file_chars("fileA_CaesarDecipheredOutput.txt", binFC)
    create_histogram_for_file_chars("fileB_CaesarDecipheredOutput.txt", binFC)

    # ------------- Vernam Decipher
    # Generates a file deciphered with caesar method
    vernam_decipher("fileA_VernamEncipheredOutput.txt", "fileA_VernamDecipheredOutput.txt", fileA_keys)
    vernam_decipher("fileB_VernamEncipheredOutput.txt", "fileB_VernamDecipheredOutput.txt", fileB_keys)

    # Entropy for caesar deciphered text file
    fileA_vernam_deciphered_entropy = get_entropy("fileA_VernamDecipheredOutput.txt")
    print("Deciphered fileA (Vernam) entropy: ", fileA_vernam_deciphered_entropy)
    fileB_vernam_deciphered_entropy = get_entropy("fileB_VernamDecipheredOutput.txt")
    print("Deciphered fileB (Vernam) entropy: ", fileB_vernam_deciphered_entropy)

    # Histogram for caesar deciphered text file
    create_histogram_for_file_chars("fileA_VernamDecipheredOutput.txt", binFV)
    create_histogram_for_file_chars("fileB_VernamDecipheredOutput.txt", binFV)
    # -----------------------------------------------------------------------------------------------------------------------

    # -------------------------- iv ------------------------ #

if __name__ == "__main__":
    main()