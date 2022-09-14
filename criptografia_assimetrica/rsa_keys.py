import argparse
import rsa


def main():
    """Gera chaves"""
    parser = argparse.ArgumentParser()
    
    # valores padrões
    FILE_PRIV = 'privateKey.pem'
    FILE_PUB = 'publicKey.pem'
    KEY_SIZE = 1024

    parser.add_argument('-u', '--user')
    parser.add_argument('-v', '--verbose', action='store_true', help='Mostra informações sobre as chaves.')
    parser.add_argument('-s', '--keysize', required=True, type=int, choices=[1024, 2048, 4096])
    args = parser.parse_args()    
    
    if args.user:
        FILE_PRIV = f'{args.user}_{FILE_PRIV}'
        FILE_PUB = f'{args.user}_{FILE_PUB}'
    
    if args.verbose:
        print(f'Chave pública: {FILE_PUB}')
        print(f'Chave privada: {FILE_PRIV}')
    
    if args.keysize:
        KEY_SIZE = args.keysize
    
    # gera as chaves
    generate_keys(FILE_PUB, FILE_PRIV, KEY_SIZE)


def generate_keys(file_pub, file_priv, key_size):
    (public_key, private_key) = rsa.newkeys(key_size)

    with open(file_pub, 'wb') as p:
        p.write(public_key.save_pkcs1('PEM'))

    with open(file_priv, 'wb') as p:
        p.write(private_key.save_pkcs1('PEM'))


if __name__ == '__main__':
    main()