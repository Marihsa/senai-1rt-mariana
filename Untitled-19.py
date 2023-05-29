salario = float( input("informe seu salario: ") )

if salario > 8250:
    salario = salario + (salario * 0.10)
    print(f"Parabens aumento de salario: R${salario}😀")

else:
    if salario < 8250:
       salario = salario + (salario * 0.15)
    print(f"aumento de salario de: R${salario}😁")

