'''Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

dia_semana = int(input('Digite o número correspondente ao dia da semana (1-domingo, 2-segunda, 3-terça,4-quarta, 5-quinta, 6-Sexta, 7-Sábado): '))

if dia_semana == 1:
    print('domingo')
elif dia_semana == 2:
    print('segunda-feira')
elif dia_semana == 3:
    print('terça-feira')
elif dia_semana == 4:
    print('quarta-feira')
elif dia_semana == 5:
    print('quinta-feira')
elif dia_semana == 6:
    print('sexta-feira')
elif dia_semana == 7:
    print('sábado')
else:
    print('Valor inválido !')