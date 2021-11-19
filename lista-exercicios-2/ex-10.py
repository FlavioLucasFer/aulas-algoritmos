'''
Escreva um programa capaz de calcular as raízes de qualquer equação do 2° grau, 
baseando-se na fórmula 𝑎𝑥2+𝑏𝑥+𝑐=0 onde os valores de a, b e c serão informados pelo usuário. 
Ao final do programa, imprima na tela os valores de x1 e x2.
'''

print('<========== CALCULADORA DE BHASKARA ==========>')

a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

x1 = 0
x2 = 0

delta = (b ** 2) - (4 * a * c)
raizDelta = delta ** (1/2)

x1 = (-b - raizDelta) / (2 * a)
x2 = (-b + raizDelta) / (2 * a)

print("x1 =", x1)
print("x2 =", x2)
