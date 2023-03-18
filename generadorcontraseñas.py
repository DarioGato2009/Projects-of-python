import time
import random
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "#@()<>?¿-;%_&:+-"
unir = f'{letras}{numeros}{simbolos}'
longitud = 10
contraseña = random.sample(unir, longitud)
password_final= "".join(contraseña)
print(password_final)
time.sleep(30)