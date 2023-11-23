#1
from random import Random, random
from secrets import randbelow


nimi=input("Mis on sinu nimi?:")
if nimi=="Juku":
    print("Lähme kinos")
    vanus=int(input("Kui vana sa on?:"))
    if vanus<6:
        pilet="tasuta"
    if vanus>5 and vanus<15:
        pilet="lastepilet"
    if vanus>14 and vanus<66:
        pilet="täispilet"
    if vanus>65:
        pilet="soduspilet"
    if vanus<1 and vanus>99:
        pilet="viga andmetega"
else: 
    print("Ära mine kinno")

#2
a=input("Mis on esimese inimese nimi?:")
b=input("Mis on teine inimese nimi?:")
print(""+a+" ja "+b+", olete täna pinginaabrid!")

#3
pikk=float(input("Mis on toa pikk seinte pikkus?: "))
lühike=float(input("Mis on toa lühike seinte pikkus?: "))
S=pikk*lühike
print ("Põranda pindala on: " + S)
soov=input("Kas soovite remonti teha?: ").lower()
if soov=="yes" or soov=="jah":
   hind=float(input("Kui palju see ruutmeeter maksab?: "))
   vahetus=S*hind
   print("Põranda vahetamise hind on " +vahetus+ "eurot." )
else: 
    print("Remonti ei tehtud")

#4
alghind=Random
print("Alghind on" + alghind)
if alghind>700:
    soodus=alghind%30
    print("Soodus on" + soodus)
else:
    print("Hind on vähem kui 700")

#5
temperatuur=float(input("Mis on toas temperatuur?: "))
if temperatuur>18:
    print("Soovitav toasoojus talvel")
else:
    print("Toas on külm")

#6
pikkus=float(input("Mis on sinu pikkus?: "))
if pikkus>0 and pikkus<250:
    if pikkus<163:
        print("Sa oled lühike")
    if pikkus>162 and pikkus<177:
        print("Oled keskmist kasvu")
    if pikkus>176:
        print("Sa oled pikk")
else:
    print ("viga")

#7

#8



#date sheet
sp=date(int(input("Sünniaasta: ")),int(input(Sünnikuu: )),int(input("Sünnipäev: ")))
praegu=date.today().yeat #2023

if (praegu-sp.year)%10==0:#sp>date(2000,1,1):
    print("Juubel")
else: 
    print("-----")