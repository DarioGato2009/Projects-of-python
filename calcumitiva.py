import time
print("Esta calculadora solo funciona con numeros enteros. Si intentas poner numeros decimales(con el punto(.)o la coma(,), el programa se cerrara.")
time.sleep(5)
print("Cabe recalcar que esta calculadora funciona con numeros negativos (Ej:-2) y positivos. Ademas, no se pueden hacer operaciones complejas con parentesis o ecuaciones, solo operaciones basicas.")
time.sleep(5)
while True == True:
    numero1 = int(input("presiona un numero"))
    operacion = (input("presiona la operacion que desea hacer"))
    numero2 = int(input("presiona tu segundo numero"))
    if operacion == "+":
        print(numero1 + numero2)
    if operacion == "-":
        print(numero1 - numero2)
    if operacion == "*":
        print(numero1 * numero2)
    if operacion == "/":
        print(numero1 / numero2)


