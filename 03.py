#Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

nome = input("Digite seu nome")
tamanho = len(nome)
parada_i = tamanho + 1

for i in nome[0:parada_i +1]:
    print(i,"\n")

