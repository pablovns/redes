#!/bin/bash

#teste algoritmo md5
for ARQ in 'arq.txt' 'arq2.txt'
do
	python3 hashes.py -a md5 -f $ARQ > saida_py.txt
	md5sum $ARQ | awk '{print $1}' > saida_sh.txt

	#Compara a diferenca nas saidas
	if diff saida_py.txt saida_sh.txt
	then
		echo "Resultado ok para arquivo $ARQ "
		
	else	
		echo "Erro para arquico $ARQ "
	fi
	#Remove arquivos temporarios
	rm saida_py.txt saida_sh.txt
done
