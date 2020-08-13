#Nome na vertical em escada invertida. Altere o programa
# anterior de modo que a escada seja invertida.

nome = input("Digite seu nome")
tamanho = len(nome)
cont = 0
for i in nome:

    nome2 = nome[0:tamanho-cont]
    cont = cont + 1
    for j in range(0,1):
        print(nome2)



