from typing import Type, Any

# Class AirQuality per il dataset
class AirQuality:
    #Inizializzo gli attributi dell'oggetto AirQuality utilizzando i valori presenti nel dizionario air_quality
    def __init__(self, air_quality):
        self.id = air_quality["_id"]
        self.Country = air_quality["Country"]
        self.City = air_quality["City"]
        self.aqi_value = air_quality["AQI Value"]
        self.aqi_category = air_quality["AQI Category"]
        self.co_aqi_value = air_quality["CO AQI Value"]
        self.co_aqi_category = air_quality["CO AQI Category"]
        self.ozone_aqi_value = air_quality["Ozone AQI Value"]
        self.ozone_aqi_category = air_quality["Ozone AQI Category"]
        self.no2_aqi_value = air_quality["NO2 AQI Value"]
        self.no2_aqi_category = air_quality["NO2 AQI Category"]
        self.pm25_aqi_value = air_quality["PM2_5 AQI Value"]
        self.pm25_aqi_category = air_quality["PM2_5 AQI Category"]
        self.lat = air_quality["lat"]
        self.lng = air_quality["lng"]

    def dump(self):
        # Restituisci l'oggetto AirQuality come un dizionario
        return {
            #"id": self.id,
            "Country": self.Country,
            "City": self.City,
            "AQI Value": self.aqi_value,
            "AQI Category": self.aqi_category,
            "CO AQI Value": self.co_aqi_value,
            "CO AQI Category": self.co_aqi_category,
            "Ozone AQI Value": self.ozone_aqi_value,
            "Ozone AQI Category": self.ozone_aqi_category,
            "NO2 AQI Value": self.no2_aqi_value,
            "NO2 AQI Category": self.no2_aqi_category,
            "PM2_5 AQI Value": self.pm25_aqi_value,
            "PM2_5 AQI Category": self.pm25_aqi_category,
            "lat": self.lat,
            "lng": self.lng
        }

# Verifica se tutti gli attributi non sono nulli
def checkFormato(test):
    # Verifica se qualche attributo è vuoto per l'oggetto AirQuality
    if (
        test.Country == "" and test.City == "" and
        test.aqi_value == "" and test.aqi_category == "" and
        test.co_aqi_value == "" and test.co_aqi_category == "" and
        test.ozone_aqi_value == "" and test.ozone_aqi_category == "" and
        test.no2_aqi_value == "" and test.no2_aqi_category == "" and
        test.pm25_aqi_value == "" and test.pm25_aqi_category == "" and
        test.lat == "" and test.lng == ""
    ):
        return False
    return True