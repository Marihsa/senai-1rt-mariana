distancia = int(input("distancia percorrida em km/s: ") )

if distancia >= 200:
    pagamento = distancia *0.50
    print("O valor da viagem será:",pagamento)
if distancia < 200:
    pagamento1 = distancia *0.45
    print("O valor da viagem será:",pagamento1)    