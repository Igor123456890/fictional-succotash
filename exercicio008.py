"""
Exercicios

1) Acrescente cores
2) Mude a largura da linha
3) Aumente a quantidade de linhas
"""

import turtle
import random

# tartaruga
t = turtle.Turtle()

# Definindo a largura da linha
t.width(3)

# Lista de cores
colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'red', 'orange', 'brown', 'cyan']

# Aumentando a quantidade de linhas para 12
for _ in range(12):
    color = random.choice(colors)
    t.color(color)
    t.forward(100)
    t.backward(100)
    t.right(30) # Ângulo ajustado para acomodar mais linhas

# janela aberta
turtle.done()
