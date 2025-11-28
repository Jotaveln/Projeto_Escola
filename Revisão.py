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
class Vendendor:
    def __init__(self, nome=None, idade=None, endereco=None, numero=None, cpf=None, salario_base=0.0):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.numero = numero
        self.cpf = cpf
        self.salario_base = salario_base
    def cadastrar_vendedor(self):
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
        self.salario_base = float(input("Digite o salário base do vendedor: "))
        print("Vendedor cadastrado com sucesso!")
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}, Número: {self.numero}, CPF: {self.cpf}, Salário Base: R${self.salario_base:.2f}."
    def calcular_comissao(self, total_vendas, percentual_comissao):
        comissao = total_vendas * (percentual_comissao / 100)
        salario_total = self.salario_base + comissao
        return salario_total
    def registrar_venda(self, valor_venda):
        print(f"Venda registrada no valor de R${valor_venda:.2f} por {self.nome}.")
    def conceder_aumento(self, percentual):
        aumento = self.salario_base * (percentual / 100)
        self.salario_base += aumento
        print(f"Salário de {self.nome} aumentado em {percentual}%. Novo salário: R${self.salario_base:.2f}.")
class Gerente:
    def __init__(self, nome=None, idade=None, endereco=None, numero=None, cpf=None, salario_base=0.0):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.numero = numero
        self.cpf = cpf
        self.salario_base = salario_base
    def cadastrar_gerente(self):
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
        self.salario_base = float(input("Digite o salário base do gerente: "))
        print("Gerente cadastrado com sucesso!")
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}, Número: {self.numero}, CPF: {self.cpf}, Salário Base: R${self.salario_base:.2f}."
    def calcular_bonificacao(self, percentual_bonificacao):
        bonificacao = self.salario_base * (percentual_bonificacao / 100)
        salario_total = self.salario_base + bonificacao
        return salario_total
    def registrar_meta(self, meta):
        print(f"Meta de vendas de R${meta:.2f} registrada pelo gerente {self.nome}.")
    def conceder_aumento(self, percentual):
        aumento = self.salario_base * (percentual / 100)
        self.salario_base += aumento
        print(f"Salário de {self.nome} aumentado em {percentual}%. Novo salário: R${self.salario_base:.2f}.")
    def promover_funcionario(self, funcionario, novo_cargo, aumento_percentual):
        funcionario.cargo = novo_cargo
        aumento = funcionario.salario_base * (aumento_percentual / 100)
        funcionario.salario_base += aumento
        print(f"{funcionario.nome} foi promovido para {novo_cargo} com um aumento de {aumento_percentual}%. Novo salário: R${funcionario.salario_base:.2f}.")
    def demitir_funcionario(self, funcionario):
        print(f"{funcionario.nome} foi demitido pelo gerente {self.nome}.")
    def organizar_reuniao(self, assunto):
        print(f"Reunião sobre '{assunto}' organizada pelo gerente {self.nome}.")
class MaquinadeCartão:
    def __init__(self, numero_serie=None, modelo=None, saldo_maquina=0.0):
        self.numero_serie = numero_serie
        self.modelo = modelo
        self.saldo_maquina = saldo_maquina
    def cadastrar_maquina(self):
        self.numero_serie = input("Digite o número de série da máquina: ")
        self.modelo = input("Digite o modelo da máquina: ")
        self.saldo_maquina = float(input("Digite o saldo inicial da máquina: "))
        print("Máquina de cartão cadastrada com sucesso!")
    def __str__(self):
        return f"Máquina de Cartão: Número de Série: {self.numero_serie}, Modelo: {self.modelo}, Saldo: R${self.saldo_maquina:.2f}."
    def processar_pagamento(self, valor_pagamento):
        if valor_pagamento > self.saldo_maquina:
            print("Saldo insuficiente na máquina para processar o pagamento.")
        else:
            self.saldo_maquina -= valor_pagamento
            print(f"Pagamento de R${valor_pagamento:.2f} processado com sucesso.")
    def recarregar_saldo(self, valor_recarregar):
        if valor_recarregar > 0:
            self.saldo_maquina += valor_recarregar
            print(f"Saldo da máquina recarregado em R${valor_recarregar:.2f}. Novo saldo: R${self.saldo_maquina:.2f}.")
    def verificar_saldo(self):
        print(f"Saldo atual da máquina: R${self.saldo_maquina:.2f}.")
    def gerar_relatorio_transacoes(self):
        print("Relatório de transações gerado.")
