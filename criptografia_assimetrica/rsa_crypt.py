import argparse
import rsa


def main():
    """Criptografa e descriptografa arquivos"""
    
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', 
        action='store_true',
        help='Descriptografa o arquivo de entrada.')

    parser.add_argument('-e', 
        action='store_true',
        help='Criptografa o arquivo de entrada.')

    parser.add_argument('-i',
        type=str,
        help='Arquivo de entrada.',
        required=True)
    
    parser.add_argument('-o',
        type=str,
        help='Arquivo de saída.')

    parser.add_argument('-k',
        type=str,
        help='Arquivo com a chave.',
        required=True)

    args = parser.parse_args()

    #Verifica se é para descriptografar
    if args.d:
        encrypt=False
    else:
        encrypt = True

    #Algoritmo
    algo = 'des'
    if args.a:
        algo = args.a
    algoritmos = {
        "des": DES, 
        "des3": DES3, 
        "aes": AES
    }
    algo = algoritmos[algo]

    #Entrada
    arq_entrada = args.i

    #Saida
    arq_saida = f'{arq_entrada}.crypto'
    if args.o:
        arq_saida = args.o

    #Senha
    senha = args.k

    if args.v:
        print('Entrada: ', arq_entrada)
        print('Saida: ', arq_saida)
        print('Algoritmo: ', algo)
        print('Criptografar: ', encrypt)
        print('Senha: ', senha)

    
    if encrypt:
        criptografar(arq_entrada, arq_saida, algo, senha)
    else:
        descriptografar(arq_entrada, arq_saida, algo, senha)


def criptografar(entrada, saida, alg, senha):
    with open(entrada, 'r') as f:
        dados = f.read()
    alg_obj = alg.new(senha, alg.MODE_ECB)
    cifrado = alg_obj.encrypt(dados)
    with open(saida, 'w') as f:
        f.write(cifrado)


def descriptografar(entrada, saida, alg, senha):
    with open(entrada, 'r') as f:
        dados = f.read()
    alg_obj = alg.new(senha, alg.MODE_ECB)
    decifrado = alg_obj.decrypt(dados)
    with open(saida, 'w') as f:
        f.write(decifrado)


if __name__ == '__main__':
    main()
