#esercizio 15
#sommare tutti i primi 100 numeri naturali
contatore = 0
n = 0

for somma in range(1, 101):
    n += 1
    contatore = contatore + n
    
print(contatore)