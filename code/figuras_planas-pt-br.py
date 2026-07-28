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
       apenas_valor = float(valor)*1000
    elif unidade_de_medida == "hm":
        apenas_valor = float(valor)*100
    elif unidade_de_medida == "dam":
        apenas_valor = float(valor)*10
    elif unidade_de_medida == "dm":
        apenas_valor = float(valor)/10
    elif unidade_de_medida == "cm":
        apenas_valor = float(valor)/100
    elif unidade_de_medida == "mm":
        apenas_valor = float(valor)/1000
    else:
        pass
    return apenas_valor
# Essa função converte o resultado para a unidade de medida que o usuário deseja
def unidade_que_usuario_deseja(medida):
    if unidade_que_usuario_deseja == "km":
        formula = float(medida)/1000
    elif unidade_que_usuario_deseja == "hm":
        formula = float(medida)/100
    elif unidade_que_usuario_deseja == "dam":
        formula = float(medida)/10
    elif unidade_que_usuario_deseja == "dm":
        formula = float(medida)*10
    elif unidade_que_usuario_deseja == "cm":
        formula = float(medida)*100
    elif unidade_que_usuario_deseja == "mm":
        formula = float(medida)*1000
    else:
        pass
    return formula
try:
    while True:
        if figura_limpa == "FIM":
            break
        elif figura_limpa in base_altura:
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
                    formula = float(apenas_valor*apenas_valor_2)
                elif figura_limpa == "TRIANGULO":
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
                apenas_valor = conversor_de_unidades(apenas_valor)
                formula = (apenas_valor**2)*pi
            else:
                medida_1 = input("Digite o valor da diagonal maior: ")
                apenas_valor, unidade_de_medida = medida_1.split()
                apenas_valor = conversor_de_unidades(apenas_valor)
                medida_2 = input("Digite o valor da diagonal menor: ")
                apenas_valor_2, unidade_de_medida = medida_2.split()
                apenas_valor_2 = conversor_de_unidades(apenas_valor_2)
                formula = (float(apenas_valor)*float(apenas_valor_2))/2

        elif figura_limpa in gono:
            if figura_limpa == "PENTAGONO":
                medida_1 = input("Digite o valor da apótema(se não souber digite NAO): ")
                apenas_valor, unidade_de_medida = medida_1.split()
                apenas_valor = conversor_de_unidades(apenas_valor)
                medida_2 = input("Digite o perimetro(se não souber digite NAO): ")
                apenas_valor_2, unidade_de_medida = medida_2.split()
                apenas_valor_2 = conversor_de_unidades(apenas_valor_2)
                formula = (float(apenas_valor)*float(apenas_valor_2))/2
            else:
                lado = input("Digite o valor do lado do hexágono: ")
                apenas_valor, unidade_de_medida = lado.split()       
                apenas_valor = conversor_de_unidades(float(apenas_valor))
                raiz_3 = 3**(0.5)
                formula = (3*(apenas_valor**2)*raiz_3)/2
        qual_unidade = input("Qual a unidade de medida que você deseja o cálculo da área da figura(coloque apeanas a abreviação): ")
        print(f"o Valor da área do {qual_figura} é {formula:.2f} {qual_unidade}²")
        
except:
    print("A figura desejada não está registrada! Por favor tente uma figura registrada que são: ")
    for registrada in base_altura:
        print(registrada)
    for tem_essas in gono:
        print(tem_essas)
    for apenas_essas in diferentes:
        print(apenas_essas)