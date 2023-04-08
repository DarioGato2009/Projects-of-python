import time
import pyautogui
import keyboard
def func():
    put = input("Selecciona y o n para acceder    ")
    if put == "y":
        print("Antes de comenzar, recuerda que, si quieres parar el programa, presiona la tecla f12. Si quieres reanudarlo, presiona la tecla f11")
        tecla_que_se_va_a_spamear = input("Presiona la tecla que deseas spamear     ")
        segundos_para_inicar_spamear = input("Selecciona los segundos restantes para comenzar a spamear     ")
        print("En ", (segundos_para_inicar_spamear), " segundos se comenzara a spamear la tecla seleccionada")
        time.sleep(int(segundos_para_inicar_spamear))
        def spamear():
            while True:
                tecla_spameada = pyautogui.press(tecla_que_se_va_a_spamear)
                if keyboard.is_pressed("f12"):
                    break
        spamear()
        while True:
            if keyboard.is_pressed("f11"):
                spamear()
                    
    if put == "n":
        pyautogui.hold("alt")
        pyautogui.press("f4")
func()