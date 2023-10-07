"""
Exercícios

1) Faça cada quadrado ter uma cor
2) Faça cada quadrado com um formato diferente da tartaruga
3) Faça os quadrados não se tocarem
4) Desenhe um quadrado maior ao redor dos demais quadrados
"""

import turtle

# Criando uma tartaruga para o quadrado maior
t_outer = turtle.Turtle()
t_outer.shape("turtle")

# Criando quatro tartarugas com formatos diferentes para os quadrados menores
t1 = turtle.Turtle()
t1.shape("turtle")

t2 = turtle.Turtle()
t2.shape("triangle")

t3 = turtle.Turtle()
t3.shape("square")

t4 = turtle.Turtle()
t4.shape("circle")

# Liste das cores para os quadrados
colors = ["red", "green", "blue", "yellow"]

# Função para desenhar um quadrado com preenchimento de cor
def draw_colored_square(turtle, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

# Desenhando o quadrado maior
t_outer.penup()
t_outer.goto(-60, -60)
t_outer.pendown()
t_outer.pencolor("black")
t_outer.pensize(2)
for _ in range(4):
    t_outer.forward(220)
    t_outer.right(90)

# Desenhando os quadrados menores com cores diferentes usando as tartarugas
for i in range(4):
    draw_colored_square([t1, t2, t3, t4][i], colors[i])

# Aguarde o usuário fechar a janela
turtle.done()
