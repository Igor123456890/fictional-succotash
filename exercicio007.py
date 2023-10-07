"""
Exercicios:

1) Mude a distancia entre as lentes dos óculos
2) Mude o tamanho das lentes
"""

import turtle

t = turtle.Turtle()
t.color('green')

# Desenhando a armação dos óculos
t.backward(120)
t.left(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.left(90)
t.forward(120)

# Ajuste do tamanho das lentes dos óculos
t.penup()
t.goto(-40, 50) # Definindo a posição para começar a desenhar a primeira lente
t.pendown()

# Desenhando a primeira lente com tamanho diferente (raio 60)
t.circle(60)

# Movendo para a posição da segunda lente
t.penup()
t.goto(40, 50) # Definindo a posição para começar a desenhar a segunda lente
t.pendown()

# Desenhando a segunda lente com tamanho diferente (raio 60)
t.circle(60)

# janela aberta
turtle.done()
