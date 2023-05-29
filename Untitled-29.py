numero = int(input("Digite um número para ver a tabuada: "))

print("Tabuada do", numero)
for cont in range(1, 11):
    resultado = numero * cont
    print(numero, "x", cont, "=", resultado)
