import random
numero = random.randint(1,6)
input("presiona enter")
for i in range(1,7):
    if i == numero:
        print("impostor")
        break
    else:
        input("tripulante")