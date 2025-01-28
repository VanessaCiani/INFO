quadrato_cerchio = input("Vuoi calcolare l'area del cerchio o del quadrato? (Cerchio/Quadrato)")
if quadrato_cerchio == "Cerchio":
    raggio = float(input("Qual è il raggio del cerchio?"))
    area = 3.14 * (raggio ** 2)
else: 
    lato = float(input("Qual è il lato del quadrato?"))
    area = lato ** 2

print(f"L'area è {area}")