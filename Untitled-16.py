nota1 = float( input("Informe a nota1: ") )
nota2 = float( input("Informe a nota2:") ) 
nota3 = float( input("Informe a nota3:") ) 

media = (nota1 + nota2+ nota3) /3

if media >= 6:
    print("Aprovado")
else:
    if media > 5:
        print("Recuperação")
    else:
        print("Reprovado")

print("sua media foi: {:.2f}".format(media))
