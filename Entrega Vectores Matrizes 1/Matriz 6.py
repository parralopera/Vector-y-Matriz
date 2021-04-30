# Se tiene una matriz con un tamaño para 100 registro de correos que le llega a un usuario donde se almacena un código consecutivo,
# la fuente (correo del remitente), el asunto y la descripción del correo y la fecha
# Se debe de hacer un algoritmo que cada que ingrese un nuevo correo lo haga de atrás hacia adelante
# es decir del ultimo enviado hacia la primera posición.
# Con el objetivo de simular que los primeros queden visibles, se deben imprimir en ese orden.

A = int(input(u"Ingrese el tamaño de datos a ingresar: "))
B = []
C = []
for i in range (0,A):
 B.append(input("Ingrese Nombres: "))
print (B)
for j in range (0,A):
 C.append(len(B[j]))
print (C)