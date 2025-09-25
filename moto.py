class moto:
    def __init__(self, marca, ano, cor, modelo):
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
    def acelerar(self, valor1):
        self.velocidade += valor1
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.modelo} aumentou a velocidade para {self.velocidade} km/h")
        
    def diminuir(self, valor1):
        self.velocidade -= valor1
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.modelo} reduziu a velocidade para {self.velocidade} km/h.")
        
        
moto1 = Moto("Bmw",2023,"Preto","1200 Gs")
moto2 = Moto("Honda",2020,"Vermelho","1200 Gs")