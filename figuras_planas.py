import unicodedata
qual_figura = input("Digite qual a figura que você deseja calcular a área: ")
figura_limpa = unicodedata.normalize('NFKD', qual_figura).encode('ASCII', 'ignore').decode('ASCII').upper()
base_altura = ["RETANGULO", "QUADRADO", "PARALELOGRAMO", "TRIANGULO",]
diferentes = ["TRAPEZIO, 'LOSANGO"]
if figura_limpa in base_altura:
    base = float(input("Digite o valor da base da figura: "))
    altura = float(input("Digite o valor da altura da figura(se for um quadrado apenas repita o valor da base): "))
    if base<=0 or altura<=0:
        print("Os valores de base ou altura não podem ser negativos")
    else:
        if figura_limpa == "RETANGULO" or figura_limpa == "PARALELOGRAMO" or figura_limpa== "QUADRADO":
            formula = (base*altura)
            print(formula)