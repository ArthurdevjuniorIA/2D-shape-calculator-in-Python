# 📐 Calculadora Geométrica & Conversor de Unidades

> Aplicação modular em Python para cálculo de áreas de figuras geométricas planas com conversão automática de unidades de medida.

---

## 📌 Sobre o Projeto

A **Calculadora Geométrica** é uma ferramenta desenvolvida em Python para calcular a área de diversas figuras geométricas (retângulos, triângulos, círculos, trapézios, polígonos regulares, entre outros).

O diferencial da aplicação está no **sistema de conversão automática de unidades**, permitindo que o usuário informe as dimensões em diferentes escalas (como `cm`, `km`, `mm`) e obtenha a resposta exata na unidade de área desejada (como `m²`, `cm²`, `km²`).

---

## 🎯 Funcionalidades

* **Suporte a múltiplas figuras geométricas:**
  * **Base & Altura:** Retângulo, Quadrado, Paralelogramo, Triângulo, Trapézio.
  * **Figuras Circulares e Diagonais:** Círculo, Losango.
  * **Polígonos Regulares:** Pentágono, Hexágono.
* **Normalização de Entrada:** Tratamento de texto com `unicodedata` para ignorar acentuação e letras maiúsculas/minúsculas.
* **Conversão de Unidades Integrada:** Entrada em unidades lineares (`km`, `hm`, `dam`, `m`, `dm`, `cm`, `mm`) e saída em unidades de área ajustadas.
* **Arquitetura Modular:** Separação clara entre interface, cálculos geométricos e conversão de medidas.

---

## 📁 Estrutura do Projeto

O projeto foi organizado utilizando o padrão modular para facilitar a manutenção e o reaproveitamento de código:

```text
calculadora-geometrica/
│
├── README.md               # Documentação do projeto
├── .gitignore              # Arquivos ignorados pelo Git
│
├── tests/
│   └── test_fixtures.txt   # Dados e simulações para testes
│
└── src/
    ├── __init__.py         # Identificador do pacote Python
    ├── main.py             # Ponto de entrada e interface com o usuário
    ├── conversores.py      # Módulo com as regras de conversão de unidades
    └── figuras.py          # Módulo com as fórmulas e lógicas geométricas
```
## ⚙️ Como Executar o Projeto
Pré-requisitos
Python 3.8+ instalado na sua máquina.

**Passo a Passo**
1. Clone o repositório
```bash
git clone [https://github.com/seu-usuario/calculadora-geometrica.git](https://github.com/seu-usuario/calculadora-geometrica.git)
```
2. Navegue até a pasta do projeto
```bash
cd calculadora-geometrica
```
3. Executar o arquivo principal
```bash
python src/main.py
```
## 💡 Exemplo de Uso
Digite a figura geométrica cuja área deseja calcular (ou FIM para sair): trapézio

Digite o valor da base da figura (se for um trapézio, digite a base maior): 10 cm

Digite o valor da altura da figura: 5 cm

Digite a base menor: 6 cm

Em qual unidade de medida deseja a área final? (ex: m, cm, km): cm

O valor da área do trapézio é 40.000000 cm²

## 🛠️ Tecnologias Utilizadas
Python 3 — Linguagem principal do projeto.

unicodedata — Módulo nativo para tratamento e remoção de acentos.
## 🚀 Próximas Evoluções Planejadas
[ ] Implementar tratamento de exceções com try/except para entradas inválidas.

[ ] Adicionar suporte a figuras tridimensionais (cálculo de volume).

[ ] Criar testes unitários automatizados com pytest na pasta tests/.

Criado e desenvolvido para ajudar alunos que tem dificuldade em geometria plana.
