from utils import get_entropy, create_histogram
from ex1a import caeser, vernam_encipher, vernam_decipher

# Test that includes the entropy presented in the console of 
# both given files and creates a histogram for each one of them
def files_test(file1, file2):
    print("Entropy of", file1, " ->", get_entropy(file1))
    create_histogram(file1)
    print("Entropy of ", file2, " ->", get_entropy(file2))
    create_histogram(file2)


# -------------------------------------------------------------------------------- #
# ----------------------------------MAIN------------------------------------------ #
def main():
    file1 = "./CD_TestFiles/a.txt"
    file2 = "./CD_TestFiles/alice29.txt"

    file1_enciph_caeser = "./Output/a_caesar_encipher.txt"
    file2_enciph_caeser = "./Output/alice29_caesar_encipher.txt"

    file1_deciph_caeser = "./Output/a_caeser_decipher.txt"
    file2_deciph_caeser = "./Output/alice29_caeser_decipher.txt"

    file1_enciph_vernam = "./Output/a_vernam_encipher.txt"
    file2_enciph_vernam = "./Output/alice29_vernam_encipher.txt"

    file1_deciph_vernam = "./Output/a_vernam_decipher.txt"
    file2_deciph_vernam = "./Output/alice29_vernam_decipher.txt"

    
    # ------------------------------------------------------------ #
    # ------------------- Original files test -------------------- #
    # ------------------------------------------------------------ #
    files_test(file1, file2)
    

    # ------------------------------------------------------------ #
    # ----- Enciphered files test using CAESER technique --------- #
    # ------------------------------------------------------------ #
    caeser(file1, file1_enciph_caeser, 4, True)
    caeser(file2, file2_enciph_caeser, 4, True)

    files_test(file1_enciph_caeser, file2_enciph_caeser)
 

    # ------------------------------------------------------------ #
    # ----- Deciphered files test using CAESER technique --------- #
    # ------------------------------------------------------------ #
    caeser(file1_enciph_caeser, file1_deciph_caeser, 4, False)
    caeser(file2_enciph_caeser, file2_deciph_caeser, 4, False)

    files_test(file1_deciph_caeser, file2_deciph_caeser)
    

    # ------------------------------------------------------------ #
    # ----- Enciphered files test using VERNAM technique --------- #
    # ------------------------------------------------------------ #
    key1 = vernam_encipher(file1, file1_enciph_vernam)
    key2 = vernam_encipher(file2, file2_enciph_vernam)

    files_test(file1_enciph_vernam, file2_enciph_vernam)


    # ------------------------------------------------------------ #
    # ----- Deciphered files test using VERNAM technique --------- #
    # ------------------------------------------------------------ #
    vernam_decipher(file1_enciph_vernam, file1_deciph_vernam, key1)
    vernam_decipher(file2_enciph_vernam, file2_deciph_vernam, key2)

    files_test(file1_deciph_vernam, file2_deciph_vernam)


if __name__ == "__main__":
    main()
