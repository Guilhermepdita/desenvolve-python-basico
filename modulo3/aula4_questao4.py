distancia = float(input("Insira a distância da entrega em km: "))
peso = float(input("Insira o peso do pacote em kg: "))

if distancia <= 100:
    valor_frete = peso * 1
    if peso > 10:
        valor_frete = 10 + peso * 1
if distancia > 100 and distancia <= 300:
    valor_frete = 1.50 * peso
    if peso > 10:
        valor_frete = 10 + 1.50 * peso
if distancia > 300:
    valor_frete = 2 * peso
    if peso > 10:
        valor_frete = 10 + 2 * peso
print(f"O valor do frete é R${valor_frete:.2f}")

#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg