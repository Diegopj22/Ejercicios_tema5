# desarrollar un reloj de horas, minutos y segundos utilizando el módulo datetime.
import datetime 
import time
import os

while True:
    os.system("clear")
    dt=datetime.datetime.now()
    print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))
    time.sleep(1)
    
    