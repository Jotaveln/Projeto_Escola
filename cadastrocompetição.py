def menu():
    cpf = input("\nDigite seu cpf: ")
    if len(cpf) < 11:
            print("Cpf invalido!")

    else:
        print("Seu cpf é valido!") 
    nome = input("\nDigite seu nome: ")
    idade = int(input("\nDigite sua idade: "))
    endereco = input("\nDigite seu endereço: ")
    numero = int(input("\nDigite seu número de whatsapp: "))
           
def escola():
    funcao = int(input("\nDigite 1 - Professor "
                   "\nDigite 2 - Aluno "))
    if funcao == 1:
        professor = int(input("Você deseja colocar as notas do aluno no sistema?"
                          "\n1 - sim "
                          "\n2 - não "))
    if funcao == 2:
        aluno = int(input("Você deseja descobrir sua nota?"
                          "\n 1 - sim"
                          "\n 2 - não"))
    if aluno == 1:
        n1 = int(input("Digite sua nota do 1° Bimestre: "))
        n2 = int(input("Digite sua nota do 2° Bimestre: "))
        n3 = int(input("Digite sua nota do 3° Bimestre: "))
        n4 = int(input("Digite sua nota do 4° Bimestre: "))
    
        notas = (n1+n2+n3+n4)/4
        print("Sua nota foi: ", notas)
        if notas >= 7:
            print("Você foi aprovado!")
        if notas < 7 or notas >= 5:
            print("Você está de recuperação, porém ainda pode passar com uma prova.")
        if notas < 5:
            print("Você está reprovado!")
            
        exit()
    
    if aluno == 2:
        print("Tenha um otimo dia de aula!")
        exit()
    
    if professor == 2:
        print("OK, tenha um otimo dia!")  
        exit()   
  
    if professor == 1:
        n1 = int(input("Digite a nota do 1° Bimestre: "))
        n2 = int(input("Digite a nota do 2° Bimestre: "))
        n3 = int(input("Digite a nota do 3° Bimestre: "))
        n4 = int(input("Digite a nota do 4° Bimestre: "))
        notas = (n1+n2+n3+n4)/4
        print("A média do seu aluno foi: ",notas)
        exit()
        
def secretaria():
    fazer = int(input("Oque você deseja fazer na secretaria:"
                      "\n1 - Pegar agenda de sala"
                      "\n2 - Imprimir atividade"
                      "\n3 - Imprimir declaração"))
    if fazer == 1:
        curso = int(input("Qual é o seu curso?"
                          "\n1 - Administração"
                          "\n2 - Desenvolvimento de sistemas"
                          "\n3 - Finanças"
                          "\n4 - Enfermagem"))
        
        print("Pegue a da sua sala embaixo da bancada.")
    
    if fazer == 2:
        atvd = int(input("Deseja imprimir uma atividade de qual matéria?"
                         "\n1 - Português"
                         "\n2 - Matemática"
                         "\n3 - Inglês"
                         "\n4 - Historia"
                         "\n5 - Química"
                         "\n6 - Biologia"
                         "\n7 - Física"
                         "\n8 - Geografia"
                         "\n9 - Filosofia"
                         "\n10 - Sociologia"
                         "\n11 - Técnico" ))
        print("Pegue sua atividade na impressora.")
        
    if fazer == 3:
        print("Sua declaração está impressa")
        

def cozinha():
    cardapio = int(input("Oque deseja ver?"
                         "\n1 - Ordem de chamada"
                         "\n2 - Cardapio"))
    if cardapio == 1:
        print("SEGUNDA      | TERÇA   | QUARTA | QUINTA   |  SEXTA"
              "\nAdministração|Finanças |Ds      |Enfermagem|Aleatório"   )

    if cardapio == 2:
        print("SEGUNDA      | TERÇA       | QUARTA | QUINTA   |  SEXTA"
              "\nBaião de dois|Arroz        |Cuscuz  |Strogonoff|Feijoada"
              "\nFrango assado|Carne cozida |Ovo     |Bruaca    |Tapioca")
        
def quadra():
    saber = int(input("Oque deseja saber?"
                      "\n1 - Horario dos intervalos"
                      "\n2 - Qual esporte está sendo praticado"
                      "\n3 - Horarios disponiveis para usar a quadra"))
    
    if saber == 1:
            print("SEGUNDA      | TERÇA   | QUARTA | QUINTA   |  SEXTA"
              "\nAdministração|Finanças |Ds      |Enfermagem|Aleatório"   )
        
#menu()
#escola()
#secretaria()
#cozinha()
#quadra()


