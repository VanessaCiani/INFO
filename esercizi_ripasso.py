#esercizio 1
#Leggi una sequenza di numeri; al primo zero incontrato deterina quanti numeri sono sai letti e la loro somma.

contatore = 1 
somma = 0

numeri = int(input("dimmi un numero: "))

while numeri != 0:
    somma = somma + numeri
    contatore= contatore + 1
    numeri = int(input("dimmi un numero: "))

if numeri == 0:
    print("hai letto", contatore, "numeri")
    print("la loro somma e':", somma)
    
