def texto_a_binario(texto):
    # Diccionario para asignar a cada letra su posición en el alfabeto
    alfabeto = {chr(i): i - 96 for i in range(97, 123)}

    # Convertir cada letra del texto a su posición en el alfabeto
    numeros = [alfabeto.get(letra.lower(), "") for letra in texto]

    # Eliminar las letras que no se encontraron en el alfabeto
    numeros = [num for num in numeros if num != ""]

    # Convertir cada número a su representación binaria
    binarios = [bin(num)[2:] for num in numeros]

    # Combinar los dígitos binarios de todos los números en una sola cadena
    cadena_binaria = "".join(binarios)

    return cadena_binaria

texto = input("Introduce el texto que deseas pasar a binario        ")
binario = texto_a_binario(texto)
print(binario)

