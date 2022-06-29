from crc import *
import binascii

from numpy import byte

from CD_TestFiles import *


# def calculate_crc(file_path, convert_newlines):
#     with open(file_path, 'rb') as f:
#         data = f.read()
#
#     try:
#         data.decode()
#         is_text = True
#     except UnicodeError:
#         is_text = False
#
#     if is_text and convert_newlines:
#         data = data.replace(b'\r\n', b'\n')
#     crc = binascii.crc32(data)
#
#     return crc
#
#
# def crc32_from_file(filename):
#     buf = open(filename, 'rb').read()
#     buf = (binascii.crc32(buf) & 0xFFFFFFFF)
#     return "%08X" % buf
#
#
# def crc_file_compute(input_file, output_file):
#     buf = open(input_file, 'rb').read()
#     bts = []
#     for char in buf:
#         bts.append(''.join(byte(char)))
#
#
# def xor(a, b):
#     result = []
#
#     for i in range(1, len(b)):
#         if a[i] == b[i]:
#             result.append('0')
#         else:
#             result.append('1')
#
#     return ''.join(result)
#
#
# def mod2_div(divident, divisor):
#     pick = len(divisor)
#     tmp = divident[0: pick]
#
#     while pick < len(divident):
#         if tmp[0] == '1':
#             tmp = xor(divisor, tmp) + divident[pick]
#         else:  # If leftmost bit is '0'
#             tmp = xor('0' * pick, tmp) + divident[pick]
#         pick += 1
#
#     if tmp[0] == '1':
#         tmp = xor(divisor, tmp)
#     else:
#         tmp = xor('0' * pick, tmp)
#
#     checkword = tmp
#     return checkword
#
#
# def decode_data(data, key):
#     l_key = len(key)
#
#     # Appends n-1 zeroes at end of data
#     appended_data = data.decode() + '0' * (l_key - 1)
#     remainder = mod2_div(appended_data, key)
#
#     return remainder

def crc_n(n):
    crc = Crc8.CCITT

    if n == 16:
        crc = Crc16.CCITT
    elif n == 8:
        crc = Crc8.CCITT
    elif n == 32:
        crc = Crc32.CRC32
    elif n == 64:
        crc = Crc64.CRC64

    return crc


def crc_file_compute(input, output, n_bits):
    crc = crc_n(n_bits)

    crc_calculator = CrcCalculator(crc)

    file_input = open(input, "rb")
    file_out = open(output, "wb")
    data = []

    for char in file_input.read():
        data.append(char)

    checksum = crc_calculator.calculate_checksum(data)

    checksum_bytes = checksum.to_bytes(int(n_bits / 8), "big")

    file_out.write(checksum_bytes)

    file_out.write(bytearray(data))

    return checksum


def crc_file_check(input, n_bits):

    file = open(input, "rb")

    crc_code = []
    # Inserts on crc_code the first crc bytes characters in file.
    i = 0
    while i < int(n_bits / 8):
        crc_code.append((file.read(1)))
        i += 1

    expected = 0

    # Calculate the expected checksum value.
    for i in crc_code:
        expected = (expected << 8) + int.from_bytes(i, "big")

    print(expected)


def main():
    crc_file_check('output.txt', 32)
    # print("Fst:", crc_file_compute("../CD_TestFiles/a.txt", 'output.txt', 32))
    # print("Snd:", crc_file_compute("../CD_TestFiles/a.txt", 'output.txt', 32))


if __name__ == '__main__':
    main()
