from Crypto.Hash import MD5, SHA224, SHA256, SHA512
import argparse


hashes = {
    "md5": MD5, 
    "sha224": SHA224, 
    "sha256": SHA256, 
    "sha512": SHA512
}

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--alg', type=str, help="Algoritmo hash.", choices=['md5', 'sha224', 'sha256', 'sha512'])
parser.add_argument('-f', '--file', type=str, help="Nome do arquivo.")
args = parser.parse_args()

if args.file:
    with open(args.file, 'r') as f:
        print(hashes[args.alg].new(data=f.read().encode()).hexdigest())
