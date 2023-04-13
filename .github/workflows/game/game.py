import PySimpleGUI as sg
from time import sleep
sg.theme('Reddit')
'''
def janela_0():
    layout = [
        [sg.Push(), sg.Text('TEXTO', pad=(27.5,27.5,3.5,3.5),size=(55,0)), sg.Push()],
        [sg.Push(),sg.Text('O que deseja fazer?',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(), sg.Button('OPÇÃO 1',size=(15,2)), sg.Push(),sg.Button('OPÇÃO 2',size=(15,2)), sg.Push(), sg.Button('Inventário',size=(15,2)), sg.Push()]
    ]
    return sg.Window('RPG', layout=layout, finalize=True)
'''
nome = ''
clas = ''

#CLASSE
class Classe():
    def __init__(self,pow,dex,con,int,wis,cha):
        self.pow = pow
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
    def atributos(self):
        print(self.pow)
        print(self.dex)
        print(self.con)
        print(self.int)
        print(self.wis)
        print(self.cha)
    

#LAYOUT DAS JANELAS
def janela_1():
    layout=[
        [],
        [sg.Push(), sg.Text('Preparado para sua aventura?'),sg.Push()],
        [],
        [sg.Push(), sg.Button('Sim'),sg.Push(), sg.Button('Não'), sg.Push()],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_2():
    layout=[
        [],
        [sg.Text('Qual seu nome?')],
        [sg.Input('',size=(50,7), key='nome')],
        [],
        [sg.Push(), sg.Button('Continuar'), sg.Push()],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_3():
    layout = [
        [],
        [sg.Text('Escolha uma classe:')],
        [],
        [sg.Button('Guerreiro',size=(7,1)),sg.Button('Mago',size=(7,1))],
        [sg.Button('Ladino',size=(7,1)),sg.Button('Clérigo',size=(7,1))]
    ]
    return sg.Window('RPG', layout=layout, finalize=True)


def janela_4():
    layout=[

        [sg.Text(f'A guerra entre os viashinos e os homens durava décadas, o rei Lorestes prometeu rios de ouro pra quem trouxesse a cabeça do rei viashiano, inúmeros mercenários tentaram se aproximar da pirâmide, porém todos falharam. Você e seu grupo de aventureiros planejava uma invasão à pirâmide mas foram emboscados, e agora só você {nome} o grande {clas}, pode salvá-los de um destino miserável.',size=(55,7))],
        [],
        [sg.Push(), sg.Button('Continuar'), sg.Push()],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_5():
    layout=[
        
        [sg.Push(), sg.Text('Após a emboscada, você e seu grupo foram separados, você acorda numa pequena câmara dentro da pirâmide, há um alçapão no teto e apenas uma saída que da para um corredor, você nota na parade diversos hierógrifos.', pad=(27.5,27.5,3.5,3.5),size=(55,0)), sg.Push()],
        [sg.Push(),sg.Text('O que deseja fazer?',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(), sg.Button('Investigar a parede',size=(15,2)), sg.Push(),sg.Button('Ir pro corredor',size=(15,2)), sg.Push(), sg.Button('Inventário',size=(15,2)), sg.Push()],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_6():
    layout = [
        [sg.Push(), sg.Text('Você anda até a saída e observa que além de ser um corredor extenso está cheio de ossos humanos, porém há uma pilha que se destaca.', pad=(27.5,27.5,3.5,3.5),size=(55,0)), sg.Push()],
        [sg.Push(),sg.Text('O que deseja fazer?',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(), sg.Button('Olhar a pilha',size=(15,2)), sg.Push(),sg.Button('Continuar andando',size=(15,2)), sg.Push(), sg.Button('Inventário',size=(15,2)), sg.Push()]
    ]
    return sg.Window('RPG', layout=layout, finalize=True)


#CRIAÇÃO DE JANELAS
janela1 = janela_1()
janela2 = None
janela3 = None
janela4 = None
janela5 = None
janela6 = None

#LOOP DE LEITURA DOS EVENTOS
while True:
    
    janela,evento,valor = sg.read_all_windows()
    
    # FECHAR O JOGO
    
    if evento == sg.WIN_CLOSED:
        janela.close()
        break
    
    #INVENTARIO
    
    if evento == 'Inventário':
        sg.popup('Inventário')
    
    #PRÉ MENU
    
    if janela == janela1 and evento == 'Sim':
        janela2 = janela_2()
        janela2.un_hide()
        janela1.hide()
    elif janela == janela1 and evento == 'Não':
        sg.popup('Volte quando estiver pronto')
        janela.close()
        break
    
    #TELA DE REGISTRO DE NOME
    
    if janela == janela2 and evento == 'Continuar':
        nome = janela2['nome'].get()
        janela3 =janela_3()
        janela2.hide()
        
    #TELA DE REGISTRO DE CLASSE
    
    if janela == janela3 and evento == 'Guerreiro':
        classe = Classe(4,0,4,3,1,2)
        clas = 'guerreiro'
        janela4 = janela_4()
        janela3.hide()
        
    if janela == janela3 and evento == 'Mago':
        classe = Classe(0,3,2,4,4,1)
        clas = 'mago'
        janela4 = janela_4()
        janela3.hide()
        
    if janela == janela3 and evento == 'Ladino':
        classe = Classe(1,4,0,3,2,4)
        clas = 'ladino'
        janela4 = janela_4()
        janela3.hide()
        
    if janela == janela3 and evento == 'Clérigo':
        classe = Classe(0,1,2,3,4,4)
        clas = 'clérigo'
        janela4 = janela_4()
        janela3.hide()
    
    #INTRODUÇÃO 

    if janela == janela4 and evento == 'Continuar':
        janela5 = janela_5()
        janela4.hide()
    
    #
    
    if janela == janela5:
        if evento == 'Investigar a parede':
            popup = sg.Window('RPG', [[sg.T('Os hierógrifos te mostram: Viashinos devorando humanos ainda vivos!')], [sg.Push(),sg.Yes(s=10, button_text='OK' ),sg.Push()]], disable_close=True).read(close=True)
            pass
        if evento == 'Ir pro corredor':
            janela6 = janela_6()
            janela5.hide()

            