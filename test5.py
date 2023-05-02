letra = input("Inserta las letras que quieras pasar a binario       ")
def letra_a_binario(letra):
    valor_numerico = ord(letra)
    valor_binario = bin(valor_numerico)
    return valor_binario

binario = letra_a_binario(letra)
print(binario)
while True:
    letra = input("Inserta las letras que quieras pasar a binario       ")
    letra_a_binario()


