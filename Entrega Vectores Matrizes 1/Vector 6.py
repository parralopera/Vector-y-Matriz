# Se desea almacenar en un vector seis posiciones que corresponde a las caras de un dado,
# con la formula de valores aleatorios debe de generar un valor de uno a seis,
# se debe solicitar el numero de lanzamientos a realizar y luego calcular el valor obtenido en cada uno de los lances.

dado=randint(1,6)

from random import*
c=0
while True:
    dado=randint(1,7)
    print("Resultado del dado: ",dado)
    c+=1
    if dado==7:
        print("Por fin 7, al intento",c+1)
        break
    
'''
# Orto intento, solo que tengo mis dudas con este... pero haber si funciona :)

import random
def dice():
  dado = []
  for i in range(100):
      dado.append(random.choice(range(1,7)))
  return dado
  
  '''