def verificar_par(numero1):
    sobra = numero1%2
    if sobra == 0:
        print("Par!")
    else:
        print("ímpar!")

x = int(input("Digite o valor x: "))
verificar_par(x)            