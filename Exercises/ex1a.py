import random
# import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------ #
# ---------------------------------- CAESAR ------------------------------------------ #
# import numpy as np
from nltk import entropy
import random
import matplotlib.pyplot as plt
import numpy as np


def shift_right_byte(byte, offset):
    if (byte + offset > 255):
        return offset - (255 - byte)
    else:
        return byte + offset


def shift_left_byte(byte, offset):
    if (byte - offset < 0):
        return 255 - (offset - byte)
    else:
        return byte - offset


def shift_right(char, offset):
    if (ord(char) + offset > 255):
        return chr(offset - (255 - ord(char)))
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
    fin.close()
    fout.close()


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
        bytes.append(byte ^ rand_num)
    fout.write(bytearray(bytes))
    fin.close()
    fout.close()
    return key


def vernam_decipher(input, output, key):
    fin = open(input, "rb")
    fout = open(output, "wb")
    bytes = []
    idx = 0
    for byte in fin.read():
        bytes.append(byte ^ key[idx])
        idx += 1
    fout.write(bytearray(bytes))
    fin.close()
    fout.close()

