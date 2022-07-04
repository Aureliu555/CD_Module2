import serial
import time


def main():
    arduino = serial.Serial('com3', 9600, timeout=1)
    n = 0
    while n < 3:
        data = str(arduino.readline(), 'utf-8')
        if len(data) != 0:
            print(data)
            n += 1

    arduino.close()


if __name__ == '__main__':
    main()
