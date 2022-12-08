from io import open
import sys

fichero = open("contador.txt", "a+")
fichero.seek(0)
contenido = fichero.read()

if len(contenido) == 0:
    contenido = "0"
    fichero.write(contenido)

fichero.close()

#Vamos a intentar transformar el texto a un número
try:
    contador = int(contenido)

    # En función de lo que el usuario quiera
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contenido += 1
        elif sys.argv[1] == "dec":
            contenido -= 1
    
    print(contador)

    #Volvemos a escribir en el fichero los cambios
    fichero = open("contador.txt", "w")
    fichero.write(str(contenido))
    fichero.close()

except:
    print("Error: Fichero corrupto.")


