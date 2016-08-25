# encoding: utf-8
import hashlib
from Crypto.PublicKey import RSA

#abre arquivo original e gera o sha256.
arquivo = open('arquivo.txt', 'rb').read()
shaArquivo = hashlib.sha256(arquivo).digest()

#Abre arquivo para posteriormente validar assinatura
arquivoAssinado = open('assinado', 'rb').read()

#abre arquivo certificado.
arquivo = open('certificado', 'r').read()
arquivoSplit = arquivo.splitlines()
n, e = arquivoSplit[0], arquivoSplit[1]

#reconstroi a chave pública e criptografa o sha256 do arquivo original
public_key = RSA.construct((int(n), int(e)))
cripto_pk = public_key.encrypt(shaArquivo, 1024)

#valida se arquivo esta assinado.
if arquivoAssinado == cripto_pk[0]:
    print('arquivo com assinatura digital válida')
else:
    print('arquivo com assinatura digital inválida')
