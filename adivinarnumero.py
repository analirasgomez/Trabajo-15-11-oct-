#Generamos un numero ramdon entre el 1 y el 100.
import random
Numero_a_descubrir = random.randint (1,100)

Intentos = 0 
Puntos = 0

while True : 
 Intentos = Intentos +1

 try: 
    numero_elegido = float (input ("Número:"))
    if numero_elegido == Numero_a_descubrir :
        print (f"Ese es el número,{Numero_a_descubrir}, muy bien.")
        break;
        
    if numero_elegido > Numero_a_descubrir :
        print ("El número es más bajo")
        continue 
       
    if numero_elegido < Numero_a_descubrir :
        print ("El número es más alto")
        continue
 except:
    continue
 
print (f"Intentos:{Intentos}")
 