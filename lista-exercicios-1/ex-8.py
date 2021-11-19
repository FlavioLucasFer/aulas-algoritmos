'''
Escreva um programa capaz de calcular a seguinte equação do 2° grau 𝑥2−𝑥 −12=0. 
O programa deve armazenar os valores de a, b e c em variáveis assim como os resultados da equação. 
Para a solução, pode-se quebrar a resolução da equação em quantas partes forem necessárias 
e armazenas as os valores das partes em quantas variáveis forem necessárias. 
Ao final do programa, exiba os resultados da equação na tela usando funções “print”.
'''
a = 1
b = -1
c = -12

x1 = 0
x2 = 0

delta = 4 * a * c
delta = (b ** 2) - delta

raizDelta = delta ** (1/2)

parteBaixo = 2 * a

x1 = (-b + raizDelta) / parteBaixo
x2 = (-b - raizDelta) / parteBaixo

print("x1:", x1)
print("x2:", x2)
