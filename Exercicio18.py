'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
resto_ano_div4 = ano % 4
resto_ano_div100 = ano % 100
resto_ano_div400 = ano % 400
print(f'{dia}/{mes}/{ano}')

if mes == 1 and 0 < dia <= 31:
    print('Data válida')
elif mes == 2 and resto_ano_div4 == 0 and resto_ano_div100 > 0 and 0 < dia <= 29:
    print('O ano é bissexto')
    print('Data válida')
elif mes == 2 and resto_ano_div4 > 0 and resto_ano_div400 > 0 and 0 < dia <= 28:
    print('O ano não é bissexto')
    print('Data válida')
elif mes == 2 and resto_ano_div4 > 0 and resto_ano_div400 == 0 and 0 < dia <= 29:
    print('O ano é bissexto')
elif mes == 3 and 0 < dia <= 31:
    print('Data válida')
elif mes == 4 and 0 < dia <= 30:
    print('Data válida')
elif mes == 5 and 0 < dia <= 31:
    print('Data válida')
elif mes == 6 and 0 < dia <= 30:
    print('Data válida')
elif mes == 7 and 0 < dia <= 31:
    print('Data válida')
elif mes == 8 and 0 < dia <= 31:
    print('Data válida')
elif mes == 9 and 0 < dia <= 30:
    print('Data válida')
elif mes == 10 and 0 < dia <= 31:
    print('Data válida')
elif mes == 11 and 0 < dia <= 30:
    print('Data válida')
elif mes == 12 and 0 < dia <= 31:
    print('Data válida')
else:
    print('Data inválida')




