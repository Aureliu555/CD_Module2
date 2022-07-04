from ex2a import crc_file_compute, crc_file_check

def main():
    # 1º Passo -> codificar o ficheiro a.txt
    file_coded = "./Output/a_coded.txt"
    file_coded_crc = "./Output/a_coded_crc.txt"
    crc_bits = 32

    # Partindo do principio que o ficheiro "a_coded.txt" é o ficheiro que foi codificado pelo modulo anteiror
    # 2º Passo -> aplicar o CRC ao cabeçalho do ficheiro
    crc_file_compute(file_coded, file_coded_crc, crc_bits)

    # 3º Passo -> verificação da integridade do ficheiro "a_coded_crc.txt" com o CRC presente no cabeçalho através do uso da função crc_file_check
    crc_file_check(file_coded_crc, crc_bits)

    # 4º Passo -> Caso o ficheiro "a_coded_crc.txt" tenha passado com sucesso pela função crc_file_check (return True), será executada a função
    #             descodificadora do modulo anteiror

if __name__ == "__main__":
    main()