import math
import matplotlib.pyplot as plt
import numpy as np
from random import randint

def arr_from_file(file):
    arr = []
    f = open(file, "r")
    for c in f.read():
        arr.append(c)
    f.close()
    return arr

def create_file_with_errors(input, ouput, error_rate):
    in_arr = arr_from_file(input)
    f_out = open(ouput, "w")
    arr_size = len(in_arr)
    errors = arr_size*(error_rate/100)
    idx_arr = []
    j = 0
    while j < errors:
        rnd = randint(8, arr_size-1)
        if rnd not in idx_arr:
            idx_arr.append(rnd)
            j += 1
    for idx in idx_arr:
        in_arr[idx] = chr(randint(0, 80))       # !! It was supposed to be from 0..255 but the characters above 80 are hard to map into chars
    for c in in_arr:
        f_out.write(c)
    f_out.close()

# Creates a dictionary with each character and its occurence from the file passed as parameter
def words_from_file(file):
    my_dict = {}
    f = open(file, "rb")
    t = 0
    for c in f.read():
        t += 1
        if c in my_dict:
            my_dict[c] += 1
        else:
            my_dict[c] = 1
    f.close()
    return my_dict, t

# Calculates the entropy from a given file 
def get_entropy(file):
    my_dict, total = words_from_file(file)      # creates the dictionary with the character and its occurences
    count = 0
    for i in my_dict:
        count += (my_dict[i] / total) * math.log2(my_dict[i] / total)   # auxiliary sum to the full entropy calculation
    return -1 * count   # retruns the entropy

# Creates a histogram from a given file
def create_histogram(file):
    my_dict, total = words_from_file(file)
    occurences = my_dict.values()
    bytes = my_dict.keys()
    chars = []
    for b in bytes:
        chars.append(chr(b))
    bar_x_locations = np.arange(len(occurences))
    plt.bar(bar_x_locations, occurences, align = 'center')
    plt.xticks(bar_x_locations, chars)
    plt.show()
