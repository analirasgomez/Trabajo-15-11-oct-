#Generamos un numero ramdon entre el 1 y el 100.
import random
Numero_a_descubrir = random.randint (1,100)
print (Numero_a_descubrir)

numero_elegido = float (input ("Número:"))

while numero_elegido>Numero_a_descubrir and numero_elegido<Numero_a_descubrir :
    if numero_elegido > Numero_a_descubrir :
        print ("El número es mas bajo")
    if numero_elegido < Numero_a_descubrir :
        print ("El número es mas alto")
    continue

if numero_elegido == Numero_a_descubrir :
    print ("Ese es el número")
