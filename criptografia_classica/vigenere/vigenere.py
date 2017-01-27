from itertools import cycle


class Vigenere:
    def __init__(self, chave):
        self.chave = chave

    def criptografar(self, arquivo, chave=None):
        if chave is None:
            chave = self.chave
        return bytes((b + a) % 256 for (a, b) in zip(cycle(chave), arquivo))

    def descriptografar(self, arquivo, chave=None):
        if chave is None:
            chave = self.chave
        return self.criptografar(arquivo, [-ki for ki in chave])

arq_original = open('vegenere.txt', 'rb').read()
#Converte chave para bytes
chave = str('chave para criptografar substituir por outra mais segura!!! :)').encode()
vigenere = Vigenere(chave)

arq_criptografado = vigenere.criptografar(arq_original)
arq_descriptografado = vigenere.descriptografar(arq_criptografado)

print(arq_criptografado)
print(arq_descriptografado)

#Grava em arquivo
open('criptografado_vigenere', 'xb').write(arq_criptografado)
open('descriptografado_vigenere', 'x').write(arq_descriptografado.decode())
