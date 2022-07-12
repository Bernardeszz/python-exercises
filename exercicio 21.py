#Peça para o usuario digitar três números e faça a multiplicação ao cubo de cada número

print ('Seja bem vindo, qual o seu nome?')
nome = input()

print(f'Sr. {nome}, digite um número')
num1 = float (input())

print ('digite outro número')
num2 = float (input())

print ('digite o último número')
num3 = float (input())

clc1 = num1 **2

clc2 = num2 **2

clc3 =num3 **2

soma = clc1 + clc2 + clc3

print (f'o calculo ao cubo desses três números é: {soma}')


