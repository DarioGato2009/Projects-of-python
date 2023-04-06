import keyboard
import time
import pyautogui
mensaje = input("Escribe el mensaje para spamear    ")
tiempo_esperar = input("Escribe los segundos que deseas esperar antes de empezar a spamear el mensaje   ")
def spam():
    spameador = 1
    time.sleep(int(tiempo_esperar))
    while spameador == 1:
        pyautogui.write(mensaje)
        pyautogui.press("enter")
        if keyboard.is_pressed("f7"):
            spameador = 0
            if keyboard.is_pressed("f8"):
                spameador = 1
spam()