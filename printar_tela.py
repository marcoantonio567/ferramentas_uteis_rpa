import pyautogui
import time

# Aguarde alguns segundos antes de começar
time.sleep(3)

# Obtenha as dimensões da tela
largura, altura = pyautogui.size()

# Mova o mouse para o centro da tela
pyautogui.moveTo(554, 750, duration=2)

# Clique com o botão esquerdo do mouse
pyautogui.click()

# Digite algo no teclado
pyautogui.typewrite("fala ai meu mano") 

# Pressione a tecla Enter
pyautogui.press("enter")

# Mova o mouse para uma posição específica
pyautogui.moveTo(100, 100, duration=1)

# Role a roda do mouse para cima
pyautogui.scroll(3)

# Capture uma captura de tela
pyautogui.screenshot("captura_de_tela.png")

# Mova o mouse de volta para a posição original
pyautogui.moveTo(largura / 2, altura / 2, duration=1)
