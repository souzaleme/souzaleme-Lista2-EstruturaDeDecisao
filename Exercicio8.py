'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''

produto1 = int(input('Digite o preço do produto 1: R$ '))
produto2 = int(input('Digite o preço do produto 2: R$ '))
produto3 = int(input('Digite o preço do produto 3: R$ '))

if produto3 > produto1 < produto2:
    print(f'O produto mais barato a ser comprado é o produto 1, que custa: R$ {produto1}')
elif produto1 > produto2 < produto3:
    print(f'O produto mais barato a ser comprado é o produto 2, que custa: R$ {produto2}')
else:
    print(f'O produto mais barato a ser comprado é o produto 3, que custa: R$ {produto3}')


