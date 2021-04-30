# Se tiene un vector de 20 posiciones donde se desean almacenar marcas de vehículos,
# se tiene un segundo vector donde se almacenan los precios del mismo.

Marca=[]
for i in range(20):
    ingresar=(input("Ingrese Marca de Vehiculo: "))
    Marca.append(ingresar)
    
Precio=[]
for i in range(20):
    ingresar=int(input("Ingrese Precio de Vehiculo: "))
    Precio.append(ingresar)
    
print(Marca)
print(Precio)