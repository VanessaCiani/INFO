from math import gcd

#Problema 1:
def divisori(numero):
    divisori = []
    for i in range(1, numero+1):
        if numero % i == 0:
            divisori.append(i)
    return divisori

#Problema 2:
def NumPrimo(numero):
    if len(divisori(numero)) == 2:
        return True
    
#Problema 3:
def NumPrim(numero):
    num_primi = []
    for i in range (2, numero+1):
        if NumPrimo(i):
            num_primi.append(i)
    return num_primi

#Problema 4:
def coprimi(num1,num2):
    mcd = gcd(num1,num2)
    if mcd == 1:
        return True
    
#Problema 5:
def eulero(numero):
    contatore = 0
    for i in range(1, numero):
        if coprimi(i, numero):
            contatore += 1
    return contatore