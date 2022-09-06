from Crypto.Cipher import DES, DES3, AES
import argparse


def main():
    algoritmos = {
        "des": DES, 
        "des3": DES3, 
        "aes": AES
    }

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, type=str, help="Nome do arquivo de entrada.")
    parser.add_argument('-o', '--output', type=str, help="Nome do arquivo de saída.")
    parser.add_argument('-a', '--alg', type=str, help="Algoritmo de encriptação.", choices=['des', 'des3', 'aes'])
    parser.add_argument('-k', '--key', type=str, help="Senha de encriptação.")
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decripta o arquivo de entrada.')
    parser.add_argument('-d', '--view', action='store_true', help='Mostra informações sobre os dados.')

    args = parser.parse_args()

    key = args.key
    # if len(key) % 8 != 0:
    #     key += ('0' * (8 - (len(key) % 8)))

    if args.input:
        with open(args.input, 'r') as f:
            entrada = f.read()
            decrypt = bool(args.d)
            
            if decrypt:
                descriptografar(algoritmos[args.alg], entrada, saida)
                
            else:
                criptografar(algoritmos[args.alg], entrada, saida)

    if args.v:
        print(entrada)
        print(saida)
        print(algo)
        print(decrypt)
        print(senha)


def criptografar(alg, entrada, saida, senha):
    alg_obj = alg.new(senha, alg.MODE_ECB)
    cifrado = alg_obj.encrypt(entrada)

def descriptografar(algoritmo, entrada, saida, senha):
    alg_obj = alg.new(senha, alg.MODE_ECB)
    decifrado = alg_obj.decrypt(entrada)


if __name__ == '__main__':
    main()