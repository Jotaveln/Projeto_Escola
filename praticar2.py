def carro():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cpf = input("Digite seu cpf: ")
    endereco = input("Digite seu endereço: ")
    numero = int(input("Digite seu número de whatsapp: "))
    
   
    print("\n --- FICHA DE CADASTRO ---")
    print(f"NOME: {nome}")
    print(f"IDADE: {idade}")
    print(f"CPF: {cpf}")
    print(f"ENDEREÇO: {endereco}")
    print(f"NÚMERO: {numero}")
    
    if len(cpf) < 11:
        print("Cpf invalido!")
    else:
        print("Seu cpf é valido!")
    if idade < 18:
        print("Você é menor de idade!")
    else:
        print("Você é maior de idade!")
carro()