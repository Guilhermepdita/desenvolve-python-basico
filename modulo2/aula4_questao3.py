#Entrada de dados
nome1 = input('Digite o nome do produto 1: ')
preco_unitario1 = float(input('Digite o preço unitário do produto 1: '))
quantidade1 = int(input('Digite a quantidade do produto 1: '))
preco_total1 = preco_unitario1 * quantidade1

nome2 = input('Digite o nome do produto 2: ')
preco_unitario2 = float(input('Digite o preço unitário do produto 2: '))
quantidade2 = int(input('Digite a quantidade do produto 2: '))
preco_total2 = preco_unitario2 * quantidade2

nome3 = input('Digite o nome do produto 3: ')
preco_unitario3 = float(input('Digite o preço unitário do produto 3: '))
quantidade3 = int(input('Digite a quantidade do produto 3: '))
preco_total3 = preco_unitario3 * quantidade3

#Processamento
preco_total_compra = preco_total1 + preco_total2 + preco_total3

#Saída
print(f'Total: R${preco_total_compra:,.2f}')