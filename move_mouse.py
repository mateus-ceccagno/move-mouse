import time
import pyautogui

# Define the time in seconds to consider inactivity
# The value set here is for testing only, increase this value as you are interested:
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