import matplotlib.pyplot as plt
import numpy as np
from ex3a1 import NRZU_Coder, NRZU_Decoder, PSK_Modulator, PSK_Demodulator, channel

def rect_pulse_presentation(bits, samples_per_bit, a_max, alpha, max_noise):
    xt = NRZU_Coder(bits, samples_per_bit, a_max)
    yt = channel(xt, alpha, max_noise)
    t = np.arange(0, len(yt), 1)
    plt.plot(t, yt)
    plt.show()
    decoded_data = NRZU_Decoder(yt, samples_per_bit, a_max)
    print("NRZU =", decoded_data)

def sinusoidal_pulse_presentation(bits, tb_in_millis, samples_per_bit, f, a_max, alpha, max_noise):
    xt = PSK_Modulator(bits, tb_in_millis, samples_per_bit, f, a_max)
    yt = channel(xt, alpha, max_noise)
    t = np.arange(0, len(yt), 1)
    plt.plot(t, yt)
    plt.show()
    decoded_data = PSK_Demodulator(yt, samples_per_bit)
    print("PSK =", decoded_data)
    
def main():
    bits = [1, 0, 1, 1, 0, 0 ,0, 1]
    #rect_pulse_presentation(bits, 75, 5, 1.0, 0.0)
    #sinusoidal_pulse_presentation(bits, 1, 75, 2, 5, 1.0, 0.0)
    rect_pulse_presentation(bits, 75, 5, 1.0, 0.0)
    sinusoidal_pulse_presentation(bits, 1, 75, 2, 2, 1.0, 0.0)

if __name__ == '__main__':
    main()
