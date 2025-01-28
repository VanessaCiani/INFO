#Nome: Vanessa Ciani
#Partner: Fabio Monaco

import random

# Funzione per generare la sequenza segreta+
def genera_sequenza():
    return random.sample(range(1, 7), 4)

# Funzione per dare il feedback sui tentativi
def valuta_tentativo(sequenza_segreta, tentativo):
    giusti_posizione = 0
    giusti_altro_posto = 0
    
    # Copia della sequenza segreta per confronti
    sequenza_segreta_copy = sequenza_segreta[:]
    tentativo_copy = tentativo[:]
    
    # Verifica i numeri giusti e al posto giusto
    for i in range(4):
        if tentativo[i] == sequenza_segreta[i]:
            giusti_posizione += 1
            sequenza_segreta_copy[i] = None  # Rimuove il numero trovato
            tentativo_copy[i] = None  # Rimuove il numero trovato
    
    # Verifica i numeri giusti ma al posto sbagliato
    for i in range(4):
        if tentativo_copy[i] is not None and tentativo_copy[i] in sequenza_segreta_copy:
            giusti_altro_posto += 1
            sequenza_segreta_copy[sequenza_segreta_copy.index(tentativo_copy[i])] = None  # Rimuove il numero trovato
    
    return giusti_posizione, giusti_altro_posto

def gioco():
    print("Scegli la difficoltà:")
    print("1. Facile (15 tentativi)")
    print("2. Intermedio (10 tentativi)")
    print("3. Difficile (7 tentativi)")
    difficolta = int(input("Inserisci il numero della difficoltà: "))
    
    if difficolta == 1:
        tentativi_max = 15
    elif difficolta == 2:
        tentativi_max = 10
    else:
        tentativi_max = 7

    # Genera la sequenza segreta
    sequenza_segreta = genera_sequenza()

    print(f"\nHai {tentativi_max} tentativi per indovinare la sequenza segreta composta da 4 numeri distinti tra 1 e 6.")
    
    for tentativo_numero in range(1, tentativi_max + 1):
        print(f"\nTentativo {tentativo_numero}/{tentativi_max}:")
        tentativo = []
        
        # Il giocatore inserisce i numeri uno alla volta
        for i in range(4):
            while True:
                try:
                    numero = int(input(f"Inserisci il numero {i + 1} (tra 1 e 6): "))
                    if numero < 1 or numero > 6:
                        print("Il numero deve essere tra 1 e 6.")
                    elif numero in tentativo:
                        print("I numeri devono essere distinti.")
                    else:
                        tentativo.append(numero)
                        break
                except ValueError:
                    print("Devi inserire un numero valido.")
        
        # Valuta il tentativo
        giusti_posizione, giusti_altro_posto = valuta_tentativo(sequenza_segreta, tentativo)
        
        # Controlla se il giocatore ha indovinato
        if giusti_posizione == 4:
            print("\nCongratulazioni! Hai indovinato la sequenza!")
            break
        else:
            print(f"Numeri giusti al posto giusto: {giusti_posizione}")
            print(f"Numeri giusti ma al posto sbagliato: {giusti_altro_posto}")
    
    else:
        # Se il ciclo finisce senza indovinare
        print(f"\nHai esaurito i tentativi. La sequenza segreta era: {sequenza_segreta}")

# Avvia il gioco
gioco()