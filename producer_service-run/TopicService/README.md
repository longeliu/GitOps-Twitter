# Servicio de Asignacion de Topics y creación de Productores
## Introducción
Este es el servicio que se encargará de la creación de los pods de kafka siguiendo el estado de los pods guardados dentro de una BBDD
## Requisitos
Se necesita una base de datos a la que se pueda comunicar el servicio, para el prototipado se colocará una en local y posteriormente se modificará la conexión para que pueda ser posible acceder desde el servicio