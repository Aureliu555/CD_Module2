from utils import create_file_with_errors
from ex2a import crc_file_compute, crc_file_check

def to_write(res):
    if res:
        return "No errors found"
    else:
        return "Errors detected"

def main():
    file = "./CD_TestFiles/a.txt"
    file_with_crc_no_errors = "./Output/alice29_crc.txt"
    crc_bits = 32
    result = False
    # Creates the file with the crc on the header
    crc_file_compute(file, file_with_crc_no_errors, crc_bits)

    # Creates the fails with the error rates: 0.01%, 0.1%, 0.5%, 1% and 5%
    create_file_with_errors(file_with_crc_no_errors, "./Output/alice29_errors_0_01.txt", 0.01)
    create_file_with_errors(file_with_crc_no_errors, "./Output/alice29_errors_0_1.txt", 0.1)
    create_file_with_errors(file_with_crc_no_errors, "./Output/alice29_errors_0_5.txt", 0.5)
    create_file_with_errors(file_with_crc_no_errors, "./Output/alice29_errors_1.txt", 1)
    create_file_with_errors(file_with_crc_no_errors, "./Output/alice29_errors_5.txt", 5)

    result = crc_file_check(file_with_crc_no_errors, crc_bits)               # Cheks if there are any errors on the file with no errors
    print("File with no erros ->", to_write(result))

    result = crc_file_check("./Output/alice29_errors_0_01.txt", crc_bits)    # Cheks if there are any errors on the file with 0.01% error rate
    print("File with error rate of 0.01% ->", to_write(result))

    result = crc_file_check("./Output/alice29_errors_0_1.txt", crc_bits)     # Cheks if there are any errors on the file with 0.1% error rate
    print("File with error rate of 0.1% ->", to_write(result))

    result = crc_file_check("./Output/alice29_errors_0_5.txt", crc_bits)     # Cheks if there are any errors on the file with 0.5% error rate
    print("File with error rate of 0.5% ->", to_write(result))

    result = crc_file_check("./Output/alice29_errors_1.txt", crc_bits)       # Cheks if there are any errors on the file with 1% error rate
    print("File with error rate of 1% ->", to_write(result))

    result = crc_file_check("./Output/alice29_errors_5.txt", crc_bits)       # Cheks if there are any errors on the file with 5% error rate
    print("File with error rate of 5% ->", to_write(result))



if __name__ == "__main__":
    main()
