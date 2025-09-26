class Moto:
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
        
    def detalhes(self):
         return (f"{self.marca} {self.modelo} ({self.ano}) - "
                f"Cor: {self.cor}, Velocidade: {self.velocidade} km/h")
 
    
    
    
moto1 = Moto("Bmw", "1200 GS", 2024, "Azul e prata")
moto2 = Moto("Honda", "160 Fan", 2018, "Branca")   
print(moto1.detalhes())
print(moto2.detalhes())
moto1.acelerar(35)
moto2.acelerar(49)
moto1.diminuir(17)
moto2.diminuir(12)
print(moto1.detalhes())
print(moto2.detalhes())     
        
