# importo le funzioni necessarie dal modulo Flask per gestire richieste, reindirizzamenti, template HTML, risposte HTTP e JSON
from flask import Flask, render_template, request
import QueryList as Query
import AirQuality

app = Flask(__name__, template_folder="bd_projects_frontend", static_folder="bd_projects_frontend/assets")

table = None


def changeResult(value):
    global table
    table = value
    return getResult()


def getResult():
    return table


def fullTable():
    lista = Query.countryAlphabetica()
    airQuality = []
    for i in lista:
        airQuality.append((AirQuality.AirQuality(i)))
    return airQuality


@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/test_query")
def test_query():
    return render_template("test_query.html", list_air=changeResult(fullTable()))


# Ricerca paese
@app.route("/test_query/find_query", methods=['POST', 'GET'])
def find_query():
    # Verifica se la richiesta è di tipo POST
    if request.method == 'POST':
        # Estrae i valori dai campi del modulo inviato con la richiesta
        country = request.form['find-country']
        city = request.form['find-city']
        aqi_min = request.form['find-aqi-min']
        aqi_max = request.form['find-aqi-max']
        aqi_category = request.form['find-aqi_category']
        co_min = request.form['find-co-min']
        co_max = request.form['find-co-max']
        aqi_co_category = request.form['find-aqi-co_category']
        lat = request.form['find-lat']
        lng = request.form['find-lng']

        temp1 = 0
        temp2 = 0
        # Se il nome del paese rappresenta una stringa vuota viene assegnato un dizionario {"$ne": None}.
        if country == "":
            country = {"$ne": None}
        if city == "":
            city = {"$ne": None}
        if aqi_category == "":
            aqi_category = {"$ne": None}
        if aqi_co_category == "":
            aqi_co_category = {"$ne": None}
        if lat == "":
            lat = {"$ne": None}
        if lng == "":
            lng = {"$ne": None}

        # Qui gestisco i casi in cui ho uno o entrambi i valori di aqi_min e aqi_max forniti come stringhe vuote.
        # A seconda di questi valori, viene costruita una condizione di filtro per il campo "tot_aqi" utilizzando operatori di confronto
        # come "$ne" (diverso da null), "$gt" (maggiore di) e "$lt" (minore di) nel contesto delle query al database.
        if aqi_min == "":
            if aqi_max == "":
                tot_aqi = {"$ne": None, "$ne": None}
            else:
                temp2 = float(aqi_max)
                tot_aqi = {"$ne": None, "$lt": temp2}
        else:
            temp1 = float(aqi_min)
            if aqi_max == "":
                tot_aqi = {"$gt": temp1, "$ne": None}
            else:
                temp2 = float(aqi_min)
                tot_aqi = {"$gt": temp1, "$lt": temp2}
        if co_min == "":
            if co_max == "":
                tot_co = {"$ne": None, "$ne": None}
            else:
                temp2 = float(co_max)
                tot_co = {"$ne": None, "$lt": temp2}
        else:
            temp1 = float(co_min)
            if co_max == "":
                tot_co = {"$gt": temp1, "$lt": temp2}
            else:
                temp2 = float(co_max)
                tot_co = {"$ne": None, "$lt": temp2}
        print(country, city, tot_aqi, aqi_category, tot_co, aqi_co_category, lat, lng)
        try:
            lista = Query.eightParameter(country, city, tot_aqi, aqi_category, tot_co, aqi_co_category, lat, lng)
            airQuality = []
            for i in lista:
                airQuality.append(AirQuality.AirQuality(i))
            if len(airQuality) != 0:
                return render_template("test_query.html", list_air=changeResult(airQuality))
                print("effettuata")
            else:
                return render_template("test_query.html", response="Non esistono paesi con queste caratteristiche.")
                print("fallita ricerca")
        except:
            print("non entra")
            return render_template("test_query.html", response="Nessun paese trovato.", list_air=getResult())
    return render_template("test_query.html", response="Errore rilevato", list_air=getResult())


# Inserimento
@app.route("/test_query/insert_country", methods=['POST', 'GET'])
def insert_country():
    country = request.form['ins-country']
    city = request.form['ins-city']
    aqi_value = request.form['ins-aqi-value']
    aqi_category = request.form['ins-aqi-category']
    co_aqi_value = request.form['ins-co-value']
    co_aqi_category = request.form['ins-co-category']
    ozone_aqi_value = request.form['ins-ozone-value']
    ozone_aqi_category = request.form['ins-ozone-category']
    no2_aqi_value = request.form['ins-no2-value']
    no2_aqi_category = request.form['ins-no2-category']
    pm25_aqi_value = request.form['ins-pm25-value']
    pm25_aqi_category = request.form['ins-pm25-category']
    lat = request.form['ins-lat']
    lng = request.form['ins-lng']

    # Crea un dizionario con i valori estratti per costruire l'oggetto AirQuality
    object = {
        "_id": "",
        "Country": country,
        "City": city,
        "AQI Value": aqi_value,
        "AQI Category": aqi_category,
        "CO AQI Value": co_aqi_value,
        "CO AQI Category": co_aqi_category,
        "Ozone AQI Value": ozone_aqi_value,
        "Ozone AQI Category": ozone_aqi_category,
        "NO2 AQI Value": no2_aqi_value,
        "NO2 AQI Category": no2_aqi_category,
        "PM2_5 AQI Value": pm25_aqi_value,
        "PM2_5 AQI Category": pm25_aqi_category,
        "lat": lat,
        "lng": lng
    }

    # creo l'oggetto AirQuality ed invoco checkFormato
    air_quality = AirQuality.AirQuality(object)
    if AirQuality.checkFormato(air_quality):
        Query.insertCountry(air_quality)
        return render_template("test_query.html", response="Paese inserito correttamente", list_air=fullTable())
    else:
        return render_template("test_query.html", response="Valori mancanti", list_air=getResult())


