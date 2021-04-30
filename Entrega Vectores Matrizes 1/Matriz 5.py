'''
Realice un algoritmo que permita obtener el valor de cada uno de los vehículos teniendo la siguiente tabla de información.


Marca       Precio          % Descuento

Mazda       70.000.000      10%
Renault     56.000.000      20%
Chevrolet   64.000.000      11%
Audi        170.000.000     10%
Fiat        79.000.000      7%
Toyota      80.000.000      12%

'''

Mazda=0
Renult=0
Chevrolet=0
Audi=0
Flat=0
Toyota=0

# Fijos

Mazda_fijo=70000000
Renult_fijo=56000000
Chevrolet_fijo=64000000
Audi_fijo=170000000
Flat_fijo=79000000
Toyota_fijo=80000000

# Desc

Mazda_desc=0.10
Renult_desc=0.20
Chevrolet_desc=0.11
Audi_desc=0.10
Flat_desc=0.7
Toyota_desc=0.12

comprar = input("Ingrese Vehiculo a comprar: ")

if(comprar=="Mazda" or "mazda"):
        print("Valor a pagar: ", Mazda_fijo - Mazda_desc)
elif(comprar=="Renult" or "renult"):
        print("Valor a pagar: ", Renult_fijo - Renult_desc)
elif(comprar=="Chevrolet" or "chevrolet"):
        print("Valor a pagar: ", Chevrolet_fijo - Chevrolet_desc)
elif(comprar=="Audi" or "audi"):
        print("Valor a pagar: ", Audi_fijo - Audi_desc)
elif(comprar=="Flat" or "flat"):
        print("Valor a pagar: ", Flat_fijo - Flat_desc)
elif(comprar=="Toyota" or "toyota"):
        print("Valor a pagar: ", Toyota_fijo - Toyota_desc)
else:
    print("Error... Por favor intentar otra vez...")