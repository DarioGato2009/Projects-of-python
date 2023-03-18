import ctypes
import pyautogui as input

# obtén el identificador de la ventana actual
hwnd = ctypes.windll.user32.GetForegroundWindow()

# minimiza la ventana
while True:
    input.click(x = 1000, y =500)