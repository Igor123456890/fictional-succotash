"""
Exercícios

1) Mude/defina a forma da tartaruga
2) Mude a ordem das cores
3) Mude a largura da linha
4) Faça a tartaruga desenhar dois quadrados
"""
import turtle

turtle = turtle.Turtle()
turtle.pensize(5)

# Defina a forma da tartaruga
turtle.shape("turtle")

def animal():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

# Desenho do primeiro quadrado
turtle.color("blue")
animal()

# Movendo a tartaruga para uma nova posição
turtle.penup()
turtle.forward(150)
turtle.pendown()

# Desenho do segundo quadrado
turtle.color("red")
animal()

turtle.done()
