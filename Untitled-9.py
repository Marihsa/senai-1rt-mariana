def converter_para_milimetros(metros):
    milimetros = metros * 1000
    return milimetros

def main():
    metros = float(input("Digite o valor em metros: "))
    milimetros = converter_para_milimetros(metros)
    print(f"{metros} metros equivalem a {metros:.2f} metros e {milimetros:.2f} milímetros.")

if __name__ == "__main__":
    main()