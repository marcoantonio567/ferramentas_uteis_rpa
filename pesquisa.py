import pyautogui
import time
import webbrowser

# Abrir o navegador da web (neste caso, o Chrome)
webbrowser.open("https://www.google.com")

# Aguarde alguns segundos para o navegador abrir
time.sleep(5)

# Use o PyAutoGUI para realizar uma pesquisa no Google
pyautogui.write("Automatização com PyAutoGUI")
pyautogui.press("enter")

# Aguarde alguns segundos para os resultados da pesquisa aparecerem
time.sleep(5)

# Role a página para baixo (duas vezes) usando um valor positivo
pyautogui.scroll(2)

# Capture uma captura de tela da página de resultados da pesquisa
pyautogui.screenshot("resultado_da_pesquisa.png")

# Feche o navegador
pyautogui.hotkey("ctrl", "w")
