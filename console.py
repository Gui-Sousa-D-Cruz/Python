import random
import keyboard

def escolha():  # escolha de ação
    loop = True
    while loop:
        if keyboard.is_pressed('s'):
            escolha.act = 'S'
            loop = False
            break
        else:
            if keyboard.is_pressed('n'):
                escolha.act = 'N'
                loop = False
                break

nome = input('Olá! Qual seu nome? ')

print(f'Oi {nome}, está pronto para saber seu destino? ')

print('Aperte |S| para sim ou |N| para não!')

escolha() 

if escolha.act.upper() == 'S':

    num1 = int(random.randint(1, 20))

    if num1 == 1:
        print('|=-=-=|Você deve mandar mensagem para ela|=-=-=|')
    else:
        print('|=-=-=|Você não deve mandar mensagem para ela nunca mais|=-=-=|')
else: 
    print('|=-=-=|VOSE EH GAY|=-=-=|')