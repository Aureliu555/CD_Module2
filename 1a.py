import random

# ------------------------------------------------------------------------------------ #
# ---------------------------------- CAESAR ------------------------------------------ #

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

# -------------------------------------------------------------------------------- #
# ----------------------------------MAIN------------------------------------------ #

def main():
    #caeser("CD_TestFiles/a.txt", "Output/a_ccipher.txt", 5, True)
    #caeser("Output/a_ccipher.txt", "Output/a_cdecipher.txt", 5, False)
    key = vernam_encipher("CD_TestFiles/a.txt", "Output/a_vcipher.txt")
    vernam_decipher("Output/a_vcipher.txt", "Output/a_vdecipher.txt", key)

if __name__ == "__main__":
    main()