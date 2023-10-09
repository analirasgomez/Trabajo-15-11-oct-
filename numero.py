#Generamos un numero ramdon entre el 1 y el 100.
import random
numero_a_descubrir = random.randint (1,100)

print ("Intenta adivinar el número del 1 al 100")

#importamos el tiempo siendo sleep 1 seg y empezamos la cuenta de ellos.
import time 
inicio = time.time()
time.sleep(1)

#Nombramos los parametros para el resultado final.
intentos = 0 
puntos_de_diferencias = 0

#Creamos un bucle en el que si el numero que elegimos es mayor o menos que el que hay que descrubrir, empezara en bucle de nuevo; y si adivinamos el numero terminara el bucle.
while True :
 #Establecemos la formula para cualcular el número de intentos.
 intentos = intentos +1 
 try: 
    #Creamos un espacio para poner nuestro número y calculamos mediante el balor absoluto los puntos finales.
    numero_elegido = float (input ("Número:"))
    puntos_de_diferencias = int(puntos_de_diferencias + abs(numero_a_descubrir - numero_elegido))
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

#finalizamos el tiempo
fin = time.time()

#proyectamos los intentos, los puntos de diferencia finales y el tiempo tardado.
print (f"Intentos:{intentos}")
print (f"Número de diferencia entre el num dicho y el que buscas (cuantos menos mejor):  {puntos_de_diferencias}")
print (f"Has tardado: {int(fin-inicio)} segundos.")

#calculamos con formula y proyectamos los puntos totales.
puntos_totales = int(puntos_de_diferencias * (fin-inicio) / intentos)
print (f"puntos finales (cuantos menos mejor): {puntos_totales} puntos.") 