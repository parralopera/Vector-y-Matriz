# Se desea realizar un algoritmo que permita almacenar dos valores que son ingresados en código binario,
# y se debe de realizar la suma y la resta de estos dos valores.

import numpy as np

valor1 = np.array([45, 65, 23 ,4 ,34])
print(valor1)
valor2 = np.array([6, 32, 8, 82, 77])
print(valor2)
op=input("Como desea realizar la operacion (suma/resta/multi/div): ")
if op=="suma":
    operacion = valor1 + valor2
elif op=="resta":
    operacion = valor1 - valor2
elif op=="multi":
    operacion = valor1 * valor2
elif op=="div":
    operacion = valor1 / valor2

print(operacion)

# Este algoritmo no suma los valores en binario, pero muestra una opcion de realizar diferentes operciones con los valores en los arrays
