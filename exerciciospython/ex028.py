from random import randint
from time import sleep
num = randint(1, 5)
print('-=-' * 20)
print('Eu pensei em um número entre 1 e 5, tente advinhar qual foi.')
print('-=-' * 20)
pal = int(input('Digite aqui seu palpite: '))
print('-=-' * 20)
print('Processando sua resposta...')
print('-=-' * 20)
sleep(2)
if pal == num:
    print('Você acertou, parabéns!')
else:
    print('Você errou, pensei em {}, tente novamente!'.format(num))
print('-=-' * 20)
