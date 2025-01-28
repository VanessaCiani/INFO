import libreria_dadi

n = int(input("quanti dadi vuoi lanciare?"))
m = int(input("da quante facce?"))

risultato = libreria_dadi.lancia_dadi(n, m)
print(risultato)