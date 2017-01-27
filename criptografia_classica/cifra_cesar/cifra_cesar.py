
class CifraCesar:
    def __init__(self, chave):
        self.chave = chave

    def criptografar(self, texto, chave=''):
        if chave == '':
            chave = self.chave
        return bytes((letra + chave) % 256 for letra in texto)

    def descriptografar(self, texto, chave=''):
        if chave == '':
            chave = self.chave
        return self.criptografar(texto, chave * -1)


#lendo arquivo à ser criptografado.
arquivo = open('1.input', 'rb').read()

cifraCesar = CifraCesar(5)

#Criptografando arquivo que foi lido
cripto = cifraCesar.criptografar(arquivo)
open('criptografado_cesar', 'wb').write(cripto)

#descriptografando
descripto = cifraCesar.descriptografar(open('criptografado_cesar', 'rb').read())
open('descriptografado_cesar', 'wb').write(descripto)

if arquivo == descripto:
    print("Arquivo original está igual ao cifrado")
else:
    print("Arquivo original está diferente do cifrado")
