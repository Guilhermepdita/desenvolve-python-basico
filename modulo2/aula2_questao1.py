#entrada de dados
#idade juliana
#idade de cris
idade_juliana = int(input("Qual é a idade de Juliana?"))
idade_cris    = int(input("Qual é a idade de Cris?"))

#processamento
#true se ambos forem maior de idade
#<expressão1> = juliana é maior de idade
#<expressão2> = cris é maior de idade
# <expressão1>and<expressão2>
#false em qualquer outro caso.
podem_entrar = idade_juliana >= 18 and idade_cris >= 18

#saída
print(podem_entrar)