import PySimpleGUI as sg
import random
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

#CLASSE
class Classe():
    def __init__(self,pow,dex,con,int,wis,cha):
        self.pow = pow
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.hp = 10 + con 
        self.mana = 10 + int
    def atributos(self):
        print(self.pow)
        print(self.dex)
        print(self.con)
        print(self.int)
        print(self.wis)
        print(self.cha)
        



def d20(scss, atrib):
    d20.sucesso = scss
    d20.d20 = random.randint(1, 20)
    roll = d20.d20 + atrib
    # print(scss, atrib, d20.d20, roll)

    if roll <= 5:
        # print('Fracasso crítico!')
        d20.f_crit = True
        d20.fail = True
    elif roll >= 20:
        # print('Sucesso crítico!')
        d20.s_crit = True
        d20.fail = False
    elif roll >= d20.sucesso:
        # print('Sucesso')
        d20.s_crit = False
        d20.fail = False
    else:
        # print('Fracasso')
        d20.f_crit = False
        d20.fail = True
        
def d4(crit):
    d4.n = random.randint(1, 4)
    d4.n_2 = random.randint(1, 4)
    if crit == False:
        d4.d4 = d4.n
    else:
        d4.d4 = d4.n + d4.n_2
    
    
#VARIAVEIS
historico = []
leng = int(len(historico))

nome = ''
clas = ''

classe = Classe(0,0,0,0,4,0)
pow = classe.pow
dex = classe.dex
con = classe.con
inT = classe.int
wis = classe.wis
cha = classe.cha
hpmax= classe.hp
hp = hpmax
manamax= classe.mana
mana = manamax
dano = 0
porcHP= int((100 * hp) / hpmax)
porcMANA= int((100 * mana) / manamax)


