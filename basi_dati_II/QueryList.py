import BDConnectionPool as Cp
import AirQuality


# Lista delle query
# EightParameter è la query dinamica per la ricerca che mi permette di calcolare i range sulla base dei valori inseriti dall'utente.
def eightParameter(country, city, tot_aqi, aqi_category, tot_co, aqi_co_category, lat, lng):
    col = Cp.connection_pool()
    query = col.find({"$and": [
        {"Country": country},
        {"City": city},
        {"AQI Value": tot_aqi},
        {"CO AQI Value": tot_co},
        {"AQI Category": aqi_category},
        {"CO AQI Category": aqi_co_category},
        {"lat": lat},
        {"lng": lng}
    ]
    })
    return query


# InsertCounry mi permette di inserisci un paese con tutti i campi necessari per la memorizzazione in MongoDB
def insertCountry(country):
    col = Cp.connection_pool()
    col.insert_one({
        "Country": country.Country,
        "City": country.City,
        "AQI Value": country.aqi_value,
        "AQI Category": country.aqi_category,
        "CO AQI Value": country.co_aqi_value,
        "CO AQI Category": country.co_aqi_category,
        "Ozone AQI Value": country.ozone_aqi_value,
        "Ozone AQI Category": country.ozone_aqi_category,
        "NO2 AQI Value": country.no2_aqi_value,
        "NO2 AQI Category": country.no2_aqi_category,
        "PM2_5 AQI Value": country.pm25_aqi_value,
        "PM2_5 AQI Category": country.pm25_aqi_category,
        "lat": country.lat,
        "lng": country.lng
    })


# UpdateCountry è la funzione per aggiornare un paese in base al nome della città indicata
def updateCountry(country, country1):
    col = Cp.connection_pool()
    myquery = {"Country": country}
    newvalues = {
        "$set": {
            "Country": country1.Country,
            "City": country1.City,
            "AQI Value": country1.aqi_value,
            "AQI Category": country1.aqi_category,
            "CO AQI Value": country1.co_aqi_value,
            "CO AQI Category": country1.co_aqi_category,
            "Ozone AQI Value": country1.ozone_aqi_value,
            "Ozone AQI Category": country1.ozone_aqi_category,
            "NO2 AQI Value": country1.no2_aqi_value,
            "NO2 AQI Category": country1.no2_aqi_category,
            "PM2_5 AQI Value": country1.pm25_aqi_value,
            "PM2_5 AQI Category": country1.pm25_aqi_category,
            "lat": country1.lat,
            "lng": country1.lng
        }
    }
    print(newvalues)
    col.update_one(myquery, newvalues)


# DeleteCountry è la funzione che elimina un paese sulla base del nome
def deleteCountry(country):
    col = Cp.connection_pool()
    col.delete_one({"Country": country})


# Trova tutti i paesi in ordine alfabetico per nome, utile per inserire gli elementi nella tabella
def countryAlphabetica():
    col = Cp.connection_pool()
    query = col.find().sort("Country", 1)
    return query


# Trova i paesi per nome
def findCountryByName(name):
    col = Cp.connection_pool()
    query = col.find({"Country": name})
    return query


# Trova i paesi per categoria di AQI
def findCountryByAQICategory(category):
    col = Cp.connection_pool()
    query = col.find({"AQI Category": category})
    return query


# Trova i paesi con valore di AQI tra min e max
def findCountryByAQIValue(min, max):
    col = Cp.connection_pool()
    query = col.find({"AQI Value": {"$gt": min, "$lt": max}})
    return query


# Trova i paesi per coordinata latitudine e longitudine
def findCountryByCoordinates(lat, lng):
    col = Cp.connection_pool()
    query = col.find({"lat": lat, "lng": lng})


# Trova i paesi con valore di CO AQI tra min e max
def findCountryByCOAQIValue(min, max):
    col = Cp.connection_pool()
    query = col.find({"CO AQI Value": {"$gt": min, "$lt": max}})
    return query


# Trova i paesi per categoria di Ozone AQI
def findCountryByOzoneAQICategory(category):
    col = Cp.connection_pool()
    query = col.find({"Ozone AQI Category": category})
    return query


# Trova i paesi con valore di NO2 AQI tra min e max
def findCountryByNO2AQIValue(min, max):
    col = Cp.connection_pool()
    query = col.find({"NO2 AQI Value": {"$gt": min, "$lt": max}})
    return query


# Trova i paesi per categoria di PM2_5 AQI
def findCountryByPM25AQICategory(category):
    col = Cp.connection_pool()
    query = col.find({"PM2_5 AQI Category": category})
    return query


# Trova i paesi con valore di PM2_5 AQI tra min e max
def findCountryByPM25AQIValue(min, max):
    col = Cp.connection_pool()
    query = col.find({"PM2_5 AQI Value": {"$gt": min, "$lt": max}})
    return query


# Trova i paesi per coordinata latitudine o longitudine
def findCountryByLatitudeOrLongitude(value):
    col = Cp.connection_pool()
    query = col.find({"$or": [{"lat": value}, {"lng": value}]})
    return query
