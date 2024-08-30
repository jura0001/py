from iot_package.sensors import Sensors
import time

# Za ovaj zadatak koristite Simulator koji
# se nalazi u mapi "simulator" - simulator.py.
# Također, kako bi čitali podatke sa senzora potrebno je
# koristiti klasu Sensors koja je već uključena u ovoj datoteci.

# Napišite skriptu koja svake sekunde (1s) sa senzora pročita
# temperaturu i tlak zraka.
# Na temelju pročitanih vrijednosti skripta treba na
# zaslon (display) ispisati pripadajuću poruku.
# Idealna temperatura je u rasponu od 10-24 (°C),
# a idealan tlak zraka u rasponu od 101200 - 101400 (Pa).
# Ako su temperatura i tlak u idealnom rasponu treba na
# zaslon ispisati:
#   - "MOZETE IZACI".
# Ako je temperatura izvan raspona treba ispisati:
#   - "OSTANITE DOMA".
# Ako je tlak izvan raspona treba ispisati:
#   - "OSTANITE DOMA".
# Ako su i temperatura i tlak izvan raspona
# potrebno je preferirati "OSTANITE DOMA"


def main():

    sensors = Sensors()

    while True:
        temp = sensors.get_temperature()
        humidty = sensors.get_humidity()

        if temp >= 10 and temp <=24 and humidty >= 1012 and humidty <=1014: 
            message="MOZETE IZACI"
        else:
            message="OSTANITE DOMA"
        sensors.show_message(message)
        time.sleep(1)

if __name__ == "__main__":
    main()