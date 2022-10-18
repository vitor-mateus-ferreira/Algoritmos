"""
print("Matéria nova!")

# Modo:
# r - leitura (read)
# w - escrita (write): acrescenta dados a partir de criação de novo arquivo
# a - escrita (append): acrescenta dados mantendo os dados originais que o arquivo já possui.

arq = open("C:/Users/Aluno/Desktop/dados.txt", "r")

print("Nome: ", arq.name)
print("Modo: ", arq.mode)
print("Fechado ? ", arq.closed)

arq.close()
print("Fechado ? ", arq.closed) 

conteudo = arq.readline() # ler uma linha singular
print(conteudo)

conteudo = arq.readlines() # transforma o arquivo em um vetor
print(conteudo)


# Transformando a string em int
arq = open("C:/Users/Aluno/Desktop/dados.txt", "r")

conteudo = arq.readlines() # transforma o arquivo em um vetor
print(conteudo)

for i in range(0, len(conteudo)):
    nome = int(conteudo[i])
    print(nome)

arq.close() 
""" 

# Maior valor, média, números pares

import random

while(True):
    print("1 - Mostrar números")
    print("2 - Mostrar relatório")
    print("3 - Inserir número aleatório")
    print("4 - Inserir número (usuário)")
    print("5 - Sair")
    opc = int(input("Opção: "))

    if(opc == 1):
        arq = open("dados.txt", "r")
        conteudo = arq.readlines()

        for i in range(0, len(conteudo)):
            nome = int(conteudo[i])
            print(nome)

        arq.close()

    elif(opc == 2):

        arq = open("dados.txt", "r")

        conteudo = arq.readlines()
        # ["10", "14", "19", "11"]
        #   0      1     2     3

        maior = int(conteudo[0])
        soma = 0
        pares = 0

        for i in range(0, len(conteudo)):

            num = int(conteudo[i])
            # Soma para média
            soma += num
            # Verificar se é par
            if(num % 2 == 0):
                pares += 1
            # Verificar se é maior
            if(num > maior):
                maior = num

        print("Pares:", pares)
        print("Média:", soma/(len(conteudo)))
        print("Maior:", maior)
        print("Números:", len(conteudo))

        arq.close()

    elif(opc == 3):
        print("Gerando gerando número e armazenando...")

        n = random.randint(1, 100)
        nome = "dados.txt"
        modo = "a"
        arq = open(nome, modo)
        arq.write(str(n) + "\n")
        arq.close()

    elif(opc == 4):
        
        novo_num = int(input("digite o valor númerico: "))
        nome = "dados.txt"
        modo = "a"
        arq = open(nome, modo)
        arq.write(str(novo_num) + "\n")
        arq.close()

    elif(opc == 5):
        print("Saindo...")
        break
    else:
        print("Opção inválida!")

    