class Sapato:
    def __init__(self, tamanho=None, cor=None, tipo=None, preco=None):
        self.tamanho = tamanho
        self.cor = cor
        self.tipo = tipo
        self.preco = preco
    def cadastrar_sapato(self):
        self.tamanho = float(input("Digite o tamanho do sapato: "))
        self.cor = input("Digite a cor do sapato: ")
        self.tipo = input("Digite o tipo do sapato (ex: tênis, social, sandália): ")
        self.preco = float(input("Digite o preço do sapato: "))
        print("Sapato cadastrado com sucesso!")
    def __str__(self):
        return f"Sapato: Tamanho {self.tamanho}, Cor: {self.cor}, Tipo: {self.tipo}, Preço: R${self.preco:.2f}."
    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        print(f"Desconto de {percentual}% aplicado. Novo preço: R${self.preco:.2f}.")
    def trocar_cor(self, nova_cor):
        self.cor = nova_cor
        print(f"A cor do sapato foi alterada para {self.cor}.")
    def ajustar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
        print(f"O tamanho do sapato foi ajustado para {self.tamanho}.")
class Camiseta:
    def __init__(self, tamanho=None, cor=None, estilo=None, preco=None):
        self.tamanho = tamanho
        self.cor = cor
        self.estilo = estilo
        self.preco = preco
    def cadastrar_camiseta(self):
        self.tamanho = float(input("Digite o tamanho da camiseta: "))
        self.cor = input("Digite a cor da camiseta: ")
        self.estilo = input("Digite o estilo da camiseta (ex: polo, regata, manga longa): ")
        self.preco = float(input("Digite o preço da camiseta: "))
        print("Camiseta cadastrada com sucesso!")
    def __str__(self):
        return f"Camiseta: Tamanho {self.tamanho}, Cor: {self.cor}, Estilo: {self.estilo}, Preço: R${self.preco:.2f}."
    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        print(f"Desconto de {percentual}% aplicado. Novo preço: R${self.preco:.2f}.")
    def trocar_cor(self, nova_cor):
        self.cor = nova_cor
        print(f"A cor da camiseta foi alterada para {self.cor}.")
    def ajustar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
        print(f"O tamanho da camiseta foi ajustado para {self.tamanho}.")
class Calça:
    def __init__(self, tamanho=None, cor=None, estilo=None, preco=None):
        self.tamanho = tamanho
        self.cor = cor
        self.estilo = estilo
        self.preco = preco
    def cadastrar_calça(self):
        self.tamanho = float(input("Digite o tamanho da calça: "))
        self.cor = input("Digite a cor da calça: ")
        self.estilo = input("Digite o estilo da calça (ex: jeans, social, moletom): ")
        self.preco = float(input("Digite o preço da calça: "))
        print("Calça cadastrada com sucesso!")
    def __str__(self):
        return f"Calça: Tamanho {self.tamanho}, Cor: {self.cor}, Estilo: {self.estilo}, Preço: R${self.preco:.2f}."
    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        print(f"Desconto de {percentual}% aplicado. Novo preço: R${self.preco:.2f}.")
    def trocar_cor(self, nova_cor):
        self.cor = nova_cor
        print(f"A cor da calça foi alterada para {self.cor}.")
    def ajustar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
        print(f"O tamanho da calça foi ajustado para {self.tamanho}.")
while True:
    escolha = int(input("\nDigite 1 - Cadastrar Cliente"
                        "\nDigite 2 - Cadastrar Vendedor"
                        "\nDigite 3 - Cadastrar Gerente"
                        "\nDigite 4 - Cadastrar Máquina de Cartão"
                        "\nDigite 5 - Cadastrar Sapato"
                        "\nDigite 6 - Cadastrar Camiseta"
                        "\nDigite 7 - Cadastrar Calça"
                        "\nDigite 0 - Sair"
                        "\nEscolha uma opção: "))
    if escolha == 1:
        cliente = Cliente()
        cliente.cadastrar()
        print(cliente)
    elif escolha == 2:
        vendedor = Vendendor()
        vendedor.cadastrar_vendedor()
        print(vendedor)
    elif escolha == 3:
        gerente = Gerente()
        gerente.cadastrar_gerente()
        print(gerente)
    elif escolha == 4:
        maquina = MaquinadeCartão()
        maquina.cadastrar_maquina()
        print(maquina)
    elif escolha == 5:
        sapato = Sapato()
        sapato.cadastrar_sapato()
        print(sapato)
    elif escolha == 6:
        camiseta = Camiseta()
        camiseta.cadastrar_camiseta()
        print(camiseta)
    elif escolha == 7:
        calca = Calça()
        calca.cadastrar_calça()
        print(calca)
    elif escolha == 0:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

C = Cliente()
C.cadastrar()
print(C)
V = Vendendor()
V.cadastrar_vendedor()
print(V)
G = Gerente()
G.cadastrar_gerente()
print(G)
M = MaquinadeCartão()
M.cadastrar_maquina()
print(M)
S = Sapato()
S.cadastrar_sapato()
print(S)
Ca = Camiseta()
Ca.cadastrar_camiseta()
print(Ca)
Cal = Calça()
Cal.cadastrar_calça()
print(Cal)