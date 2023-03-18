import time
minutos = " minuto"
han_pasado = "Ha pasado "
numero_de_minutos = 1
segundos_por_minuto = 61
i = 1
a = i + 1
while i < a :
    print (i)
    time.sleep (1)
    i += 1
    a = i + 1
    if i == segundos_por_minuto :
        segundos_por_minuto +=60
        print (han_pasado + str(numero_de_minutos) + minutos)
        numero_de_minutos += 1
    if numero_de_minutos >= 2 :
        han_pasado = "Han pasado "
        minutos = " minutos"
    if i >= 100000 :
        break
print ("Ganaste")