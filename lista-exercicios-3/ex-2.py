'''
Escreva um programa que exibe a mensagem “Jovem Padawan” caso o usuário tenha menos de 25 anos de idade, 
ou a mensagem “Jedi” caso o usuário tenha entre 25 e 51 anos ou a mensagem “Mestre Jedi” 
caso o usuário tenha mais de 50 anos de idade. O programa deve pedir para o usuário informar a idade dele.
'''

idade = int(input("Informe sua idade: "))

mensagem = "Mestre Jedi"

if (idade < 25):
	mensagem = "Jovem Padawan"
elif (idade >= 25 and idade < 51):
	mensagem = "Jedi"

print(mensagem)
