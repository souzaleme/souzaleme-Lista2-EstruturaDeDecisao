'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = float(input('Digite seu salário: R$ '))
aumento_20 = salario * 0.2
aumento_15 = salario * 0.15
aumento_10 = salario * 0.1
aumento_5 = salario * 0.05

if salario <= 280:
    print(f'Seu salário antes do reajuste era de: R${salario}')
    print('Seu salário terá um reajuste de 20%')
    print(f'O valor do aumento sobre seu salário será de: R${aumento_20}')
    print(f'Seu novo salário será de: R${salario + aumento_20}')
elif 280 < salario <=700:
    print(f'Seu salário antes do reajuste era de: R${salario}')
    print('Seu salário terá um reajuste de 15%')
    print(f'O valor do aumento sobre seu salário será de: R${aumento_15}')
    print(f'Seu novo salário será de: R${salario + aumento_15}')
elif 700 < salario <= 1500:
    print(f'Seu salário antes do reajuste era de: R${salario}')
    print('Seu salário terá um reajuste de 10%')
    print(f'O valor do aumento sobre seu salário será de: R${aumento_10}')
    print(f'Seu novo salário será de: R${salario + aumento_10}')
else:
    print(f'Seu salário antes do reajuste era de: R${salario}')
    print('Seu salário terá um reajuste de 5%')
    print(f'O valor do aumento sobre seu salário será de: R${aumento_5}')
    print(f'Seu novo salário será de: R${salario + aumento_5}')

