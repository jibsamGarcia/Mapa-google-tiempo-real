from time import sleep
import requests
from random import randint, choice
import random


url_classify = 'http://0.0.0.0:8000/telemetria'


#  Thread 1 ­ Receiving Messages
def prueba():
    valores_caida = ["true", "false"]
    caida_random = randint(0,1)
    #ran = random.uniform(5,8)
    caida = valores_caida[caida_random]
    caid = choice(valores_caida)
    latitud = round(random.uniform(21.11, 23.63), 6)
    longitud = round(random.uniform(-101.64, -102.55), 6)
    latidos = randint(75, 95)
    wrapped_msg = {
                'Caida': caida,
                'Latitud': latitud,
                'Longitud': longitud,
                'Latidos': latidos,
                }
    requests.post(url_classify, json=wrapped_msg)

if __name__ == "__main__":
    while True:
        prueba()
        sleep(3)
