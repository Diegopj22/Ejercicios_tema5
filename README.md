# Ejercicios_tema5
https://github.com/Diegopj22/Ejercicios_tema5.git
## Ejercicio 1
¿Eres capaz de desarrollar un reloj de horas, minutos y segundos utilizando el módulo datetime con la hora actual? Hazlo en un script llamado reloj.py y ejecútalo en la terminal:

Ayuda

El módulo time integra una función llamada sleep(segundos) que puede pausar la ejecución de un programa durante un tiempo. Así mismo el módulo os integra la función system('cls') y system('clear') para limpiar la pantalla de la terminal en sistemas Windows y Linux/Unix respecticamente.



## Ejercicio 2
En este ejercicio deberás crear un script llamado contador.py que realice varias tareas sobre un fichero llamado contador.txt que almacenará un contador de visitas (será un número):

Nuestro script trabajará sobre el fichero contador.txt. Si el fichero no existe o está vacío lo crearemos con el número 0. Si existe simplemente leeremos el valor del contador.
Luego a partir de un argumento:
Si se envía el argumento inc, se incrementará el contador en uno y se mostrará por pantalla.
Si se envía el argumento dec, se decrementará el contador en uno y se mostrará por pantalla.
Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador por pantalla.
Finalmente guardará de nuevo el valor del contador de nuevo en el fichero.
Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: Error: Fichero corrupto.
