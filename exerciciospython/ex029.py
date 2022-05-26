km = int(input('Digte a velocidade atual do veículo: '))
if km > 80:
    print('O limte de velocidade é de 80Km/h')
    print('Você foi multado pois andou a {}Km/h'.format(km))
    multa = (km - 80) * 7
    print('Sua multa foi de: R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

