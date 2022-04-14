'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe
se este ano é ou não bissexto.'''

ano = int(input('Digite um ano: '))
resto_ano_div4 = ano % 4
resto_ano_div100 = ano % 100
resto_ano_div400 = ano % 400

if resto_ano_div4 == 0 and resto_ano_div100 > 0:
    print('O ano é bissexto')
elif resto_ano_div4 > 0 and resto_ano_div400 > 0:
    print('O ano não é bissexto')
elif resto_ano_div4 > 0 and resto_ano_div400 == 0:
    print('O ano é bissexto')
