import sys
import time
import json
from kubernetes import client, config

config.load_incluster_config()
v1 = client.CoreV1Api()

namespace = "protokafka"

# -----FUNION DEL SERVICIO-----
#   El servicio deberá arrancar el proceso de creación de los pods necesarios para el correcto funcionamiento de kafka con múltiples topics.
#   El servicio podrá crear y eliminar topics, pero no podrá modificarlos, para crear un nuevo topic se deberá de reiniciar el proceso.
# -----------------------------

def openJson():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return data

def writeJson(data):
    with open("data.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=1)

# Función destinada a la creación de nuevos pods producer en kubernetes, provisionalmente es una idea feliz.
#   IMPORTANTE: EL PRODUCER TENGA QUE MIRAR TAMBIEN LA BBDD PARA ELEGIR EL TOPIC ESPECÍFICO
def create_producer(topic):
    pod_manifest = {
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
        "name": "producer-pod" + "-" + topic.lower(),
        "labels": {
            "app": "kafka-producer"
        }
    },
    "spec": {
        "containers": [
            {
                "name": "producer",
                "image": "longeliu/producer",
                "env": [
                    {
                        "name": "PRODUCER_TOPIC",
                        "value": topic
                    }
                ]
            }
            ]
        }
    }

    print(f'POD MANIFEST:\n{pod_manifest}')

    pod = v1.create_namespaced_pod(body=pod_manifest, namespace=namespace)

    print("New Producer Created")


# Funcion destinada a la creación de nuevos topics en la BBDD 
#   ¿Se permite la existencia de multiples topics con el mismo nombre en el caso de que se quiera que se manden datos al mismo brooker?, provisionalmente se omitirá el control de errores.
#   TODO Queda pendiente de discusión como se deberá agregar topics nuevos, ya sea a partir del backend o del front end, o a mano desde SQL.
def create_topic(topic_str):
    # PARA COMPROBAR SI EXISTE UN TOPIC DE MISMO NOMBRE
    pass

# Funcion destinada a la creación de nuevos topics en la BBDD
def remove_topic(topic_str):
    pass

# STATUS: 
#   - 0 = LIBRE
#   - 1 = OCUPADO

# BUCLE INFINITO QUE COMPRUEBA CONSTANTEMENTE SI HAY CAMBIOS EN DB
while True:
    topics = openJson() #Abre el json que contiene los datos
    for key in topics:  #Comprobamos todas los topics
        print(topics[key]["name"])
        print(topics[key]["status"])
        if topics[key]["status"] == "0": # Si el estado es 0, crea nuevo producer y actualiza el estado del json
            create_producer(topics[key]["name"])
            topics[key]["status"] = "1"
            writeJson(topics)

    time.sleep(5) #Actualización cada 5 segundos