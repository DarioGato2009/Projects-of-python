def cifrado_cesar(texto, desplazamiento):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cifrado = alfabeto[desplazamiento:] + alfabeto[:desplazamiento]
    tabla = str.maketrans(alfabeto, cifrado)
    texto_cifrado = texto.translate(tabla)
    return texto_cifrado

# Ejemplo de uso
texto_original = input("Introduce tu texto original     ")
desplazamiento = input("Introduce el desplazamiento     ")
texto_cifrado = cifrado_cesar(texto_original, desplazamiento)

print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)
