import pandas as pd
import csv

# Il codice pulisce un dataset sulla qualità dell'aria, eliminando le righe con valori mancanti e creando un nuovo file CSV senza righe mancanti.

def delete_null_item():
    # Prendo il dataset world_air_quality.csv e lo memorizzo nella variabile air_quality
    air_quality = pd.read_csv("world_air_quality.csv")

    # Uso dropna di pandas per eliminare le righe con almeno un valore mancante
    air_quality.dropna(axis='index', how='any', inplace=True)

    # Apro un nuovo file CSV chiamato world_air_quality_cleaned e itero su ogni riga del DataFrame air_quality per scriverle nel file
    with open('world_air_quality_cleaned.csv', 'w', encoding="UTF-8", newline='') as file:
        writer = csv.writer(file)

        writer.writerow([
            "Country",
            "City",
            "AQI Value",
            "AQI Category",
            "CO AQI Value",
            "CO AQI Category",
            "Ozone AQI Value",
            "Ozone AQI Category",
            "NO2 AQI Value",
            "NO2 AQI Category",
            "PM2_5 AQI Value",
            "PM2_5 AQI Category",
            "lat",
            "lng"
        ])

        for i in range(0, len(air_quality)):
            try:
                writer.writerow([
                    air_quality["Country"][i],
                    air_quality["City"][i],
                    air_quality["AQI Value"][i],
                    air_quality["AQI Category"][i],
                    air_quality["CO AQI Value"][i],
                    air_quality["CO AQI Category"][i],
                    air_quality["Ozone AQI Value"][i],
                    air_quality["Ozone AQI Category"][i],
                    air_quality["NO2 AQI Value"][i],
                    air_quality["NO2 AQI Category"][i],
                    air_quality["PM2.5 AQI Value"][i],
                    air_quality["PM2.5 AQI Category"][i],
                    air_quality["lat"][i],
                    air_quality["lng"][i]
                ])
            except Exception as e:
                print(f"Errore durante la scrittura della riga {i}: {str(e)}")

delete_null_item()
