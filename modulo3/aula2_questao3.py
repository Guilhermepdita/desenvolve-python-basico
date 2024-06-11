#Entrada
idade = int(input('Digite sua idade: '))
jogou = input('Já jogou pelo menos 3 jogos de tabuleiro? ')
venceu = int(input('Quantos jogos já venceu? '))

#Processamento
#A - tiver entre 16 e 18 anos
#B - já tiver jogado pelo menos 3 jogos
#C - já ter vencido pelo menos 1 jogo 

a = idade > 15 and idade <= 18
b = True or False
if jogou == "sim":
    b = True
else:
    b = False
c = venceu >= 1

apto = a and b and c
#Saída
print(a, b, c)
print(f'Apto para ingressar no clube de jogos de tabuleiro: {apto}')