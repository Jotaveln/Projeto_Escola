class Funcionario:
    def __init__(self, nome, cargo, salario_base, turno = None):
        self.nome = nome
        self.cargo = cargo
        self.salario_base = salario_base
        self.turno = turno
    def cadastrar_funcionario(self):
        self.nome = input("Digite o nome do funcionário: ")
        self.cargo = input("Digite o cargo do funcionário: ")
        self.salario_base = float(input("Digite o salário base do funcionário: "))
        self.turno = input("Digite o turno do funcionário (ex: manhã, tarde, noite): ")
        print("Funcionário cadastrado com sucesso!")
    def __str__(self):
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}, Salário Base: R${self.salario_base:.2f}, Turno: {self.turno}."                                      
        exit()
    def calcular_salario(self, horas_extra = 0):
        valor_hora_extra = (self.salario_base / 160) * 1.5
        salario_total = self.salario_base + (horas_extra * valor_hora_extra)
        return salario_total
    def registrar_ponto(self, horas_trabalhadas):
        print(f"{self.nome} trabalhou {horas_trabalhadas} horas hoje.")
    def conceder_aumento(self, percentual):
        aumento = self.salario_base * (percentual / 100)
        self.salario_base += aumento
        print(f"Salário de {self.nome} aumentado em {percentual}%. Novo salário: R${self.salario_base:.2f}.")

class Garçom(Funcionario):
    def __init__(self, nome=None, cargo="Garçom", salario_base=0.0, turno=None, mesa_atendida=None):
        super().__init__(nome, cargo, salario_base, turno)
        self.mesa_atendida = mesa_atendida
    def calcular_salario(self):
        if self.mesa_atendida is None:
            return self.salario_base
        bonus = self.mesa_atendida * 10
        return self.salario_base + bonus
    def trabalhar(self):
        if self.mesa_atendida is None:
            print(f"{self.nome} está aguardando para atender uma mesa.")
        else:
            print(f"{self.nome} está atendendo a mesa {self.mesa_atendida}.")
    def servir_pedido(self, pedido):
        if pedido is none:
            print(f"{self.nome} não tem pedidos para servir no momento.")
        else:
            print(f"{self.nome} está servindo o pedido: {pedido}.")

class Cozinheiro(Funcionario):
    def __init__(self, nome=None, cargo="Cozinheiro", salario_base=0.0, turno=None, especialidade=None):
        super().__init__(nome, cargo, salario_base, turno)
        self.especialidade = especialidade
    def calcular_salario(self):
        if self.especialidade is None:
            return self.salario_base
        bonus = 200 if self.especialidade == "chef" else 100
        return self.salario_base + bonus
    def trabalhar(self):
        if self.especialidade is None:
            print(f"{self.nome} está cozinhando pratos variados.")
        else:
            print(f"{self.nome}, o {self.especialidade}, está preparando pratos especiais.")
    def preparar_prato(self, prato):
        if prato is None:
            print(f"{self.nome} não tem pratos para preparar no momento.")
        else:
            print(f"{self.nome} está preparando o prato: {prato}.")
    def limpar_cozinha(self):
        print(f"{self.nome} está limpando a cozinha.")

class Gerente(Funcionario):
    def __init__(self, nome , salario_base , turno=None, equipe_supervisionada = None):
        super().__init__(nome, salario_base, turno)
        self.equipe_supervisionada = equipe_supervisionada if equipe_supervisionada is not None else []
    def calcular_salario(self):
        bonus = len(self.equipe_supervisionada) * 300
        return self.salario_base + bonus
    def trabalhar(self):
        print(f"{self.nome} está supervisionando {len(self.equipe_supervisionada)} funcionários.")
    def contratar(self,novo_funcionario = None):
        if novo_funcionario is None:
            print(f"{self.nome} não tem novos funcionários para contratar no momento.")
        else:
            self.equipe_supervisionada.append(novo_funcionario)
            print(f"{self.nome} contratou {novo_funcionario.nome}.")

class LavadorDePratos(Funcionario): 
   






            


    
    
        