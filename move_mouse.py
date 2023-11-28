import time
import pyautogui

# Define the time in seconds to consider inactivity
# The value set here is for testing only, increase this value as you are interested:
"""
Colab - Sintaxe Básica do Python

https://colab.research.google.com/drive/1TTaLUGJP94dxNmEaX-ey-vZT7asBUPB1?usp=sharing

Colab - NumPy

https://colab.research.google.com/drive/17lkN9Z3jJ7kQLrVEqLPWaeQ1B6jkui95?usp=sharing

Colab - Pandas

https://colab.research.google.com/drive/1XWVZYJ59BSVqmNDpbKUSNGune9jc5ppm?usp=sharing

Colab - Atividade

https://colab.research.google.com/drive/1IH1xoCf0HAvmrpzWNMvC8m3hIPqEAyyF?usp=sharing

 

Colab - Atividade - Gabarito

https://colab.research.google.com/drive/1ZA52vDLFhC-iOeBsNfmz0vFJoHVF3sQH?usp=sharing
Colab Exemplo Cancer de Mama:

https://colab.research.google.com/drive/1NHzaAg7AEV0EeSv16aPotuhZX0yb9JiO?usp=sharing

 

Colab Atividade Salário:

https://colab.research.google.com/drive/1FhDu0DwyGtaedrR5DhIwxJESh4Q3GJTJ?usp=sharing
Colab Aula4Exemplo1 - Gráficos

https://colab.research.google.com/drive/1iqXGu01KbkmIdQW7bhzhvLBxSdWomkbw?usp=sharing

Colab Aula4Exemplo2 - Gráficos e Pandas

https://colab.research.google.com/drive/1n4VtGyFboHJ8m3XgoFZSo1Wo-k0VPAjq?usp=sharing

Colan Aula4Atividade 1 - Salário

https://colab.research.google.com/drive/1zgA896PQi2mpRkBIFyGhYzghVRJp--Cm?usp=sharing
Colab - Aula 5 - Exemplo 1

https://colab.research.google.com/drive/1DobDmiY4-pLxDGGGRRzZJLnpKmc-WDgm?usp=sharing
Colab Aula 6 - Atividade 1 - Cálculo dos coeficientes

https://colab.research.google.com/drive/16IUgtgnW439PO0VARcEjgzjibBeJ9tXc?usp=sharing

Colab Aula 6 - Exemplo 1 - Regressão linear simples

https://colab.research.google.com/drive/1GsR1tYh1OzkAyxIVLyy-4gkeHvGzlinC?usp=sharing

Colab Aula 6 - Exemplo 2 - Seguro Saúde

https://colab.research.google.com/drive/1pN4RxWny9paZhGqAmn5iWi2goYHOKw88?usp=sharing

Colab Aula 6 - Exemplo 2 - Seguro Sáude - Completo

https://colab.research.google.com/drive/1LVv6WcEPRqL9q9J5BiNCdqTy6dhS9eST?usp=sharing

Colab Aula 6 - Exemplo 3 - Classificação - Iris

https://colab.research.google.com/drive/1qLzoWBOj5c2hN-JEt-83DGPDgTRIigTC?usp=sharing
Descrição da questão 6 da prova.

https://colab.research.google.com/drive/1EfJOZxRWPZ1NEeBrKkwT_g01Avw8eHf1?usp=sharing
Colab - Medidas de Classificação

https://colab.research.google.com/drive/12bhvYQGON0bsYnGFuDGKB9JJG2w1wKDr?usp=sharing
Colab: Árvore de Decisão Carro

https://colab.research.google.com/drive/11-NofE80PMkP8qXGaeAZhcjyX1oLnwEy?usp=sharing
Link Colab RNA - Cancer de mama

https://colab.research.google.com/drive/1GLMAzqh9yqg2Ohm_z7lnwqi939cBOwQS?usp=sharing
"""
INATIVIDADE = 5

# Get the current time
ultima_atividade = time.time()

# Infinite loop
while True:
    # Get the current mouse position
    x, y = pyautogui.position()

    # Wait for 1 second
    time.sleep(1)

    # Get the current time
    tempo_atual = time.time()

    # Calculate the elapsed time since the last activity
    tempo_inativo = tempo_atual - ultima_atividade

    # Check if there has been recent activity
    if tempo_inativo >= INATIVIDADE:
        # Move the mouse
        pyautogui.moveTo(x + 5, y - 5, duration=0.5)

    # Check if there has been a mouse or keyboard action
    if pyautogui.position() != (x, y):
        # Update the time of the last activity
        ultima_atividade = tempo_atual
