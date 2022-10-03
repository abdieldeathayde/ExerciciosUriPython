def ex1():
    print("Alo, mundo!")
#ex1()

def ex2():
    numero = int(input("Digite um número: \n"))
    print(f"O número informado foi:  [{numero}]")
#ex2()

def ex3():
    numero1 = int(input("Digite o primeiro número: \n "))
    numero2 = int(input("Digite o segundo número: \n "))
    soma = numero1 + numero2
    print(f"A soma é {soma}")
#ex3()

def ex4():
    notas = []
    soma = 0
    nota1 = int(input("Digite a nota 1"))
    notas.append(nota1)
    nota2 = int(input("Digite a nota 2: "))
    notas.append(nota2)
    nota3 = int(input("Digite a nota 3: "))
    notas.append(nota3)
    nota4 = int(input("Digite a nota 4: ")) 
    notas.append(nota4)
    
    qtdItens = len(notas)
    
    for i in range(qtdItens):
    
        soma += notas[i]
    media = soma / 4
    
    print(f"A média é: {media}") 
#ex4()