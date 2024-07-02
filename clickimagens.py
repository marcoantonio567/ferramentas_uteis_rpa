import time
import pyautogui
from PIL import Image

time.sleep(2)
image = Image.open('2.png')

# Localiza a imagem na tela
locations = pyautogui.locateAllOnScreen(image)
# Itera sobre as ocorrências da imagem
for location in locations:
    # Clica na ocorrência
    pyautogui.click(location,duration=0.4)