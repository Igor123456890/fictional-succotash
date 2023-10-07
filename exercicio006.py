"""
Exercicios

1) Era para ser um envelope. Mas saiu errado. Corrija.
"""

import turtle

# Configuração inicial
t = turtle.Turtle()
t.speed(1)
t.color('green')
t.pensize(2)

# Desenhando a parte superior do envelope
t.fillcolor('white')
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.end_fill()

# Desenhando a aba do envelope
t.fillcolor('white')
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(40)
t.left(90)
t.forward(50)
t.end_fill()

# Fechar o envelope
t.penup()
t.goto(70, 0)
t.pendown()
t.left(45)
t.forward(140)

# Finalizar
turtle.done()
