#Generamos un numero ramdon entre el 1 y el 100.
import random
numero_a_descubrir = random.randint (1,100)
3
print ("Intenta adivinar el número del 1 al 100")

#Nombramos los parametros para el resultado final.
intentos = 0 
puntos = 0

#Creamos un bucle en el que si el numero que elegimos es mayor o menos que el que hay que descrubrir, empezara en bucle de nuevo; y si adivinamos el numero terminara el bucle.
while True :
 #Establecemos la formula para cualcular el número de intentos.
 intentos = intentos +1 
 try: 
    #Creamos un espacio para poner nuestro número y calculamos mediante el balor absoluto los puntos finales.
    numero_elegido = float (input ("Número:"))
    puntos = puntos + abs(numero_a_descubrir - numero_elegido)
    if numero_elegido == numero_a_descubrir:
        print (f"Ese es el número,{numero_a_descubrir}, muy bien.")
        break;
        
    if numero_elegido > numero_a_descubrir:
        print ("El número es más bajo")
        continue 
       
    if numero_elegido < numero_a_descubrir:
        print ("El número es más alto") 
        continue
 except:
    continue
 
 #proyectamos los intentos y los puntos finales. 
print (f"Intentos:{intentos}")
print (f"Puntos (cuantos menos mejor): {puntos}")







