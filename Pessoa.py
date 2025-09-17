class SerVivo:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        
class Pessoa(SerVivo):
    
    def andar(self):
        print(f"{self.nome} está andando")
    def estudar(self):
        print(f"{self.nome} está estudando")
    def dormir(self):
        print(f"{self.nome} está dormindo")
    def idad(self):
        print(f"{self.nome} tem {self.idade} anos")
        
jv = Pessoa("João Vitor",16)
jv.estudar()
jv.andar()
jv.dormir()
jv.idad()
    