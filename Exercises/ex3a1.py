import math
import numpy as np
import random as rnd

def channel(xt, alpha, max_noise):
    yt = []
    for s in xt:
        yt.append((alpha*s) + rnd.uniform(-max_noise, max_noise))
    return yt

def bit_decision(yt, samples_per_bit, avg_a):
    sum = 0
    idx = 0
    bits = []
    while idx < len(yt):
        if (idx+1) % samples_per_bit != 0:
            sum += yt[idx]
        else: 
            if (sum / samples_per_bit) > avg_a:
                bits.append(1)
            else:
                bits.append(0)
            sum = yt[idx]
        idx += 1
    return bits


def NRZU_Coder(bits, n_samples, a_max):
    xt = [] 
    for bit in bits:
        if bit == 1:
            n = n_samples
            while n > 0:
                xt.append(a_max)
                n -= 1
        else:
            n = n_samples
            while n > 0:
                xt.append(0)
                n -= 1
    return xt


def NRZU_Decoder(yt, samples_per_bit, a_max):
    return bit_decision(yt, samples_per_bit, a_max/2)


def PSK_Modulator(bits, tb, n_samples, f, a):
    t = np.arange(0, tb, 1/n_samples)
    xt = []
    for bit in bits:
        if bit == 1:
            n = 0
            while n < n_samples:
                amp = -a * np.cos(2 * math.pi * f * t[n])
                xt.append(amp)
                n += 1
        else:
            n = 0
            while n < n_samples:
                amp = a * np.cos(2 * math.pi * f * t[n])
                xt.append(amp)
                n += 1
    return xt


def PSK_Demodulator(yt, samples_per_bit):
    return bit_decision(yt, samples_per_bit, 0)


def main():
    bits = [1, 0, 1]
    xt = PSK_Modulator(bits, 1, 5, 2, 2)
    decoded = PSK_Demodulator(xt, 5)
    print(xt)

if __name__ == '__main__':
    main()