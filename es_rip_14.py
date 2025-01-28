#esercizio 14

num_a = int(input("dimmi un numero "))
num_b = int(input("dimmi un'altro numero "))

prodotto = num_a * num_b

if prodotto > 10:
    print("la diferenza è di : ", str(num_a - num_b))
    
elif prodotto <= 10:
    print("la somma è di : ", str(num_a + num_b))