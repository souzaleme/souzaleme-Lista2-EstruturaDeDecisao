'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra
 escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

sexo = str(input('Digite o sexo, "M" para masculino ou "F" para feminino: ')).upper()

if sexo == 'M':
 print('M - Masculino')
elif sexo == 'F':
 print('F - Feminino')
else:
 print('Sexo inválido')
