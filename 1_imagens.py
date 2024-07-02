import pyautogui
import cv2
import time

# pip install opencv-python

# Aguarde alguns segundos para garantir que a imagem esteja visível na tela
time.sleep(2)

# Localize a imagem na tela com ajuste de confiança
try:
    image_location = pyautogui.locateOnScreen('config.png', confidence=0.7)
    if image_location:
        # Obtenha o centro da imagem
        image_center = pyautogui.center(image_location)

        # Clique na posição encontrada
        pyautogui.click(image_center)
    else:
        print("Imagem não encontrada na tela.")
except pyautogui.ImageNotFoundException:
    print("Imagem não encontrada na tela.")
