import matplotlib.pyplot as plt
import numpy as np
from ex3a1 import NRZU_Coder, NRZU_Decoder, PSK_Modulator, PSK_Demodulator

def rect_pulse_presentation(bits, samples_per_bit, a_max):
    coded = NRZU_Coder(bits, samples_per_bit, a_max)
    t = np.arange(0, len(coded), 1)
    plt.plot(t, coded)
    plt.show()
    decoded = NRZU_Decoder(coded, samples_per_bit, a_max)
    print("NRZU =", decoded)

def sinusoidal_pulse_presentation(bits, tb_in_millis, samples_per_bit, f, a_max):
    modulator = PSK_Modulator(bits, tb_in_millis, samples_per_bit, f, a_max)
    t = np.arange(0, len(modulator), 1)
    plt.plot(t, modulator)
    plt.show()
    demodulator = PSK_Demodulator(modulator, samples_per_bit)
    print("PSK =", demodulator)
    
def main():
    bits = [1, 0, 1, 1, 0, 0, 0, 1]
    rect_pulse_presentation(bits, 100, 5)
    sinusoidal_pulse_presentation(bits, 1, 100, 2, 2)

if __name__ == '__main__':
    main()
