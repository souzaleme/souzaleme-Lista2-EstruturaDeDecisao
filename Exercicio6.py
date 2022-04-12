'''Faça um Programa que leia três números e mostre o maior deles'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num3 < num1 > num2:
    print(f'O maior número é {num1}')
elif num1 < num2 > num3:
    print(f'O maior número é: {num2}')
else:
    print(f'O maior número é: {num3}')
