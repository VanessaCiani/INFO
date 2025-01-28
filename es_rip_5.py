from random import randint

numero_tentativi = 20
hai_vinto = False

def genera_numero():
    return randint(1000, 9999)

numero_casuale = genera_numero()
inizio = input("Vuoi iniziare il gioco? (SI o NO)")

while inizio == "SI":
    numero_tentativi = 20
    while numero_tentativi > 0:
        numero_tentativi -= 1
        numero = int(input("Dammi un numero da indovinare"))
        if numero == numero_casuale:
            hai_vinto = True
            print("Hai vinto")
        elif numero < numero_casuale:
            print("Il numero da indovinare è più grande")
        else:
            print("Il numero da indovinare è più piccolo")
        if numero_tentativi == 0 :
            print("Hai finito i tentativi!!!")
    inizio = input("Vuoi ricominciare il gioco? (SI o NO)")
    
if inizio == "NO":
    print("Esci")
    