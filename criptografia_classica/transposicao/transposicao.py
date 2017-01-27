from itertools import zip_longest
from math import ceil

original = open('transposicao.txt', 'rb').read()

class Transposicao:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def criptografar(self, arquivo, tamanho=None):
        if tamanho is None:
            tamanho = self.tamanho
        linhas = []
        #quebra as informações de tamanho K, ex: k=2 d='teste um' 'te' 'st' 'te' ' u' 'm '
        for i in range(0, len(arquivo), tamanho):
            linhas.append(arquivo[i:i+tamanho])
        #'ABCD', 'xy' --> Ax By C0 D0
        intercalacao = zip_longest(*linhas, fillvalue=0)
        return bytes(sum(intercalacao, ()))

    def descriptografar(self, arquivo, tamanho=None):
        if tamanho is None:
            tamanho = self.tamanho
        #calcula a largura da matriz
        kd = ceil(len(arquivo) / tamanho)
        return self.criptografar(arquivo, kd)

transposicao = Transposicao(7)

criptografado = transposicao.criptografar(original)
open('criptografado_transposicao', 'wb').write(criptografado)
#print(criptografado)

descriptografado = transposicao.descriptografar(criptografado)
open('descriptografado_transposicao', 'wb').write(descriptografado)
#print(descriptografado)
