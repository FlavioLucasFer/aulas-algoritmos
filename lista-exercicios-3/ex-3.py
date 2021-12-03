# Escreva um programa capaz de imprimir na tela se um dado número informado pelo usuário é ímpar ou par.


numero = float(input("Informe um número: "))

if (numero % 2 == 0):
	print(numero, "é PAR")
else: 
	print(numero, "é ÍMPAR")
