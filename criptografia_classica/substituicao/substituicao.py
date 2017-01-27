from random import shuffle
from collections import OrderedDict

#Carrega a chave para o dictionary
#key1 = dict(enumerate(open('key1', 'rb').read()))
#Carrega o dictionary para decodificação
#key1_dec = dict((j,i) for (i, j) in key1.items())
#Carrega o arquivo a ser criptografado

nome_chave = 'key1'
nome_arquivo = 'substituicao.txt'


original = open(nome_arquivo, 'rb').read()

class Substituicao:
    def __init__(self, chave):
        try:
            # Carrega a chave para o dictionary
            self.chave = dict(enumerate(open(chave, 'rb').read()))
        except IOError as e:
            #caso não consiga carregar a chave vai criar uma aleatória e gravar.
            tmp = list(range(256))
            shuffle(tmp)
            self.chave = dict(enumerate(tmp))
            open('chave_gerada_automaticamente', 'xb').write(bytes(self.chave.values()))
        finally:
            # Carrega o dictionary para decodificação
            self.chave_dec = dict((j, i) for (i, j) in self.chave.items())

    def criptografar(self,texto):
        return bytes(self.chave[i] for i in texto)

    def descriptografar(self, texto):
        return bytes(self.chave_dec[i] for i in texto)

substituicao = Substituicao(nome_chave)

arq_criptografado = substituicao.criptografar(original)
arq_descriptografado = substituicao.descriptografar(arq_criptografado)

#Grava em arquivo
open('criptografado_substituicao', 'xb').write(arq_criptografado)
open('descriptografado_substituicao', 'x').write(arq_descriptografado.decode())
