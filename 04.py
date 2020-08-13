#Nome na vertical em escada. Modifique o programa anterior de
# forma a mostrar o nome em formato de escada.

nome = input("Digite seu nome")
tamanho = len(nome)
parada_i = tamanho + 1
nome_parcial = ''
nome2 = ''
cont = 0


for i in nome[0:parada_i +1]:
    cont= cont + 1
    nome2 = nome2 + i
    for j in nome2[cont-1:cont]:
     nome_parcial = nome_parcial + i
    print(nome_parcial)
