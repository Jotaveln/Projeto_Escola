class Cliente:
    def __init__(self, nome=None, idade=None, endereco=None, numero=None, cpf=None):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.numero = numero
        self.cpf = cpf
    def cadastrar(self):
        self.cpf = input("\nDigite seu cpf: ")
        if len(self.cpf) < 11:
             print("Cpf invalido!")
             exit()

        else:
            print("Seu cpf é valido!") 
        self.nome = input("Digite seu nome: ")
        self.idade = int(input("Digite sua idade: "))
        self.endereco = input("Digite seu endereço: ")
        self.numero = float(input("Digite seu número de whatsapp: "))
        print("Cadastro realizado com sucesso!")

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}, Número: {self.numero}, CPF: {self.cpf}."
class Produto:
    def __init__(self,nome = None, preco = None):
        self.nome = nome
        self.preco = preco
    def cadastrar_produto(self):
        self.nome = input("Digite o nome do produto: ")
        self.preco = float(input("Digite o preço do produto: "))
        print("Produto cadastrado com sucesso!")
    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}."
    
class Alimento(Produto):
    def __init__(self, nome=None, preco=None, validade=None):
        super().__init__(nome, preco)
        self.validade = validade
    def cadastrar_alimento(self):
        self.nome = input("Digite o nome do alimento: ")
        self.preco = float(input("Digite o preço do alimento: "))
        self.validade = float(input("Digite a validade do alimento (DD/MM/AAAA): "))
        print("Alimento cadastrado com sucesso!")
    def __str__(self):
        return f"Alimento: {self.nome}, Preço: R${self.preco:.2f}, Validade: {self.validade}."

class Bebida(Produto):
    def __init__(self, nome=None, preco=None, volume=None):
        super().__init__(nome, preco)
        self.volume = volume
    def cadastrar_bebida(self):
        self.nome = input('Digite o nome da bebida: ')
        self.preco = float(input("Digite o preço da bebida: "))
        self.volume = input("Digite o volume da bebida (ex: 500ml): ")
        print("Bebida cadastrada com sucesso!")
    def __str__(self):
        return f"Bebida: {self.nome}, Preço: R${self.preco:.2f}, Volume: {self.volume}."
    
class Higiene(Produto):
    def __init__(self, nome=None, preco=None, tipo=None):
        super().__init__(nome, preco)
        self.tipo = tipo
    def cadastrar_higiene(self):
        self.nome = input("Digite o nome do produto de higiene: ")
        self.preco = float(input("Digite o preço do produto de higiene: "))
        self.tipo = input("Digite o tipo do produto de higiene (ex: sabonete, shampoo): ")
        print("Produto de higiene cadastrado com sucesso!")
    def __str__(self):
        return f"Produto de Higiene: {self.nome}, Preço: R${self.preco:.2f}, Tipo: {self.tipo}."  
class Limpeza(Produto):
    def __init__(self, nome=None, preco=None, uso=None):
        super().__init__(nome, preco)
        self.uso = uso
    def cadastrar_limpeza(self):
        self.nome = input("Digite o nome do produto de limpeza: ")
        self.preco = float(input("Digite o preço do produto de limpeza: "))
        self.uso = input("Digite o uso do produto de limpeza (ex: multiuso, desinfetante): ")
        print("Produto de limpeza cadastrado com sucesso!")
    def __str__(self):
        return f"Produto de Limpeza: {self.nome}, Preço: R${self.preco:.2f}, Uso: {self.uso}."

while True:
    escolha = int(input("\nDigite 1 - Cadastrar Cliente"
                        "\nDigite 2 - Cadastrar Produto"
                        "\nDigite 3 - Sair do sistema\n"))
    if escolha == 1:
        c = Cliente()
        c.cadastrar()
        print(c)
    elif escolha == 2:
        tipo_produto = int(input("\nDigite 1 - Alimento"
                                 "\nDigite 2 - Bebida"
                                 "\nDigite 3 - Higiene"
                                 "\nDigite 4 - Limpeza\n"))
        if tipo_produto == 1:
            a = Alimento()
            a.cadastrar_alimento()
            print(a)
        elif tipo_produto == 2:
            b = Bebida()
            b.cadastrar_bebida()
            print(b)
        elif tipo_produto == 3:
            h = Higiene()
            h.cadastrar_higiene()
            print(h)
        elif tipo_produto == 4:
            l = Limpeza()
            l.cadastrar_limpeza()
            print(l)
        else:
            print("Opção inválida!")
    elif escolha == 3:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")



# c = Cliente()
# c.cadastrar()
# print(c)
# a = Alimento()
# a.cadastrar_alimento()
# print(a)
# b = Bebida()
# b.cadastrar_bebida()
# print(b)
# h = Higiene()
# h.cadastrar_higiene()
# print(h)
# l = Limpeza()
# l.cadastrar_limpeza()
# print(l)
