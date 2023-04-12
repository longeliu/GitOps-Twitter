from .producer import Producer
import sys
import os

env_vars = {
    "PRODUCER_TOPIC": ""
}

for k,v in os.environ.items():
    if k == "PRODUCER_TOPIC":
        env_vars[k] = v
        print(env_vars[k])
    else:
        print("{0} no es una clave valida".format(k))


if __name__ == '__main__':
    producer = Producer(env_vars["PRODUCER_TOPIC"])
    producer.start_write()