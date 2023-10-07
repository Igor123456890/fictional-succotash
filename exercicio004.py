"""
Exercícios

1) Acrescente ao menos mais duas cores à lista de cores possíveis
Veja os nomes de cores válidos em: https://pt.wikipedia.org/wiki/Lista_de_cores
(coluna Nome Web)
2) Faça o triângulo apontar para cima
3) Remova a cor vermelha da lista de cores possíveis
4) Mude a largura da linha
"""

import turtle
import random

turtle = turtle.Turtle()
turtle.width(3) # Definindo a largura da linha para 3 pixels
colors = ['purple', 'blue', 'green', 'orange'] #duas cores adicionadas e removido o red

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.setheading(60)
