class Pessoa:
    def __init__(self, nome: str)-> None:
        self.nome = nome 

    def apresentar(self) -> str:
        return f"Olá, eu sou {self.nome}."
    
class Aluno(Pessoa):
    def __init__(self, nome = None, matricula = None) -> None:
        if nome is None:
            nome = input("Digite o nome do Aluno: ")
        if disciplina is None:
            disciplina = input("Digite a matricula do aluno: ")
        super().__init__(nome)
        self.matricula = matricula

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e sou aluno, matricula {self.matricula}."                                          
    
class Professor(Aluno):
    def __init__(self, nome = None, disciplina = None, matricula = None):
        if nome is None:
            nome = input("Digite o nome do professor: ")
        if disciplina is None:
            disciplina = input("Digite a disciplina do professor: ")
        if matricula is None:
            matricula = int(input("Digite a matricula do professor: "))
        super().__init__(nome, matricula)
        self.disciplina = disciplina

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"Professor {self.nome} de {self.disciplina}."


p= Pessoa("Gilberto")
a= Aluno()
pr= Professor()    
print(p.apresentar())
print(a.apresentar())   
print(pr.apresentar())
    
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
  
