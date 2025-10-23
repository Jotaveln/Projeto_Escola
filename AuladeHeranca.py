class Pessoa:
    def __init__(self, nome: str,cpf: int)-> None:
        self.nome = nome 
        self.cpf = cpf

    def apresentar(self) -> str:
        return f"Olá, eu sou {self.nome}. e tenho cpf {self.cpf}."
    
class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: str, cpf: int) -> None:
        super().__init__(nome)
        super().__init__(cpf)
        self.matricula = matricula

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e sou aluno, matricula {self.matricula}."                                          
    
# class Professor(Pessoa):
#     def __init__(self, nome: str, disciplina: str, cpf: int) -> None:
#         super().__init__(nome)
#         super().__init__(cpf)
#         self.disciplina = disciplina

#     def apresentar(self) -> str:
#         return f"Professor {self.nome} de {self.disciplina}."
    
# class BolsaMixin:
#     def calcular_bolsa(self) -> float:
#         return 1200

# class AlunoBolsista(Aluno, BolsaMixin):
#     def apresentar(self) -> str:
#         base = super().apresentar()
#         return f"{base} e recebo bolsa de R${self.calcular_bolsa:.2f} reais."

# def apresentar_todos(pessoas: list[Pessoa]) -> list[str]:
#     return [p.apresentar() for p in pessoas]

# def main() -> None:
#    p =Pessoa("Gilberto", 932438327)
#    a = Aluno("Thiago", "202781",123234298)
#    pr = Professor("Carlos", "Matemática",123233434)
#    ab = AlunoBolsista("Gabriel", "202782", 234523234)

#    resultados = apresentar_todos([p, a, pr, ab])
#    for r in resultados:
#        return r
   
#    print("",
#          f"isintance(ab, Pessoa):{isinstance(ab, Pessoa)}",
#          f"isinstance(ab, Aluno):{isinstance(ab, Aluno)}",
#          f"isinstance(ab, BolsaMixin):{isinstance(ab, BolsaMixin)}",
#          sep="\n")
   
#    print("MRO AlunoBolsista:")
#    for cls in AlunoBolsista.__mro__:
#         print("-",cls.__name__)
    
#    if __name__ == "__main__":
#         main()        
  
