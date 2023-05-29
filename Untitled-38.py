import time

def regressiva(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1

    print("Contagem regressiva concluída!")

contagem = int(input("Digite um número para a contagem regressiva começar: "))
regressiva(contagem)

