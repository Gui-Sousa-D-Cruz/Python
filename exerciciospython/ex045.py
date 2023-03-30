from random import choice
from time import sleep

lista = ['pedra', 'papel', 'tesoura']
print('-='*20)
print('           JOKÊMPO DO GUIGUI')
while True:#loop principal
    print('-='*20)
    print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
    print('-='*20)
    while True: #loop de escolha
        esc = int(input('Faça sua escolha: '))
        print('-='*20)
        if esc == 1:
            jogador = 'pedra'
            break #loop de escolha
        elif esc == 2:
            jogador = 'papel'
            break #loop de escolha
        elif esc == 3:
            jogador = 'tesoura'
            break #loop de escolha
        else:
            print('Escolha uma opcão válida!')
            print('-='*20)
    pc = choice(lista)
    sleep(1)
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PO!!!')
    print('-='*20)
    print('')
    print(f'O jogador escolheu {jogador}')
    print('')
    print(f'A máquina escolheu {pc}')
    print('')
    print('-='*20)
    
    if jogador == 'pedra' and pc == 'tesoura' or jogador == 'papel' and pc == 'pedra' or jogador == 'tesoura' and pc == 'papel':
        print('Vitória do jogador')
    elif jogador == pc:
        print('Empate')
    else:
        print('Vitória da máquina')
    print('-='*20)
    print('''Jogar novamente?
[ 1 ] Sim
[ 2 ] Não''')

    esc = int(input('Faça sua escolha: '))
    if esc == 2:      
        break #loop principal
    elif esc == 1:
        pass
    else:
        print('ERRO!!! Opção inválida!')
            
        