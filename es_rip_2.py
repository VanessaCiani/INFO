#esercizio 2
#scrii un programma che, letto in ingresso il numero di righe da stampare

righe = int (input ("quante righe vuoi nella piramide"))
def triangolo1 (n):
    numero = 1
    for i in range (1, n+1):
        for f in range (i):
            print(numero, end = " ")
            numero = numero + 1
        print()

triangolo1(righe)
            