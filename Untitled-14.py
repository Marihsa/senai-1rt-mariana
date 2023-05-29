def encontrar_maior_menor(valor1, valor2, valor3):
    maior = max(valor1, valor2, valor3)
    menor = min(valor1, valor2, valor3)
    return maior, menor

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

maior, menor = encontrar_maior_menor(valor1, valor2, valor3)

print("O maior valor digitado é:", maior)
print("O menor valor digitado é:", menor)
