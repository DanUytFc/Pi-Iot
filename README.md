# RPI-Gone-Fishing
## Beschrijving
Bewaking van een verblijfplaats is ingeburgerd via commerciële oplossingen gebaseerd op internet deurbel, ip camera's ...

Deze zijn afhankelijk van de aanwezigheid van netspanning(voor voeding van de apparaten) en een werkend internet(voor toegang op afstand) op deze locaties. 

Dit project implementeerd een prototype voor ***monitoring van netspanning en internet*** gebaseerd op een ***Raspberry Pi***.
## Bronnen
Inspiratie heb ik helaas opgedaan tijdens de overstromingen in de Ardennen afgelopen jaar. Noodgedwongen waren we verplicht onze verblijfplaats te verlaten toen deze getroffen werd. 

Zowel de elektriciteit en internet werden uitgeschakeld uit veiligheid. Hierdoor was het niet meer mogelijk om op afstand de geinstalleerde ip camera te bereiken. 

Op YouTube is er een video over [How to Detect Power & Internet Outages With My Raspberry Pi Python Project](https://www.youtube.com/watch?v=Tj0mNO3ZDao/) die als referentie zal gebruikt worden. 
## Hardware
Aangezien hardware levering een probleem is in deze pandemie periode zal ik terugvallen op de beschikbare [Raspberry Pi 2 Model B Rev 1.1](Images/RASPBERRY_PI_2_B_06.jpg). 
- Eenmaal het prototype op punt staat, is het de bedoeling om over te schakelen naar de Raspberry Pi Zero W. Dit maakt echter geen deel uit van dit project. 

Zodra hardware terug beschikbaar is kunnen volgende uitbreidingen overwogen worden: 
1. [4G/3G/2G/GSM/GPRS/GNSS HAT](Images/Raspberry_PI_LTE.png) om tijdelijk over te schakelen naar mobiel data GSM netwerk indien internet via vast ethernet weggevallen is. Als alternatief zal ondertussen de beschikbare [Huawei E8372h-153 - 4G Dongle](Images/Huawei_E8372h-153-4G_Dongle.png) in combinatie met de [SONY UWA-BR100 USB Wi-Fi adapter](Images/SONY_USB_Wifi.jpg) gebruikt worden. 
2. [Uninterruptible Power Supply(UPS) HAT](Images/PiJuice_HAT.png) om 5V voeding tijdelijk te voorzien indien de netspanning weggevallen is.
## Software
Als basis voor de software zal de GitHub Python source [Outage-Detector](https://github.com/fabytm/Outage-Detector/) gelinkt aan het YouTube referentie project gebruikt worden. 

Deze zal geimplementeerd worden op de meest recente ***Bullseye Raspberry Pi OS.*** 
>Noteer eveneens welke aanpassingen je aan welke configuratiebestanden je hebt doorgevoerd.
### Eigen scripts en programma's
Overzicht van de taaklijst: 
- [ ] Installatie en configuratie Outage-Detector. 
- [ ] Notificatie via email. 
- [ ] Notificatie via push berichten. 
- [ ] Notificatie via IFTTT.
- [ ] Automatische failover naar mobiel data GSM network indien internet via vast ethernet weggevallen is. 
>Sla je als apparte bestanden op in deze repository.
## Afbeeldingen toevoegen
1.  Raspberry Pi 2 Model B Rev 1.1:

![Raspberry Pi 2 Model B Rev 1.1](Images/RASPBERRY_PI_2_B_06.jpg)

2. Raspberry Pi Zero W:

![Raspberry Pi Zero W](Images/Raspberry_PI_Zero_W.jpg)

3. PiJuice HAT - A portable Power Platform for Every Raspberry Pi:

![PiJuice HAT](Images/PiJuice_HAT.png)

4. 4G/3G/2G/GSM/GPRS/GNSS HAT voor Raspberry Pi - LTE CAT4:

![Raspberry Pi - LTE](Images/Raspberry_PI_LTE.png)

5. Huawei E8372h-153 - 4G Dongle:

![Huawei - 4G Dongle](Images/Huawei_E8372h-153-4G_Dongle.png)

6. SONY UWA-BR100 USB Wi-Fi adapter: 

![SONY - USB Wifi](Images/SONY_USB_Wifi.jpg)
