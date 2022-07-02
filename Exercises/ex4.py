import serial
import time


def main():
    arduino = serial.Serial('com3', 9600)
    time.sleep(1)
    data = arduino.readline()
    print("Be happy")
    print(data)
    n = 5
    # while n > 0:
    #     if data != arduino.readline():
    #         data = arduino.readline()
    #         print('New data:', data)
    #         n = n-1
    while n > 0:
        while arduino.inWaiting() == 0:
            pass
        data = arduino.readline()
        print('New data:', data)
        n = n-1

    arduino.close()


if __name__ == '__main__':
    main()
