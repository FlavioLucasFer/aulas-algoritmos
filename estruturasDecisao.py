'''
OPERADORES LÓGICOS

==  -> igualdade
!=  -> diferença
>   -> maior que
<   -> menor que
>=  -> maior ou igual a
<=  -> menor ou igual a

CONECTIVO LÓGICO
or  (||) -> ou
and (&&) -> e
'''

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / altura

classicacao = "MAGREZA"
grauObesidade = "0"


if (imc >= 18.5 and imc <= 24.9):
	classicacao = "NORMAL"
	grauObesidade = "0"

elif (imc >= 25 and imc <= 29.9):
	classicacao = "SOBREPESO"
	grauObesidade = "I"

elif (imc >= 30 and imc <= 39.9):
	classicacao = "OBESIDADE"
	grauObesidade = "II"

elif (imc >= 40):
	classicacao = "OBESIDADE GRAVE"
	grauObesidade = "III"

print("IMC:", imc)
print("Classificação:", classicacao)
print("Guau de obesidade:", grauObesidade)
