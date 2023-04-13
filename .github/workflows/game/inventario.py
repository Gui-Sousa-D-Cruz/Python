import PySimpleGUI as sg
import random as rd
sg.theme('Reddit')
janela1= ''
nome = 'Gui'
classe = 'Gigolo'

dano = rd.randint(1,4)
danom = rd.randint(1,4)

def inventario():
    layout = [
        [sg.Text(f'Nome:   {nome}',size=(18,0)),sg.T(f'Classe:    {classe}', size=(18,0))],
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

pow = 0
dex = 0
con = 0
inT = 0
wis = 0
cha = 0
hpmax= 10 + con
hp = hpmax
manamax = 10 + inT
mana = manamax

hp-=dano
mana-=danom

porcHP= int((100 * hp) / hpmax)
porcMANA= int((100 * mana) / manamax)

invent=inventario()
invent['hp'].update(porcHP)
invent['mana'].update(porcMANA)

while True:
    janela,evento,valor = sg.read_all_windows()
    
   #------------------------------------------------------------------# 
    if janela == invent:
        if evento == 'Voltar':
            pass
           
  #------------------------------------------------------------------#  
    # FECHAR O JOGO 
    if evento == sg.WIN_CLOSED:
        janela.close()
        break