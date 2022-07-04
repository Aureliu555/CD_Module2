from crc import Crc8, Crc16, Crc32, Crc64, CrcCalculator

from numpy import byte

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
        return True
    else:
        return False

