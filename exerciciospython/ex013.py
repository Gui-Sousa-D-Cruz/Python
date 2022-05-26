n1 = int(input('Digite seu sálario aqui: '))
print('Seu salário é: R${:.2f}.'.format(n1))
p1 = n1*(15/100)
s = n1+p1
print('Seu salário com aumento de 15% é R${:.2f}.'.format(s))