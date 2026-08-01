import unicodedata
which_figure = input("Enter the shape whose area you wish to calculate: ")

# Transforms any text in all caps and without accents
which_figure_uppercase = unicodedata.normalize('NFKD', which_figure).encode('ASCII', 'ignore').decode('ASCII').upper()
base_height = ["RETANGULO", "QUADRADO", "PARALELOGRAMO", "TRIANGULO","TRAPEZIO"]
diferents = ["LOSANGO", "CIRCULO"]
polygons = ["PENTAGONO", "HEXAGONO"]

# This function converts the unity of measurement for meters
def unit_converter(value):
    if unity_of_measure == "km":
       only_value = float(value)*1000
    elif unity_of_measure == "hm":
        only_value = float(value)*100
    elif unity_of_measure == "dam":
        only_value = float(value)*10
    elif unity_of_measure == "dm":
        only_value = float(value)/10
    elif unity_of_measure == "cm":
        only_value = float(value)/100
    elif unity_of_measure == "mm":
        only_value = float(value)/1000
    else:
        pass
    return only_value
# This function converts the results to the unity of measurement that the user wants
def unit_that_the_user_wants(measure):
    if unit_that_the_user_wants == "km":
        formula = float(measure)/1000
    elif unit_that_the_user_wants == "hm":
        formula = float(measure)/100
    elif unit_that_the_user_wants == "dam":
        formula = float(measure)/10
    elif unit_that_the_user_wants == "dm":
        formula = float(measure)*10
    elif unit_that_the_user_wants == "cm":
        formula = float(measure)*100
    elif unit_that_the_user_wants == "mm":
        formula = float(measure)*1000
    else:
        pass
    return formula
try:
    while True:
        if which_figure_uppercase == "FIM":
            break
        elif which_figure_uppercase in base_height:
            measure_1 = input("Digite o value da base da figura(se for um trapézio, digite a base maior): ")
            only_value, unity_of_measure = measure_1.split()
            only_value = float(only_value)
            only_value = unit_converter(only_value)
            measure_2 = input("Digite o valor da altura da figura(se for um quadrado repita o valor da base): ")
            only_value_2, unity_of_measure = measure_2.split()
            only_value_2 = float(only_value_2)
            only_value_2 = unit_converter(only_value_2)
            if only_value<=0 or only_value_2<=0:
                print("Os valores de base ou altura não podem ser negativos")
            else:
                if which_figure_uppercase == "RETANGULO" or which_figure_uppercase == "PARALELOGRAMO" or which_figure_uppercase== "QUADRADO":
                    formula = float(only_value*only_value_2)
                elif which_figure_uppercase == "TRIANGULO":
                    formula = (only_value)*(only_value_2)/2
                else:
                    measure_3 = input("Digite a base menor: ")
                    only_value_3, unity_of_measure = measure_3.split()
                    only_value_3 = unit_converter(only_value_3)
                    formula = ((float(only_value)+float(only_value_3))*float(only_value_2))/2

        elif which_figure_uppercase in diferents:
            if which_figure_uppercase == "CIRCULO":
                measure_1 = input("Digite qual é o raio da figura: ")
                only_value, unity_of_measure = measure_1.split()
                pi = 3.14159
                only_value = unit_converter(only_value)
                formula = (only_value**2)*pi
            else:
                measure_1 = input("Digite o value da diagonal maior: ")
                only_value, unity_of_measure = measure_1.split()
                only_value = unit_converter(only_value)
                measure_2 = input("Digite o value da diagonal menor: ")
                only_value_2, unity_of_measure = measure_2.split()
                only_value_2 = unit_converter(only_value_2)
                formula = (float(only_value)*float(only_value_2))/2

        elif which_figure_uppercase in polygons:
            if which_figure_uppercase == "PENTAGONO":
                measure_1 = input("Digite o value da apótema(se não souber digite NAO): ")
                only_value, unity_of_measure = measure_1.split()
                only_value = unit_converter(only_value)
                measure_2 = input("Digite o perimetro(se não souber digite NAO): ")
                only_value_2, unity_of_measure = measure_2.split()
                only_value_2 = unit_converter(only_value_2)
                formula = (float(only_value)*float(only_value_2))/2
            else:
                lado = input("Digite o value do lado do hexágono: ")
                only_value, unity_of_measure = lado.split()       
                only_value = unit_converter(float(only_value))
                raiz_3 = 3**(0.5)
                formula = (3*(only_value**2)*raiz_3)/2
        qual_unidade = input("Qual a unidade de measure que você deseja o cálculo da área da figura(coloque apeanas a abreviação): ")
        formula = unit_that_the_user_wants(formula)
        print(f"o value da área do {which_figure} é {formula:.2f} {qual_unidade}²")
except:
    print("A figura desejada não está registrada! Por favor tente uma figura registrada que são: ")
    for registrada in base_height:
        print(registrada)
    for tem_essas in polygons:
        print(tem_essas)
    for only_essas in diferents:
        print(only_essas)
