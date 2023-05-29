def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def maior_numero(a, b):
    return max(a, b)

def menor_numero(a, b):
    return min(a, b)

def exibir_menu():
    print("Menu:")
    print("a. Somar")
    print("b. Multiplicar")
    print("c. Maior número")
    print("d. Menor número")

def main():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    exibir_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "a":
        resultado = somar(valor1, valor2)
        print("Resultado da soma:", resultado)
    elif opcao == "b":
        resultado = multiplicar(valor1, valor2)
        print("Resultado da multiplicação:", resultado)
    elif opcao == "c":
        resultado = maior_numero(valor1, valor2)
        print("Maior número:", resultado)
    elif opcao == "d":
        resultado = menor_numero(valor1, valor2)
        print("Menor número:", resultado)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()