#Generamos un numero ramdon entre el 1 y el 100.
import random
Numero_a_descubrir = random.randint (1,100)


numero_elegido = float (input ("Número:"))
if numero_elegido > Numero_a_descubrir :
    print ("El número es mas bajo")
if numero_elegido < Numero_a_descubrir :
    print ("El número es mas alto")
if numero_elegido == Numero_a_descubrir :
    print ("Ese es el número")