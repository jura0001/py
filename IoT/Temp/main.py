from iot_package.sensors import Sensors
import time


# Za ovaj zadatak koristite Simulator koji
# se nalazi u mapi "simulator" - simulator.py.
# Također, kako bi čitali podatke sa senzora potrebno je
# koristiti klasu `Sensors` koja je već uključena u ovoj datoteci.

# Napišite skriptu koja svake sekunde (1s) sa senzora pročita
# temperaturu.
# Na temelju pročitanih vrijednosti skripta treba na
# zaslon (display) ispisati pripadajuću poruku.
# Idealna temperatura je u rasponu od 18-24.
# Ako je temperatura idealnom rasponu treba na zaslon ispisati:
#   - "IDEALNO".
# Ako je temperatura izvan raspona treba ispisati:
#   - "HLADNO" ako je ispod ili "VRUCE" ako je iznad.



def main():
   
    sensors = Sensors()
    while True:

        temp = sensors.get_temperature()
        # TODO: Potrebno je implementirati zadano ponasanje
        if 18 <= temp <= 24:
            message= "IDEALNO"
        elif temp <18:
            message="HLADNO"
        else:
            message="VRUCE"
        sensors.show_message(message)
        time.sleep(1)
        print(temp)

if __name__ == "__main__":
    main()
