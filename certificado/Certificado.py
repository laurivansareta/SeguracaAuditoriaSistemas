import hashlib
from Crypto.PublicKey import RSA
from Crypto.Util.randpool import RandomPool


arquivo = open('arquivo.txt', 'rb').read()
shaArquivo = hashlib.sha256(arquivo).digest()

#criptografar o sha do arquivo com aes.

# RandomPool do próprio PyCrypto:
pool = RandomPool(384)
pool.stir()

# randfunc(n) deve retornar uma string de dados aleatórios de
# comprimento n, no caso de RandomPool, o método get_bytes
randfunc = pool.get_bytes

# Tamanho da chave, em bits
N = 1024

# Geramos a chave (contendo a chave pública e privada):
key = RSA.generate(N, randfunc)

# Criptografamos o texto com a chave:
enc = key.encrypt(shaArquivo, '')

arquivoAssinado = open('assinado', "wb")
arquivoAssinado.write(enc[0]) #pegar somente o primeiro
arquivoAssinado.close()

certificado = open('certificado', "w")
certificado.write(str(key.n)+'\n')
certificado.write(str(key.e)+'\n')
certificado.close()
