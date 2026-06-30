import unicodedata
qual_figura = input("Digite qual a figura que você deseja calcular a área: ")
figura_limpa = unicodedata.normalize('NFKD', qual_figura).encode('ASCII', 'ignore').decode('ASCII').upper()
base_altura = ["RETANGULO", "QUADRADO", "PARALELOGRAMO", "TRIANGULO","TRAPEZIO"]
diferentes = ["LOSANGO", "CIRCULO"]
gono = ["PENTAGONO", "HEXAGONO"]
if figura_limpa in base_altura:
    base = float(input("Digite o valor da base da figura(se for um trapézio, digite a base maior): "))
    altura = float(input("Digite o valor da altura da figura(se for um quadrado repita o valor da base): "))
    if base<=0 or altura<=0:
        print("Os valores de base ou altura não podem ser negativos")
    else:
        if figura_limpa == "RETANGULO" or figura_limpa == "PARALELOGRAMO" or figura_limpa== "QUADRADO":
            formula = (base*altura)
            print(formula)
        elif figura_limpa == "TRIANGULO":
            formula = (base*altura)/2
            print(formula)
        else:
            base_menor = float(input("Digite a base menor: "))
            formula = ((base+base_menor)*altura)/2
            print(formula)
elif figura_limpa in diferentes:
    if figura_limpa == "CIRCULO":
        raio = float(input("Digite qual é o raio da figura"))
        pi = 3.14159
        formula = (raio**2)*pi
        print(formula)
    else:
        diagonal_maior = float(input("Digite o valor da diagonal maior: "))
        diagonal_menor = float(input("Digite o valor da diagonal menor: "))
        formula = (diagonal_maior*diagonal_menor)/2
        print(formula)
elif figura_limpa in gono:
    if figura_limpa == "PENTAGONO":
        apotema = float(input("Digite o valor da apótema(se não souber digite NAO): "))
        perimetro = float(input("Digite o perimetro(se não souber digite NAO): "))
        formula = (apotema*perimetro)/2
        print(formula)
    else:
        lado = float(input("Digite o valor do lado do hexágono: "))
        raiz_3 = 3**(1/2)
        formula = (3*(lado**2)*raiz_3)/2
        print(formula)




