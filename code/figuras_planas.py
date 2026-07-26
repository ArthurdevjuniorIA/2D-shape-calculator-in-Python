import unicodedata
qual_figura = input("Digite qual a figura que você deseja calcular a área: ")

# Tranforma qualquer texto em um sem acentos e em caixa alta
figura_limpa = unicodedata.normalize('NFKD', qual_figura).encode('ASCII', 'ignore').decode('ASCII').upper()
base_altura = ["RETANGULO", "QUADRADO", "PARALELOGRAMO", "TRIANGULO","TRAPEZIO"]
diferentes = ["LOSANGO", "CIRCULO"]
gono = ["PENTAGONO", "HEXAGONO"]

# Essa função converte a unidade de medida para metros
def conversor_de_unidades(valor):
    if unidade_de_medida == "km":
       apenas_valor = float(apenas_valor) * 1000
    elif unidade_de_medida == "hm":
        apenas_valor = float(apenas_valor) * 100
    elif unidade_de_medida == "dam":
        apenas_valor = float(apenas_valor) * 10
    elif unidade_de_medida == "dm":
        apenas_valor = float(valor)/10
    elif unidade_de_medida == "cm":
        apenas_valor = float(valor)/100
    elif unidade_de_medida == "mm":
        apenas_valor = float(apenas_valor)/1000
    return unidade_de_medida
if figura_limpa in base_altura:
    medida_1 = input("Digite o valor da base da figura(se for um trapézio, digite a base maior): ")
    apenas_valor, unidade_de_medida = medida_1.split()
    apenas_valor = float(apenas_valor)
    apenas_valor = conversor_de_unidades(apenas_valor)
    medida_2 = input("Digite o valor da altura da figura(se for um quadrado repita o valor da base): ")
    apenas_valor_2, unidade_de_medida = medida_2.split()
    apenas_valor_2 = float(apenas_valor_2)
    apenas_valor_2 = conversor_de_unidades(apenas_valor_2)
    if apenas_valor<=0 or apenas_valor_2<=0:
        print("Os valores de base ou altura não podem ser negativos")
    else:
        if figura_limpa == "RETANGULO" or figura_limpa == "PARALELOGRAMO" or figura_limpa== "QUADRADO":
            apenas_valor = conversor_de_unidades(apenas_valor)
            apenas_valor_2 = conversor_de_unidades(apenas_valor_2)
            formula = float(apenas_valor*apenas_valor_2)
        elif figura_limpa == "TRIANGULO":
            apenas_valor = conversor_de_unidades(apenas_valor)
            apenas_valor_2 = conversor_de_unidades(apenas_valor_2)
            formula = (apenas_valor)*(apenas_valor_2)/2
        else:
            medida_3 = input("Digite a base menor: ")
            apenas_valor_3, unidade_de_medida = medida_3.split()
            apenas_valor_3 = conversor_de_unidades(apenas_valor_3)
            formula = ((float(apenas_valor)+float(apenas_valor_3))*float(apenas_valor_2))/2

elif figura_limpa in diferentes:
    if figura_limpa == "CIRCULO":
        medida_1 = input("Digite qual é o raio da figura: ")
        apenas_valor, unidade_de_medida = medida_1.split()
        pi = 3.14159
        apenas_valor = float(apenas_valor)
        conversor_de_unidades(apenas_valor)
        formula = (apenas_valor**2)*pi
    else:
        medida_1 = input("Digite o valor da diagonal maior: ")
        apenas_valor, unidade_de_medida = medida_1.split()
        apenas_valor = float(apenas_valor)
        conversor_de_unidades(apenas_valor)
        medida_2 = input("Digite o valor da diagonal menor: ")
        apenas_valor_2, unidade_de_medida = medida_2.split()
        apenas_valor_2 = conversor_de_unidades(apenas_valor_2)
        formula = (float(apenas_valor)*float(apenas_valor_2))/2

elif figura_limpa in gono:
    if figura_limpa == "PENTAGONO":
        medida_1 = input("Digite o valor da apótema(se não souber digite NAO): ")
        apenas_valor, unidade_de_medida = medida_1.split()
        apenas_valor = float(apenas_valor)
        conversor_de_unidades(apenas_valor)
        medida_2 = input("Digite o perimetro(se não souber digite NAO): ")
        apenas_valor_2, unidade_de_medida = medida_2.split()
        apenas_valor_2 = float(apenas_valor_2)
        conversor_de_unidades(apenas_valor_2)
        formula = (apenas_valor*apenas_valor_2)/2
    else:
        medida_1 = input("Digite o valor do lado do hexágono: ")
        apenas_valor, unidade_de_medida = medida_1.split()
        apenas_valor = float(apenas_valor)
        conversor_de_unidades(apenas_valor)
        raiz_3 = 3**(1/2)
        formula = (3*(medida_1**2)*raiz_3)/2
print(f"o Valor da área do {qual_figura} é {formula} m²")