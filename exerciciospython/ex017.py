from math import pow, hypot
catop = float(input('Digite o cateto oposto: '))
catadj= float(input('Digite o cateto adjacente: '))
num1 = pow(catop, 2)
num2 = pow(catadj, 2)
soma = num1+num2
hip = hypot(num1+num2)
print('A sua equação é: \nx²={:.0f}²+{:.0f}² \nx²={:.0f}+{:.0f} \n'
      'x²={:.0f} \nx=√{:.0f} \nx={:.0f}'.format(catop, catadj, num1, num2, soma, soma, hip))



