import pyautogui
import keyboard
def func():
    print("para empezar a spamear el click izquierdo, presiona f1, para parar el programa, presiona f2")
    while True:
        if keyboard.is_pressed('f1'):
            while True:
                pyautogui.tripleClick()
                if keyboard.is_pressed('f2'):
                    break
while True:
    func()