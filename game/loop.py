import keyboard
import random

def escolha(): #escolha de ação
    loop = True
    while loop:
        if keyboard.is_pressed('s'):
            act = 'S'
            loop = False
            break
        else:
            if keyboard.is_pressed('n'):
                act = 'N'
                loop = False
                break


def classe(): #escolha de classe
    loop = True
    while loop:
        if keyboard.is_pressed('1'):
            classe = 'guerreiro'
            loop = False
            break
        else:
            if keyboard.is_pressed('2'):
                classe = 'mago'
                loop = False
                break
            else:
                if keyboard.is_pressed('3'):
                    classe = 'ladino'
                    loop = False
                    break
                else:
                    if keyboard.is_pressed('4'):
                        classe = 'clérigo'
                        loop = False
                        break


def d20(scss, atrib):
    sucesso = scss
    d20 = random.randint(1, 20)
    roll = d20 + atrib
    print(scss, atrib, d20, roll)
      

    if roll <= 5:
        #print('Fracasso crítico!')
        f_crit = True
    else:
        if roll >= 20:
            #print('Sucesso crítico!')
            s_crit = True
        else:
            if roll >= sucesso:
                #print('Sucesso')
                s_crit = False
            else:
                #print('Fracasso')
                f_crit = False