# Se desea realizar un algoritmo que almacene las letras del alfabeto,
# debe mostrar las posiciones de las letras donde se encuentran cuando una persona, digita un nombre o una palabra.

# Solo Mostrar alfabeto

def listAlphabet():
      return [chr(i) for i in range(ord('a'),ord('z')+1)]
print(listAlphabet())


# Pocicion de letras y/o numeros

almacen = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numero = int(input("Ingrese numero de letra: [1_26]"))

if(numero > 0 and numero <= 26):
    print (almacen[numero - 1])
    
else:
    print ("Ingresar un valor entre 1-26: ")