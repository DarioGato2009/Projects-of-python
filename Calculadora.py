import time
print("Cabe recalcar que esta calculadora funciona con numeros negativos (Ej:-2) y positivos. Ademas, no se pueden hacer operaciones complejas con parentesis o ecuaciones, solo operaciones basicas.")
time.sleep(5)
while True:
    numero1 = float(input("Presiona un número "))        
    operacion = (input("Presiona la operacion que desea hacer "))
    numero2 = float(input("Presiona tu segundo numero "))
    if operacion == "+":
        print(numero1 + numero2)
    if operacion == "-":
        print(numero1 - numero2)
    if operacion == "*":
        print(numero1 * numero2)
    if operacion == "/":
        print(numero1 / numero2)