#LAYOUT DAS JANELAS
def inventario():
    layout = [
        [sg.Text(f'Nome:   {nome}',size=(18,0)),sg.T(f'Classe:    {clas}', size=(18,0))],
        [sg.Push(),sg.Text('HP :',size=(6,0)),sg.ProgressBar(100, orientation='h', s=(30, 20), k='hp', ), sg.Push(), sg.Text(f'{hp}/{hpmax}')],
        [sg.Push(),sg.Text('MANA :'),sg.ProgressBar(100, orientation='h', s=(30, 20), k='mana'),sg.Push(), sg.Text(f'{mana}/{manamax}')],
        [
        sg.Push(),
        sg.Listbox(['','',f'        Força: {pow} ','',f'        Agilidade: {dex}','',f'        Constituição: {con}','',f'        Inteligência: {inT}','',f'        Sabedoria: {wis}','',f'        Carisma: {cha}',''], no_scrollbar=True, s=(20, 15)),
        sg.Push(),
         sg.Listbox([''], no_scrollbar=True, s=(20, 15)),
         sg.Push(),
         sg.Listbox([''], no_scrollbar=True, s=(20, 15)),
         sg.Push(),
         ],
        [sg.Push(), sg.Button('Voltar',size=(15,2)), sg.Push()]
    ]   
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_1():
    layout=[
        [],
        [sg.Push(), sg.Text('Preparado para sua aventura?'),sg.Push()],
        [],
        [sg.Push(), sg.Button('Sim',size=(15,2)),sg.Push(), sg.Button('Não',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_2():
    layout=[
        [],
        [sg.Push(), sg.Text('Qual seu nome?'), sg.Push()],
        [sg.Input('',size=(50,7), key='nome')],
        [],
        [sg.Push(), sg.Button('Continuar',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_3():
    layout = [
        [],
        [sg.Push(), sg.Text('Escolha uma classe:'), sg.Push()],
        [],
        [sg.Button('Guerreiro',size=(15,2)),sg.Button('Mago',size=(15,2))],
        [sg.Button('Ladino',size=(15,2)),sg.Button('Clérigo',size=(15,2))],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)


def janela_4():
    layout=[

        [sg.Text(f'A guerra entre os viashinos e os homens durava décadas, o rei Lorestes prometeu rios de ouro pra quem trouxesse a cabeça do rei viashiano, inúmeros mercenários tentaram se aproximar da pirâmide, porém todos falharam. Você e seu grupo de aventureiros planejava uma invasão à pirâmide mas foram emboscados, e agora só você {nome} o grande {clas}, pode salvá-los de um destino miserável.',size=(55,7))],
        [],
        [sg.Push(), sg.Button('Continuar',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_5():
    layout=[
        
        [sg.Push(), sg.Text('Após a emboscada, você e seu grupo foram separados, você acorda numa pequena câmara dentro da pirâmide, há um alçapão no teto e apenas uma saída que da para um corredor, você nota na parade diversos hierógrifos.', pad=(27.5,27.5,3.5,3.5),size=(55,0)), sg.Push()],
        [sg.Push(),sg.Text('O que deseja fazer?',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(), sg.Button('Investigar a parede',size=(15,2)), sg.Push(),sg.Button('Ir pro corredor',size=(15,2)), sg.Push(), sg.Button('Inventário',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_6():
    layout = [
        [sg.Push(), sg.Text('Você anda até a saída e observa que além de ser um corredor extenso está cheio de ossos humanos, porém há uma pilha que se destaca.', pad=(27.5,27.5,3.5,3.5),size=(55,0)), sg.Push()],
        [sg.Push(),sg.Text('O que deseja fazer?',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(), sg.Button('Olhar a pilha',size=(15,2)), sg.Push(),sg.Button('Continuar andando',size=(15,2)), sg.Push(), sg.Button('Inventário',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_7_1():
    layout = [
        [sg.Push(), sg.Text('Você anda pelo corredor, esbarrando em todas as plihas de ossos, até que ouve um barulho de engrenagem, porém a armadilha trava e não ativa!', pad=(27.5,27.5,3.5,3.5),size=(55,0)), sg.Push()],
        [sg.Push(),sg.Text('O que deseja fazer?',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(), sg.Button('OPÇÃO 1',size=(15,2)), sg.Push(),sg.Button('OPÇÃO 2',size=(15,2)), sg.Push(), sg.Button('Inventário',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)

def janela_7_2():
    layout = [
        [sg.Push(), sg.Text('Você anda pelo corredor, esbarrando em todas as plihas de ossos, até que você ouve um barulho de engrenagem, então são disparados diversos dardos ao longo do corredor!', pad=(27.5,27.5,3.5,3.5),size=(55,0)), sg.Push()],
        [sg.Push(),sg.Text(f'Você recebeu {dano} de dano',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(),sg.Text('O que deseja fazer?',pad=(0,0,2,2),size=(0,2)), sg.Push()],
        [sg.Push(), sg.Button('OPÇÃO 1',size=(15,2)), sg.Push(),sg.Button('OPÇÃO 2',size=(15,2)), sg.Push(), sg.Button('Inventário',size=(15,2)), sg.Push()],
        [],
    ]
    return sg.Window('RPG', layout=layout, finalize=True)


#CRIAÇÃO DE JANELAS
invent = None
janelax=None
janela1 = None
janela2 = None
janela3 = None
janela4 = None
janela5 = None
janela6 = janela_6()
janela7 = None




#LOOP DE LEITURA DOS EVENTOS
historico.append(janela1)
while True:
    
    janela,evento,valor = sg.read_all_windows()
    print(historico)
    # FECHAR O JOGO
    
    if evento == sg.WIN_CLOSED:
        janela.close()
        break
    
    #INVENTARIO
    
    if evento == 'Inventário':
        invent=inventario()
        invent['hp'].update(porcHP)
        invent['mana'].update(porcMANA)
        
        
    
    #PRÉ MENU
    
    if janela == janela1 and evento == 'Sim':
        janela2 = janela_2()
        janela2.un_hide()
        janela1.hide()
        historico.append('janela2')
    elif janela == janela1 and evento == 'Não':
        sg.popup('Volte quando estiver pronto')
        janela.close()
        break
    
    #TELA DE REGISTRO DE NOME
    
    if janela == janela2 and evento == 'Continuar':
        nome = janela2['nome'].get()
        janela3 =janela_3()
        janela2.hide()
        historico.append('janela3')
        
    #TELA DE REGISTRO DE CLASSE
    
    if janela == janela3 and evento == 'Guerreiro':
        classe = Classe(4,0,4,3,1,2)
        clas = 'guerreiro'
        janela4 = janela_4()
        janela3.hide()
        historico.append('janela4')
        
    if janela == janela3 and evento == 'Mago':
        classe = Classe(0,3,2,4,4,1)
        clas = 'mago'
        janela4 = janela_4()
        janela3.hide()
        historico.append('janela4')
        
    if janela == janela3 and evento == 'Ladino':
        classe = Classe(1,4,0,3,2,4)
        clas = 'ladino'
        janela4 = janela_4()
        janela3.hide()
        historico.append('janela4')
        
    if janela == janela3 and evento == 'Clérigo':
        classe = Classe(0,1,2,3,4,4)
        clas = 'clérigo'
        janela4 = janela_4()
        janela3.hide()
        historico.append('janela4')
    #INTRODUÇÃO 

    if janela == janela4 and evento == 'Continuar':
        janela5 = janela_5()
        janela4.hide()
        historico.append('janela5')
    
    #
    
    if janela == janela5:
        
        if evento == 'Investigar a parede':
            popup = sg.Window('RPG', [[sg.T('Os hierógrifos te mostram: Viashinos devorando humanos ainda vivos!')], [sg.Push(),sg.Yes(s=10, button_text='OK' ),sg.Push()]], disable_close=True).read(close=True)
        
        if evento == 'Ir pro corredor':
            janela6 = janela_6()
            janela5.hide()
            historico.append('janela6')
            
    #
    
    if janela == janela6:
        
        if evento == 'Olhar a pilha':
            d20(20, wis)
            if d20.fail == False:
                pista = True
                popup = sg.Window('RPG', [[sg.T('Você analisa a pilha de ossos e descobre uma armadilha logo à frente!')], [sg.Push(),sg.Yes(s=10, button_text='OK' ),sg.Push()]], disable_close=True).read(close=True)
                janela7 = janela_7_1()
                janela6.hide()
                historico.append('janela7')
            else:
                pista = False
                popup = sg.Window('RPG', [[sg.T('A pilha de ossos não diz nada a você.')], [sg.Push(),sg.Yes(s=10, button_text='OK' ),sg.Push()]], disable_close=True).read(close=True)
                fcrit = d20.f_crit
                d4(fcrit)
                dano = d4.d4
                hp -= dano
                janela7 = janela_7_2()
                janela6.hide()
                historico.append('janela7')

                                  
        if evento == 'Continuar andando':
            d4(False)
            dano = d4.d4
            hp -= dano
            janela7 = janela_7_2()
            janela6.hide()

    #
    
    if janela == janela7:
        pass
    
    if janela == invent:
        if evento == 'Voltar':
           
           