from ex3a1 import *

def calculate_BER(original_bits_arr, decoded_bits_arr):
    total_bits = len(original_bits_arr)
    errors = 0
    idx = 0
    while idx < total_bits:
        if original_bits_arr[idx] != decoded_bits_arr[idx]:
            errors += 1
        idx += 1
    return errors/total_bits

def test_scd_rect_pulse(bits, samples_per_bit, a_max, alpha, max_noise):
    xt = NRZU_Coder(bits, samples_per_bit, a_max)
    yt = channel(xt, alpha, max_noise)
    decoded_bits = NRZU_Decoder(yt, samples_per_bit, a_max)
    return calculate_BER(bits, decoded_bits)


def test_scd_sin_pulse(bits, tb_in_millis, samples_per_bit, f, a_max, alpha, max_noise):
    xt = PSK_Modulator(bits, tb_in_millis, samples_per_bit, f, a_max)
    yt = channel(xt, alpha, max_noise)
    decoded_bits = PSK_Demodulator(yt, samples_per_bit)
    return calculate_BER(bits, decoded_bits)


def main():
    bits = [1, 0, 1, 1, 0 ,0 , 0, 1]
    print("BER_NRZU with (alpha = 1) && (noise in -0.8..0.8) ->", test_scd_rect_pulse(bits, 8, 5, 1.0, 0.8))
    print("BER_PSK with (alpha = 1) && (noise in -0.8..0.8) ->", test_scd_sin_pulse(bits, 1, 100, 2, 2, 1.0, 0.8), "\n")
    print("BER_NRZU with (alpha < 1) && (noise = 0) ->", test_scd_rect_pulse(bits, 10, 5, 0.5, 0.0))
    print("BER_PSK with (alpha < 1) && (noise = 0) ->", test_scd_sin_pulse(bits, 1, 100, 2, 2, 0.5, 0.0))

if __name__ == '__main__':
    main()
