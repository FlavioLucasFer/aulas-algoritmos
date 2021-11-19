'''
Escreva um programa capaz de calcular o IMC do usuário, 
todos os dados individuais do usuário necessários para o cálculo devem ser solicitados ao usuário. 
Ao final do programa, imprima na tela as entradas informadas pelo usuário e o valor de seu IMC.
'''

altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

imc = peso / altura

print("Seu IMC é de:", imc)
