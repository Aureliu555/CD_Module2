import serial
import time


def main():
    arduino = serial.Serial('com3', 9600, timeout=1)
    n = 0
    while n < 3:
        data = str(arduino.readline(), 'utf-8')
        print(data)
        if len(data) != 0:
            n += 1

    arduino.close()


if __name__ == '__main__':
    main()
