import pymongo
#Creo una connessione al database locale MongoDB eseguito sulla porta 27017

def connection_pool():
        client = pymongo.MongoClient("mongodb://localhost:27017")
        #accedo alla collezione presente all'interno del db AirQuality
        col = client["Air_Quality"]["Air_Quality"]
        #restituisco la collezione
        return col

