# Realice un algoritmo que permita realizar una tabla de multiplicación y que se pueda llenar sola de la tabla del 1 hasta la tabla 14.

for f in range(1,11):
    	multiplicacion = 7 * f
	print(f'7 x {f} = {multiplicacion}')
factor = 5
desde = 1
hasta = 15

for f in range(desde, hasta + 1):
	print(f'{factor} x {f} =  {factor * f}')
tabla_desde = 1
tabla_hasta = 10
desde = 1
hasta = 10

for factor1 in range(tabla_desde, tabla_hasta + 1):
	print(f'Tabla de multiplicar del {factor1}:')
	for factor2 in range(desde, hasta + 1):
		print(f'{factor1} x {factor2} = {factor1 * factor2}')
	print()