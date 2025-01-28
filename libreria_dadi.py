#1 -restituire una lista dei risultati di 'n' dadi da 'm' facce;
import random

def lancia_dadi(n, m):
    risultato = []
    for _ in range(n):
        risultato.append(random.randint(1, m))
    return risultato

#2 -restituire la somma del lancio di 'n' dadi da 'm' facce;
import random

def somma_dadi(n, m):
    somma = 0
    for _ in range(n):
        numero_casuale = random.randint(1, m)
        somma += numero_casuale
    return somma

#3 -restituire la somma del lancio 'n' dadi da 'm' facce, ricevendo come input una stringa nel formato `ndm`
import random

def somma_dadi2(ndm):
    somma = 0
    separatore = ndm.split("d")
    n = int(separatore[0])
    m = int(separatore[1])
    for _ in range(n):
        numero_casuale = random.randint(1, m)
        somma += numero_casuale
    return somma

#4 -restituire il risultato di un lancio con vantaggio di $n$ dadi da $m$ facce (ovvero dove viene restituito solo il dado con il valore più alto);
import random

def vantaggio(n, m):
    risultato = []
    for _ in range(n):
            risultato.append(random.randint(1, m))
    print(risultato)
    return max(risultato)

#5 -restituire una lista dei risultati di $x$ lanci di $n$ dadi da $m$ facce lanciati con vantaggio, ricevendo come parametri $x$ e la stringa `ndm`;
#6 -restituire la somma del lancio di $x$ lanci di $n$ dadi da $m$ facce lanciati con vantaggio, ricevendo come parametri $x$ e la stringa `ndm`;    