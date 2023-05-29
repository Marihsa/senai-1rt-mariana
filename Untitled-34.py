while True:
    numero = int(input("Digite um número (ou um valor negativo para sair): "))
    
    if numero < 0:
        print("Programa encerrado.")
        break
    
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
