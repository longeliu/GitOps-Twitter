from kafka import KafkaProducer
import time
import json

from .getter.data_getter import Info_Getter
import os
from datetime import datetime

now = datetime.now() # current date and time

#mariadb_kubsev = "mariadb-service" #TODO Innecesario, pendiente de actualización en la imagen
kafka_kubsev = "kafka-service"

class Producer:
    def __init__(self, topic):
        self.topic = topic
        #self.freq = freq if isinstance(freq, int) else int(freq) INNECESARIOS PORQUE QUEREMOS STREAM COSNTANTE
        #self.limit = limit if isinstance(limit, int) else int(limit)
        self.server_addr = str(kafka_kubsev) #TODO Falta control de errores
        self.producer = KafkaProducer(bootstrap_servers=self.server_addr,
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        self.info_getter = Info_Getter(self.topic)
    
    def start_write(self):
        for i, tweet in enumerate(self.info_getter.tweets):
            dict_data = {
                "id":tweet.id, 
                "text":tweet.text, 
                "favorite_count":tweet.favorite_count,
                "in_reply_to_status_id":tweet.in_reply_to_status_id, 
                "in_reply_to_user_id":tweet.in_reply_to_user_id, 
                "in_reply_to_screen_name":tweet.in_reply_to_screen_name,
                "coordinates":tweet.coordinates, 
                "place":str(tweet.place), 
                "lang":tweet.lang, 
                "entities":tweet.entities,
                "source":tweet.source, 
                "is_quote_status":tweet.is_quote_status,
                "user.id":tweet.user.id, 
                "user.name":tweet.user.name, 
                "user.location":tweet.user.location,
                "user.description":tweet.user.description, 
                "user.url":tweet.user.url, 
                "user.followers_count":tweet.user.followers_count,
                "user.friends_count":tweet.user.friends_count, 
                "user.listed_count":tweet.user.listed_count, 
                "user.created_at":str(tweet.user.created_at), 
                "user.favourites_count":tweet.user.favourites_count, 
                "user.verified":tweet.user.verified
            }
            self.producer.send(self.topic, value=dict_data)
            print(f'Message {i + 1}: {dict_data}')
            time.sleep(1) #CAMBIADO A FRECUENCIA 1 SEGUNDO PARA NO SATURAR LA API DE TWITTER

if __name__ == '__main__':
    pass

