"""
Exercícios
1) Reduza as duas linhas com forward para apenas uma, mas que faça a mesma
coisa que as atuais
2) Faça a tartaruga virar para a direita
3) Altere o comprimento dos lados do quadrado
4) Transforme o quadrado em um retângulo
"""

import turtle

turtle = turtle.Turtle()
turtle.shape('turtle')

l = 200 # Comprimento do retângulo
w = 100 # Largura do retângulo

# Desenhe o retângulo
turtle.forward(l)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(l)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
