import libreria_dadi

n = int(input("quanti dadi vuoi lanciare"))
m = int(input("da quante facce?"))

print(f"il dado maggiore è {libreria_dadi.vantaggio(n, m)}")