'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''

a = float(input('Digite o valor de a: '))
b = float(input('Digite ovalor de b: '))
c = float(input('Digite o valor de c: '))
delta = b ** 2 - 4 * a * c
raiz_delta = delta ** (1/2)
x1 = (-b + raiz_delta) / (2 * a)
x2 = (-b - raiz_delta) / (2 * a)

if a == 0:
    print('Não é uma equação de segundo grau, pois a é igual a zero')
elif delta < 0:
    print(f'Delta = {delta}')
    print('Delta negativo a equação não possui raizes reais')
elif delta == 0:
    print(f'Delta = {delta}')
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
elif delta > 0:
    print(f'Delta = {delta}')
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')