import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

URL = "https://danepubliczne.imgw.pl/api/data/meteo/format/xml"

# wybrane stacje (możesz zmienić nazwy)
SELECTED_STATIONS = {
    "KRAKÓW-BALICE",
    "KIELCE-SUKÓW",
    "SANDOMIERZ"
}

response = requests.get(URL)
response.raise_for_status()

root = ET.fromstring(response.content)

stations = []
wind_speeds = []

for station in root.findall("item"):
    name = station.findtext("nazwa_stacji")
    wind = station.findtext("wiatr_srednia_predkosc")


    if name in SELECTED_STATIONS and wind is not None:
        stations.append(name)
        wind_speeds.append(float(wind))

plt.figure()
plt.bar(stations, wind_speeds)
plt.xlabel("Station")
plt.ylabel("Wind speed [m/s]")
plt.title("Wind speed at selected IMGW stations")
plt.show()
