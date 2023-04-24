import requests
import PySimpleGUI as sg
import json
sg.theme('Reddit')

def janela_1():
    layout = [
    [sg.T('Valor em real:')],
    [sg.Input(k='valor')],
    [sg.Push(),sg.Button('Converter'),sg.Push()]
    ]
    return sg.Window('Conversor', layout=layout, finalize=True)

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes_dic = cotacoes.json()
cotacao_dolar = float(cotacoes_dic['USDBRL']['bid'])
print('')
print(cotacoes_dic)
print('')
print(cotacao_dolar)
print('')

janela1=janela_1()

valor=0


while True:
    
    janela,evento,valor = sg.read_all_windows()
    
    # FECHAR O JOGO
    
    if evento == sg.WIN_CLOSED:
        janela.close()
        break
    if evento == 'Converter':
        valor = int(valor['valor'])
        dolar = float(valor/cotacao_dolar)
        sg.popup(f'R$ {valor:.2f} é o equivalente a US$ {dolar:.2f}')
            
        #dolar = float(cotacao_dolar*valor)
        #sg.popup(f'{valor} em dolar é: US$ {dolar:.2f}')