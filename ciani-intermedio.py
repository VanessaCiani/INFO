#verifica livelo base
#Ogni volta che viene inserita una parola il programma deve contare: quante vocali ci sono nella parola e aggiungerlo al totale di vocali complessive inserite fino a quel momento;

contatore_doppie = 0
contatore_vocali = 0
contatore_palindrome = 0
parola = input("dimmi una parola ")
parola_inversa = parola.__reversed__

for i in range(i):
    if "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U" in parola:
        contatore_vocali= contatore_vocali + 1
        input(contatore_vocali, "dimmi un'altra parola ")
    elif "aa" or "bb" or "cc" or "dd" or "ee" or "ff" or "gg" or "hh" or "ii" or "jj" or "kk" or "ll" or "mm" or "nn" or "oo" or "pp" or "qq" or "rr" or "ss" or "tt" or "uu" or "vv" or "ww" or "xx" or "yy" or "zz" in parola:
        contatore_doppie = contatore_doppie + 1
        input(contatore_doppie, "dimmi un'altra parola ")
    elif parola == parola_inversa:
        contatore_palindrome = contatore_palindrome + 1
        input(contatore_palindrome, "dimmi un'altra parola ")
    elif parola == "0":
        quit()