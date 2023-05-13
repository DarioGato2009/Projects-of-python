import random as rd

#definir variables principales

#pedir al usuario los valores del cifrado
szl = int(input('Introduce la SZL [Longitud de cadena] >> '))
szq = int(input('Introduce la SZQ [Longitud de la clave] >> '))
snx = int(input('Introduce el SNX [shift máximo en la clave] >> '))
file_name = input('Introduce el nombre de archivo >> ')
def genkey():
    y = 1
    #hacer cosas
    for i in range (szl):
        print(":)")
        for ii in range (szl):
            ssz = rd.randint(1, snx)
            y += 1
            sszn = "ssz"
            ssz = ssz + y
            print(ssz)

    for iii in range (szq):
        print(":)")

genkey()