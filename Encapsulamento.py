# class Conta:
#     def __init__(self, saldo = 0):
#         self.__saldo = saldo



#     @property
#     def saldo(self):
#         return self.__saldo
    
#     @saldo.setter
#     def saldo(self, valor):
#         if valor < 0:
#             print("O saldo não pode ser negativo.")
#         else:
#             self.__saldo = valor

#     def depositar(self, valor):
#         if valor > 0:
#             self.__saldo += valor
        
# conta2 = Conta(500)
# print("saldo inicial:", conta2.saldo)

# conta2.saldo = -300
# print("saldo após tentativa de ajuste:", conta2.saldo)

# conta2.depositar(300)
# print("saldo após depósito:", conta2.saldo)                                          
class Produto:
    def __init__(self, preco = 0):
        self.__preco = preco



    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            print("O preço não pode ser negativo.")
        else:
            self.__preco = valor

    def depositar(self, valor):
        if valor > 0:
            self.__preco += valor
        
produto2 = Produto(100)
print("preço inicial:", produto2.preco)

produto2.preco = -50
print("preço após tentativa de ajuste:", produto2.preco)

produto2.depositar(30)
print("preço após depósito:", produto2.preco)                                          