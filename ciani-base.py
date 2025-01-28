#Nome: Vanessa
#Cognome: Ciani
#Classe: 3A INFO
#Data: 18/12/2024
from random import randint


lista_base = ["Tony Stark", "Steve Rogers", "Thor Odinson", "Henry Pym", "Bruce Banner", "Clint Barton", "Wanda Maximoff", "T'Challa", "Natasha Romanoff", "Henry McCoy", "Susan Carol", "Monica Rambeau"]
listaregalo_give = []
listaregalo_receive = []

for i in lista_base:
    listaregalo_give.append(i)
    listaregalo_receive.append(i)

while (len(lista_base)) > 0 and (len(listaregalo_receive)) :   
    contatoreregalo_give = len(listaregalo_give) - 1
    contatoreregalo_receive = len(listaregalo_receive) - 1
    pers1 = 0
    pers2 = 0
    if (len(lista_base)) > 0 and (len(listaregalo_receive)) :  
        while pers1 == pers2:
            pers1 = randint(0, contatoreregalo_give)
            pers2 = randint(0, contatoreregalo_receive)
    else:
        pers1 = 0
        pers2 = 0
    part1 = listaregalo_give[pers1]
    part2 = listaregalo_receive[pers2]
    
    print(f"{part1} farà il regalo a {part2}")
    listaregalo_give.remove(part1)
    listaregalo_receive.remove(part2)
