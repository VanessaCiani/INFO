#esercizio 18
#dati i nomi di 3 studenti la distanza in km da casa a scuola, visualizza il nome degli studenti che abitano in comuni più distanti di 30km

nome1 = input("come si chiama la prima persona? ")
nome2 = input("come si chiama la seconda persona? ")
nome3 = input("come si chiama la terza persona? ")

distanza1 = float(input("quanti km è da casa a scuola per " + nome1 + " ? "))
distanza2 = float(input("quanti km è da casa a scuola per " + nome2 + " ? "))
distanza3 = float(input("quanti km è da casa a scuola per " + nome3 + " ? "))

if distanza1 > 30 and distanza2 > 30 and distanza3 > 30:
    print(nome1 + " e " + nome2 + " e " + nome3 + " abitano in comuni più distanti di 30km")
    
elif distanza1 > 30 and distanza2 > 30:
    print(nome1 + " e " + nome2 + " abitano in comuni più distanti di 30km")

elif distanza1 > 30 and distanza3 > 30:
    print(nome1 + " e " + nome3 + " abitano in comuni più distanti di 30km")

elif distanza2 > 30 and distanza3 > 30:
    print(nome2 + " e " + nome3 + " abitano in comuni più distanti di 30km")

elif distanza1 > 30:
    print(nome1 + " abita in comuni più distanti di 30km")

elif distanza2 > 30:
    print(nome2 + " abita in comuni più distanti di 30km")

elif distanza3 > 30:
    print(nome3 + " abita in comuni più distanti di 30km")

