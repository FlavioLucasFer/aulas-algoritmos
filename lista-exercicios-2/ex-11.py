'''
Escreva um programa capaz de calcular a média anual de um aluno (baseando-se no formato bimestral) 
onde o aluno deve informar suas notas nos 4 bimestres. 
Além disso, solicite que o aluno informe a disciplina 
e ao final do programa imprima a seguinte mensagem na tela: 
“Suas notas na disciplina de DISCIPLINA foram A, B, C e D e a média anual foi de MEDIA” 
onde DISCIPLINA, A, B, C, D e MEDIA referem-se à disciplina informada pelo usuário, 
nota do 1° bimestre, nota do 2° bimestre, nota do 3° bimestre, nota do 4° bimestre 
e média anual respectivamente.
'''

print("|---------| Média anual |---------|")

disciplina = input("Informe qual a disciplina: ")

primeiroBimestre = float(input("Informe sua nota do primeiro bimestre: "))
segundoBimestre = float(input("Informe sua nota do segundo bimestre: "))
terceiroBimestre = float(input("Informe sua nota do terceiro bimestre: "))
quartoBimestre = float(input("Informe sua nota do quarto bimestre: "))

media = (primeiroBimestre + segundoBimestre + terceiroBimestre + quartoBimestre) / 4

# Suas notas na disciplina de DISCIPLINA foram A, B, C e D e a média anual foi de MEDIA

print(
	"Suas notas na disciplina de " + disciplina +
	" foram", primeiroBimestre, ", ", 
	segundoBimestre, ", ", terceiroBimestre, 
	" e", quartoBimestre, 
	" e a média anual foi de", media
)
