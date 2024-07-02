from pynput.mouse import Listener
from pynput.keyboard import Listener as KeyboardListener
import keyboard

# Função para registrar os cliques do mouse fora da janela
def on_click(x, y, button, pressed):
    if pressed:
        historico_mouse.append((x, y))
        print(f"{x},{y}, botão={button}")

# Função para registrar as teclas pressionadas
def on_key_press(key):
    historico_teclas.append(key)
    print(f"Tecla pressionada: {key}")

# Função para parar a execução quando a tecla Esc for pressionada
def stop_listeners():
    global mouse_listener, keyboard_listener
    mouse_listener.stop()
    keyboard_listener.stop()
    print("Listeners parados.")

# Inicialização do histórico
historico_mouse = []
historico_teclas = []

# Configurar o listener de cliques do mouse
with Listener(on_click=on_click) as mouse_listener:
    # Configurar o listener de teclado
    with KeyboardListener(on_press=on_key_press) as keyboard_listener:
        # Configurar a tecla Esc para parar os listeners
        keyboard.add_hotkey('esc', stop_listeners)
        
        # Mantém o programa em execução até que os listeners sejam interrompidos
        mouse_listener.join()
