from PySimpleGUI import *

# Atribui as propriedades da janela
# Nome, tamnho e widgets
# A janela do PSG é uma matriz de widgets, com linhas e colunas

# Cada lista do layout é uma linha
layout = [
    [Text('Aperte a porra do botão seu merda')], #linha 1
    [Button('Botão 1'), Button('Botão 2')] #linha 2
]

janela = Window('PSG',layout=layout)



# Lê os eventos da janela
janela.read()

# Fecha a janela
janela.close()