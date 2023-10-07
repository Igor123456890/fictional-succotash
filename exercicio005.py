"""
Exercícios

1) Aumente o tamanho do envelope
2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo
3) Deixe o envelope colorido
4) Reduza o aba do envelope
"""

import turtle

# Crie duas tartarugas com formas diferentes
aba = turtle.Turtle()
aba.shape('triangle') # Forma de triângulo para a aba
aba.color('red') # Cor da aba

corpo = turtle.Turtle()
corpo.shape('square') # Forma de quadrado para o corpo
corpo.color('blue') # Cor do corpo

# Desenho da aba (com tamanho reduzido)
aba.penup()
aba.goto(0, 0)
aba.pendown()
aba.begin_fill()
aba.left(60)
aba.forward(50) # Reduzi o tamanho da aba para 50 unidades
aba.right(120)
aba.forward(50) # Reduzi o tamanho da aba para 50 unidades
aba.right(120)
aba.forward(50) # Reduzi o tamanho da aba para 50 unidades
aba.end_fill()

# Desenho do corpo
corpo.penup()
corpo.goto(0, -50)
corpo.pendown()
corpo.begin_fill()
for _ in range(2):
    corpo.forward(150)
    corpo.right(90)
    corpo.forward(100)
    corpo.right(90)
corpo.end_fill()

# Mantenha a janela aberta até que o usuário a feche
turtle.done()
