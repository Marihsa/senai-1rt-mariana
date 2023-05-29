num1 = int(input("Digite um número inteiro: "))

print(f"Tabuada de {num1}:")
for i in range(1, 11):
    resultado = num1 * i
    print(f"{num1} x {i} = {resultado}")