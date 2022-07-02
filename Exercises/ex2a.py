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
    file_input = open(input, "rb")
    file_out = open(output, "wb")
    data = []

    for b in file_input.read():
        data.append(b)

    checksum = CrcCalculator(crc_n(n_bits)).calculate_checksum(data)

    checksum_bytes = checksum.to_bytes(int(n_bits / 8), "big")

    file_out.write(checksum_bytes)

    file_out.write(bytearray(data))

    return checksum


def crc_file_check(input, n_bits):
    file = open(input, "rb")
    data = []
    i = 0
    expected_checksum = 0

    # Inserts on crc_code the first crc bytes characters in file.
    # Calculate the expected checksum value.
    for b in file.read():
        if i < int(n_bits / 8):
            expected_checksum = (expected_checksum << 8) + int.from_bytes(byte(b), "big")
            i += 1
        else:
            data.append(b)

    actual_checksum = CrcCalculator(crc_n(n_bits)).calculate_checksum(data)

    if actual_checksum == expected_checksum:
        print("No error has been detected.")
    else:
        print("Error detected.")


def main():
    crc_file_check('output.txt', 32)
    # print("Fst:", crc_file_compute("../CD_TestFiles/a.txt", 'output.txt', 32))
    # print("Snd:", crc_file_compute("../CD_TestFiles/a.txt", 'output.txt', 32))


if __name__ == '__main__':
    main()
