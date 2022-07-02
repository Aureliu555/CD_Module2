import matplotlib.pyplot as plt
import numpy as np


def insert_bits_into(bits, container, max, min):
    if container[0] == max:
        bits.append(1)
    elif container[0] == min:
        bits.append(0)


def NRZU_Coder(binary_sequence, t, max, min):
    length = len(binary_sequence)

    emitter = [] * (length * t)
    for bit in binary_sequence:
        if bit == 1:
            n = t
            while n > 0:
                emitter.append(max)
                n -= 1
        else:
            n = t
            while n > 0:
                emitter.append(min)
                n -= 1

    plt.title("Unipolar NRZ")
    plt.plot(emitter)
    plt.show()

    return emitter


def NRZU_Decoder(binary_sequence, t, max, min):
    length = len(binary_sequence)
    code = []
    container = []
    idx = 0

    while 0 <= idx <= len(binary_sequence):
        if idx == len(binary_sequence):
            insert_bits_into(code, container, max, min)
            break

        bit = binary_sequence[idx]
        if len(container) < t:
            container.append(bit)
        else:
            insert_bits_into(code, container, max, min)
            container = [bit]

        idx += 1

    if len(code) == int(length / t):
        return code
    else:
        return "An error has occurred on NRZU decode."


def main():
    coded = NRZU_Coder([1, 0, 0, 1, 1, 0, 1], 10, 5, 0)
    print(coded)
    # unipolarNRZ = []
    # for x in coded:
    #     for i in range(100):
    #         unipolarNRZ.append(x)
    # decoded = NRZU_Decoder(coded, 10, 5, 0)
    # print(decoded)
    rng = np.arange(50)
    rnd = np.random.randint(0, 10, size=(3, rng.size))
    yrs = 1950 + rng

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
    ax.set_title('Combined debt growth over time')
    ax.legend(loc='upper left')
    ax.set_ylabel('Total debt')
    ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
    fig.tight_layout()


if __name__ == '__main__':
    main()
