#esercizio 17

sq1 = int (input("quanti punti has fatto la prima squadra? "))
sq2 = int (input("quanti punti has fatto la seconda squadra? "))

if sq1 > sq2:
    print("la prima squadra ha vinto!")
elif sq1 < sq2:
    print("la seconda squadra ha vinto!")
else:
    print("impossibile pareggiare!")