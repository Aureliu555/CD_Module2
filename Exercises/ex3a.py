import matplotlib.pyplot as plt
import numpy as np


def insert_bits_into(bits, container, max, min):
    if container[0] == max:
        bits.append(1)
    elif container[0] == min:
        bits.append(0)


def NRZU_Coder(binary_sequence, num_of_images_per_bits, max, min):
    length = len(binary_sequence)
    n = num_of_images_per_bits
    emitter = [] * (length * n)
    for bit in binary_sequence:
        if bit == 1:
            n = num_of_images_per_bits
            while n > 0:
                emitter.append(max)
                n -= 1
        else:
            n = num_of_images_per_bits
            while n > 0:
                emitter.append(min)
                n -= 1
    return emitter


def NRZU_Decoder(binary_sequence, num_of_images_per_bits, max, min):
    length = len(binary_sequence)
    code = []
    container = []
    idx = 0

    while 0 <= idx <= len(binary_sequence):
        if idx == len(binary_sequence):
            insert_bits_into(code, container, max, min)
            break

        bit = binary_sequence[idx]
        if len(container) < num_of_images_per_bits:
            container.append(bit)
        else:
            insert_bits_into(code, container, max, min)
            container = [bit]

        idx += 1

    if len(code) == int(length / num_of_images_per_bits):
        return code
    else:
        return "An error has occurred on decode."


def main():
    coded = NRZU_Coder([1, 0, 0, 1, 0, 1, 1], 10, 5, 0)
    print(coded)
    decoded = NRZU_Decoder(coded, 10, 5, 0)
    print(decoded)


if __name__ == '__main__':
    main()