@app.route("/test_query/update_country", methods=['POST', 'GET'])
def update_country():
    country = request.form['upd-country']
    new_country = request.form['upd-country2']
    city = request.form['upd-city']
    aqi_value = request.form['upd-aqi-value']
    aqi_category = request.form['upd-aqi-category']
    co_value = request.form['upd-co-value']
    co_category = request.form['upd-co-category']
    ozone_value = request.form['upd-ozone-value']
    ozone_category = request.form['upd-ozone-category']
    no2_value = request.form['upd-no2-value']
    no2_category = request.form['upd-no2-category']
    pm25_value = request.form['upd-pm25-value']
    pm25_category = request.form['upd-pm25-category']
    lat = request.form['upd-lat']
    lng = request.form['upd-lng']

    # Creazione dell'oggetto per l'aggiornamento
    obj = {
        "_id": "",
        "Country": country,
        "City": city,
        "AQI Value": aqi_value,
        "AQI Category": aqi_category,
        "CO AQI Value": co_value,
        "CO AQI Category": co_category,
        "Ozone AQI Value": ozone_value,
        "Ozone AQI Category": ozone_category,
        "NO2 AQI Value": no2_value,
        "NO2 AQI Category": no2_category,
        "PM2_5 AQI Value": pm25_value,
        "PM2_5 AQI Category": pm25_category,
        "lat": lat,
        "lng": lng
    }
    if country == "":
        return render_template("test_query.html", response="Errore! Nessun paese inserito.", list_air=getResult())
    else:
        # Trova i dati nel database
        result = Query.findCountryByName(country)
        value = []
        new = AirQuality.AirQuality(obj)
        for i in result:
            value.append(AirQuality.AirQuality(i))
        if len(value) != 0:
            if new_country == "":
                new_country = country
            if new.Country == "":
                new.Country = value[0].Country
                new_country = value[0].Country
            if new.City == "":
                new.City = value[0].City
            if new.aqi_value == "":
                new.aqi_value = value[0].aqi_value
            if new.aqi_category == "":
                new.aqi_category = value[0].aqi_category
            if new.co_aqi_value == "":
                new.co_aqi_value = value[0].co_aqi_value
            if new.co_aqi_category == "":
                new.co_aqi_category = value[0].co_aqi_category
            if new.ozone_aqi_value == "":
                new.ozone_aqi_value = value[0].ozone_aqi_value
            if new.ozone_aqi_category == "":
                new.ozone_aqi_category = value[0].ozone_aqi_category
            if new.no2_aqi_value == "":
                new.no2_aqi_value = value[0].no2_aqi_value
            if new.no2_aqi_category == "":
                new.no2_aqi_category = value[0].no2_aqi_category
            if new.pm25_aqi_value == "":
                new.pm25_aqi_value = value[0].pm25_aqi_value
            if new.pm25_aqi_category == "":
                new.pm25_aqi_category = value[0].pm25_aqi_category
            if new.lat == "":
                new.lat = value[0].lat
            if new.lng == "":
                new.lng = value[0].lng

            # Aggiorna i dati nel database
            Query.updateCountry(new_country, new)

            return render_template("test_query.html", response="Aggiornamento effettuato", list_air=fullTable())
        else:
            return render_template("test_query.html", response="Aggiornamento non effettuato.",
                                   list_air=getResult())


@app.route("/test_query/delete_country", methods=['POST', 'GET'])
def delete_query():
    if request.method == 'POST':
        # Ottieni il nome del paese da eliminare
        country = request.form['demo-country-id']

        if country == "":
            # Se il nome del paese è vuoto, mostra un messaggio di errore
            return render_template("test_query.html", response="Nessun paese rilevato da eliminare",
                                   list_air=getResult())
        else:
            # Cerca il paese nel database
            result = Query.findCountryByName(country)
            value = None
            for i in result:
                value = result
            if value is not None:
                # Se il paese è presente nel database, elimina il documento corrispondente
                Query.deleteCountry(country)
                return render_template("test_query.html", response="Eliminazione effettuata", list_air=fullTable())
                print("Eliminazione effettuata")
            else:
                # Se il paese non è presente nel database, mostra un messaggio di errore
                return render_template("test_query.html", response="Eliminazione non effettuata", list_air=getResult())
                print("Eliminazione non effettuata")


if __name__ == "__main__":
    app.run(debug=True)
