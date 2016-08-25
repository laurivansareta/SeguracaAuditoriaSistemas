'''
    :Descrição: Implementar algoritimo diffie Hellman
    p=x^a        (mod N)
    q=x^b        (mod N)
    k=p^b = q^a  (mod N)
'''

class Usuario:
    base = 5
    modulo = 23
    id_usuario = 0
    num_secreto = 0
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario

    def get_chave_secreta(self):
        self.num_secreto = int(input('Usuário: '+ str(self.id_usuario) +', Digite a sua chave secreta:' ))
        return self.num_secreto

    def get_diffie_hellman(self, base, chave_secreta):
        return (base ** chave_secreta) % self.modulo

#cria usuário
alice = Usuario(1)
#pede chave secreta ao usuário
alice.get_chave_secreta()
#aplica o algorítimo
intermedAlice = alice.get_diffie_hellman(alice.base, alice.num_secreto)

bob = Usuario(2)
bob.get_chave_secreta()
intermedBob = bob.get_diffie_hellman(bob.base, bob.num_secreto)

resAlice = alice.get_diffie_hellman(intermedAlice, bob.num_secreto)

resBob = bob.get_diffie_hellman(intermedBob, alice.num_secreto)

print('Chave secreta da alice: ' + str(resAlice))
print('Chave secreta da bob: ' + str(resBob))