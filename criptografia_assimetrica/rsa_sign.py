import rsa
import argparse

#rsa_sign [-v] [-s] -i ARQ_TO_SIGN -t ARQ_SIGNATURE -k ARQ_KEY

def sign(arq_assinar, arq_assinatura, arq_chave_priv):
    with open(arq_assinar, 'w') as f:
        pass
    # return rsa.sign(message.encode('ascii'), key, 'SHA-1')
  

def check_sign(arq_verificar, arq_assinatura, arq_chave_pub):
    #Código para verificar a assinatura do arquivo aqui
    pass


assinar = False
ARQ_IN = 'file.txt'
ARQ_SIGNATURE = 'signature,'
ARQ_KEY = 'user.pub.key'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--sign',
        help='Assinar',
        action = 'store_true'
        )
    parser.add_argument('-i', '--input',
        help='Arquivo a ser assinado ou verificado',
        type=str,
        required=True
        )
    parser.add_argument('-t', '--signature',
        help='Arquivo de saída, com a assinatura (assinar) ou arquivo de entrada com a assinatura (assinar)',
        type=str,
        )

    parser.add_argument('-k', '--key',
        help='Arquivo com a chave pública (verificar) ou privada (assinar)',
        type=str,
        required=True
        )

    parser.add_argument('-v', '--verbose',
        help='Apresenta informações sobre a operação',
        action='store_true'
        )

    args = parser.parse_args()

    if args.sign:
        assinar = True

    if args.input:
        ARQ_IN = args.input
        ARQ_OUT = f'{ARQ_IN}.out'

    if args.signature:
        ARQ_SIGNATURE = args.output

    if args.key:
        ARQ_KEY = args.key

    if args.verbose:
        print(f'Assinar           : {assinar}')
        print(f'Arquivo entrada   : {ARQ_KEY}')
        print(f'Arquivo assinatura: {ARQ_IN}')
        print(f'Arquivo chave     : {ARQ_SIGNATURE}')

    if assinar:
        ARQ_TO_SIGN = ARQ_IN
        ARQ_PRIVATE_KEY = ARQ_KEY
        sign(ARQ_TO_SIGN, ARQ_SIGNATURE, ARQ_PRIVATE_KEY)
    else:
        ARQ_TO_CHECK= ARQ_IN
        ARQ_PUBLIC_KEY = ARQ_KEY
        check_sign(ARQ_TO_CHECK, ARQ_SIGNATURE, ARQ_PUBLIC_KEY)

