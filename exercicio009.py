"""
Exercicios:

1) Faça cada passo da tartaruga ter uma cor diferente
2) Aumente/diminua o diâmetro do círculo
"""

import turtle

# tartaruga
t = turtle.Turtle()

# Diâmetro desejado
diametro = 200  

# Calculando o comprimento da circunferência com base no diâmetro
comprimento_circunferencia = 3.14159265359 * diametro

# Ajustando o passo com base no comprimento da circunferência
passo = comprimento_circunferencia / 360

# Lista de cores
cores = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Loop para desenhar círculo com cores diferentes
for grau in range(360):
    t.color(cores[grau % len(cores)]) # Seleciona a próxima cor da lista
    t.forward(passo)
    t.right(1)

# Fecha a janela quando terminar
turtle.done()
