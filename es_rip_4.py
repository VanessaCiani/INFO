#esercizio 4
#scrivi una procedura/metodo swap() che prenda in ingresso due interi e gli scambi. Scrivi un programma che utilizzi questa funzione
def swap(num1, num2):
    num1, num2 = num2, num1
    
    
num1 = input("dammi un numero: ")
num2 = input("dammi un altro numero: ")


print(num2, num1)