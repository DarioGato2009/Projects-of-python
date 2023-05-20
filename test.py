import random
i = int(input("introduce tu numero"))
a = i
numero = random.randint(1,i)
op1 = "A"
op2 = "B"
lista = []
for i in range(25):
    c = random.randint(1,2)
    if c == 1:
        lista.append(numero)
        lista.append(op1)
    else:
        lista.append(numero)
        lista.append(op2)
    print (lista)
    lista = []
    numero = random.randint(1,a)