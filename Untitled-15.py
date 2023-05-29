import datetime

def calcular_ano_100_anos(idade):
    ano_atual = datetime.datetime.now().year
    ano_100_anos = ano_atual + (100 - idade)
    return ano_100_anos


idade = int(input("Digite sua idade: "))


ano_100_anos = calcular_ano_100_anos(idade)


print("Você fará 100 anos no ano", ano_100_anos)


