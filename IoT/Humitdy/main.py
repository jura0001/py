from iot_package.sensors import Sensors
import time

# Za ovaj zadatak koristite Simulator koji
# se nalazi u mapi "simulator" - simulator.py.
# Također, kako bi čitali podatke sa senzora potrebno je
# koristiti klasu `Sensors` koja je već uključena u ovoj datoteci.

# Napišite skriptu koja svake sekunde (1s) sa senzora pročita
# temperaturu i vlagu.
# Na temelju pročitanih vrijednosti skripta treba na
# zaslon (display) ispisati pripadajuću poruku.
# Idealna temperatura je u rasponu od 18-24,
# a idealna vlaga u rasponu od 40-60.
# Ako su temperatura i vlaga u idealnom rasponu treba na zaslon ispisati:
#   - "IDEALNO".
# Ako je temperatura izvan raspona treba ispisati:
#   - "GRIJEM" ako je ispod ili "HLADIM" ako je iznad.
# Ako je vlaga izvan raspona treba ispisati:
#   - "OVLAZUJEM" ako je ispod ili "SUSIM" ako je iznad.
# Ako su i temperatura i vlaga izvan raspona potrebno je ispisati obje poruke.

#def check_conditions(temp, humidity):
#     if temp >=18 and temp <=24:
#         if humidity >=40 and humidity <=60:
#             return "IDEALNO"
#         elif humidity <40:
#             return "OVLAZUJEM"
#         else:
#             return "SUSIM"
#     elif temp <18:
#         if humidity >=40 and humidity <=60:
#             return "GRIJEM"
#         elif humidity <40:
#             return "GRIJEM I OVLAZUJEM"
#         else:
#             return "GRIJEM I SUSIM"
#     elif temp >24:
#         if humidity >=40 and humidity <=60:
#             return "HLADIM"
#         elif humidity <40:
#             return "HLADIM I OVLAZUJEM"
#         else:
#             return "HLADIM I SUSIM"

def check_conditions(temp, vlaga):
    stanje_temp = "IDEALNO" if 18 <= temp <= 24 else "GRIJEM" if temp < 18 else "HLADIM"
    stanje_vlage = "" if 40 <= vlaga <= 60 else " I OVLAZUJEM" if vlaga < 40 else " I SUSIM"
    
    return stanje_temp + stanje_vlage

def main():
    sensors = Sensors()


    while True:
        temp= sensors.get_temperature()
        humidity = sensors.get_humidity()
        sensors.show_message(check_conditions(temp,humidity))
        time.sleep(1)

if __name__ == "__main__":
    main()
