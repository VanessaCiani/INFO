from random import randint

def saluti(name):
    print(f"hello world i'm {name}")

def lancia_dado():
    valore_dado = randint(1, 6)
    print(f"Valore estratto: {valore_dado}")
    
def lancia_dadi(numero_dadi, facce):
    valore=0
    for _ in range (numero_dadi):
        valore +=randint(1, facce)
      
saluti("Vanessa")
saluti("Fabio")
numero_facce = int(input("Quante facce vuoi che il dado abbia?"))
lancia_dado(numero_facce)
lancia_dado(int(input("Quante facce vuoi che il dado abbia?")))