import pyautogui
import keyboard
def func():
    while True:
        if keyboard.ipress('f7'):
            while True:
                pyautogui.tripleClick()
                if keyboard.is_pressed('f8'):
                    break
while True:
    func()