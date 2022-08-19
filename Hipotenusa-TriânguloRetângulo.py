import math

def calculo(cat_o,cat_a):
    valor = (math.pow(cat_o,2)) + (math.pow(cat_a,2))
    return math.sqrt(valor)

print('='*22)
print(' Triângulo retângulo')
print('='*22)
print('')
co = float(input('Insira o cateto oposto: '))
ca = float(input('Insira o cateto adjacente: '))

hipotenusa = calculo(co,ca)

print('')
print('Triângulo Retângulo \n\nCateto oposto: {} \nCateto adjacente: {} \nHipotenusa: {} \n'.format(co,ca,hipotenusa))