'''
Escreva um programa capaz de exibir um menu para o usuário contendo as opções: 
somar dois números, subtrair dois números, multiplicar dois números e dividir dois números. 
O programa deve perguntar ao usuário qual operação ele deseja desempenhar, em seguida, 
solicitar dois números e efetuar a operação escolhida pelo usuário. 
Por fim, o programa deve exibir o resultado da operação na tela.
'''

print('''
|<===============> Calculadora <===============>|

0. Somar dois números
1. Subtrair dois números
2. Multiplicar dois números
3. Dividir dois números

|<===============>-------------<===============>|
''')

escolha = int(input('Escolha uma opção do menu: '))

if (escolha >= 0 and escolha <= 3):
	num1 = float(input('\nInforme o primeiro número da operação: '))
	num2 = float(input('Informe o segundo número da operação: '))

	resultado = 0
	operacao = 'undefined'

	if (escolha == 0):
		resultado = num1 + num2
		operacao = 'soma'
	
	elif (escolha == 1):
		resultado = num1 - num2
		operacao = 'subtração'
	
	elif (escolha == 2):
		resultado = num1 * num2
		operacao = 'multiplicação'
	
	elif (escolha == 3):
		resultado = num1 / num2
		operacao = 'divisão'

	print("\nA", operacao, "de", num1, "e", num2, "é igual a:", resultado)
else:
	print("Desconheço a opção", escolha, "do menu!") 
