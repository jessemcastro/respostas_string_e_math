#Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo
# delas seguido do seu comprimento. Informe também se as duas strings possuem
# o mesmo comprimento e são iguais ou diferentes no conteúdo.
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.


letra1 = ''
letra2 = ''

letra1 = input("Digite uma frase")
letra2 = input("Digite outra frase")
tamanho_letra1 = len(letra1)
tamanho_letra2 = len(letra2)

print(letra1,"\n tamanho:",tamanho_letra1)
print(letra2,"\n tamanho:",tamanho_letra2)

if tamanho_letra1 == tamanho_letra2:
    print("As string tem o mesmo tamanho")
else:
    print("As strings não tem o mesmo tamanho")

if letra1 == letra2:
    print("As strings são iguais")
else:
    print("As string são diferentes")
