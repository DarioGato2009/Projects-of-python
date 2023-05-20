import time
import pyautogui as py
a = input("Selecciona los segundos antes de comienze a comentar el codigo")
b = input("Cuantas lineas quieres comentar")
time.sleep(int(a))
for i in range (int(b)):
    py.typewrite("#")
    py.press ("down")