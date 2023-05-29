def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("O fatorial não está definido para números negativos.")
else:
    resultado = calcular_fatorial(numero)
    print("O fatorial de", numero, "é", resultado)
