print('========== LOJAS GUIGUI ==========')
val = int(input('Valor da compra: R$ '))
print('FORMAS DE PAGAMENTO ')
print('''[ 1 ] à vista dinheiro/cheque.
[ 2 ] à vista cartão de débito.
[ 3 ] 2x no cartão de crédito.
[ 4 ] 3x ou mais no cartão.''')
print('==================================')
while True:
    opc = int(input('Qual será a forma de pagamento? '))
    print('==================================')
    
    if opc == 1:
        porc = val * 10 / 100
        dec = val - porc
        print('Sua compra será à vista no dinhero/cheque!')
        print(f'Você receberá um desconto de R$ {porc:.2f}!')
        print(f'O valor total da compra será R$ {dec:.2f}!')
        print('==================================')
        break #loop principal
    elif opc == 2:
        print('Sua compra será a vista no débito')
        porc = val * 5 /100
        dec = val - porc
        print(f'Você receberá um desconto de R$ {porc:.2f}')
        print(f'O valor total da compra será R$ {dec:.2f}')
        print('==================================')
        break #loop principal
    elif opc == 3:
        print('''[ 1 ] 1x.
[ 2 ] 2x. ''')
        print('==================================')
        while True:
            p = int(input('Escolha a opção: '))
            print('==================================')
            if p == 1:
                print('Sua compra será à vista no crédito!')
                print(f'O valor da sua compra será R$ {val}!')
                break
            elif p == 2:
                print('Sua compra será parcelada em 2x no crédito!')
                print(f'O valor da sua compra será R$ {val:.2f}!')
                print(f'Serão {p} parcelas de R$ {val/2:.2f}!')
                break
            else:
                print('Digite um número válido')
                print('==================================')
                
        print('==================================')
        
        break #loop principal
    elif opc == 4:
        print('Digite uma opção válida.')
        print('==================================')
        
    else:
        print('Digite uma opção válida.')
        print('==================================')