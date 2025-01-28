import libreria_dadi

n = int(input("quanti dadi vuoi lanciare?"))
m = int(input("da quante facce?"))

risultato = libreria_dadi.somma_dadi(n, m)
print(f"La somma dei {n} dadi da {m} facce è: {risultato}")