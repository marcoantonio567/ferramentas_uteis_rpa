import pyautogui
import time

#da pause entre uma função e outra
pyautogui.PAUSE 


#usando apara arrastar o mause
# pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
pyautogui.dragTo(100, 200, 2)



with pyautogui.hold('shift'):
        pyautogui.press(['left', 'left', 'left'])
        

