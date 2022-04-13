'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao
Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade
de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.'''

salario_h = float(input('Digite seu salário por hora trabalhada: '))
h_trabalhadas = float(input('Digite o número de horas trabalhadas no mês: '))
salario_bruto = salario_h * h_trabalhadas
ir_5 = salario_bruto * 0.05
ir_10 = salario_bruto * 0.1
ir_20 = salario_bruto * 0.2
inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11

if salario_bruto <= 900:
    print(f'Salário bruto: R$ {salario_bruto} ')
    print(f'(-) IR (Isento)')
    print(f'(-) INSS (10%): R$ {inss}')
    print(f'FGTS (11%): R$ {fgts}')
    print(f'Total de descontos: R$ {ir_5 + inss}')
    print(f'Salário líquido: R$ {salario_bruto - ir_5 - inss}')
elif 900 < salario_bruto <= 1500:
    print(f'Salário bruto: R$ {salario_bruto} ')
    print(f'(-) IR (5%): R$ {ir_5}')
    print(f'(-) INSS (10%): R$ {inss}')
    print(f'FGTS (11%): R$ {fgts}')
    print(f'Total de descontos: R$ {ir_5 + inss}')
    print(f'Salário líquido: R$ {salario_bruto - ir_5 - inss}')
elif 1500 < salario_bruto <= 2500:
    print(f'Salário bruto: R$ {salario_bruto} ')
    print(f'(-) IR (10%): R$ {ir_10}')
    print(f'(-) INSS (10%): R$ {inss}')
    print(f'FGTS (11%): R$ {fgts}')
    print(f'Total de descontos: R$ {ir_10 + inss}')
    print(f'Salário líquido: R$ {salario_bruto - ir_10 - inss}')
else:
    print(f'Salário bruto: R$ {salario_bruto} ')
    print(f'(-) IR (20%): R$ {ir_20}')
    print(f'(-) INSS (10%): R$ {inss}')
    print(f'FGTS (11%): R$ {fgts}')
    print(f'Total de descontos: R$ {ir_20 + inss}')
    print(f'Salário líquido: R$ {salario_bruto - ir_20 - inss}')