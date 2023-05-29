velocidade = float(input("Digite a velocidade do carro em km/h: "))

limite = 80
multa = 7

if velocidade > limite:
    velocidade_excedida = velocidade - limite
    valor_multa = velocidade_excedida * multa
    print("Você foi multado!")
    print(f"A velocidade excedida foi de {velocidade_excedida:.2f} km/h")
    print(f"O valor da multa é de R$ {valor_multa:.2f}")
else:
    print("Você está dentro do limite de velocidade. Dirija com segurança!")

