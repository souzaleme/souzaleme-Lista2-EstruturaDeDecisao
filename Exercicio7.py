'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num2 > num1 < num3:
    print(f'O menor número é: {num1}')
elif num3 > num2 < num1:
    print(f'O menor número é: {num2}')
else:
    print(f'O menor número é: {num3}')