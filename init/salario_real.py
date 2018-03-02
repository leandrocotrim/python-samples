salario = int(input('Digite o sálario. '))
imposto = 27.5

while imposto > 0.:
    imposto = input('Digite o imposto. Ex: %27.5. ')
    if not imposto:
        imposto = 27.5
    elif imposto == 's':
        break
    else:
        imposto = float(imposto)
   
    print('Valor real: {0}'.format(salario - (salario * imposto / 100)))

if imposto < 10:
    print('Médio')
elif imposto < 27.5:
    print('Alto')
else:
    print('Muito alto')

name = 'cotrim' if 5 == 5 else 'leandro'
print('\n' + name)
