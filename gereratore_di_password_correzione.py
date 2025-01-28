import string
from random import randint

chars: str = string.ascii_letters
chars_cleaned: str = chars.replace ("O", "").replace ("l", "").replace ("i", "")
digits: str = string.digits
digits_cleanded: str = digits.replace ("0", "").replace("1", "")
symbols: str = string.punctuation


print( """ scegli una voce dal menu: 
      1. genera una password con le opzioni di default
      2. procedura guidata per la creazione di una password personalizzata
      q. esci 
""")

while True:
    user_choice: str = input()
    password: str = ""
    if user_choice == '1':
        password_length: int = 12
        chars_pool= chars_cleaned + digits_cleanded + symbols
        chars_pool_length: int = len(chars_pool)
        for _ in range(password_length):
            random_position = randint(0, chars_pool_length - 1)
            password = password + chars_pool[random_position]
        print(f"\n La password Generata è: {password}\n")
    elif user_choice == '2':
        print("Benvenuto nella procedura guidata per generare una password personalizzata.")
        password_length = 0
        while password_length < 8:
            print("Il numero di caratteri minimo è 8.")
            password_length: int = int(input("Quanti caratteri vuoi nella password? (minimo 8)"))
        
        use_digit = ""
        while use_digit != "s" and use_digit != "n":
            use_digit =input("vuoi usare i numeri? (s/n)")
            if use_digit != "s" and use_digit != "n":
                print ("Le risposte possibili sono 's' e 'n'.")
                
        use_symbols = ""
        while use_symbols != "s" and use_symbols != "n":
            use_symbols =input("vuoi usare i caratteri speciali? (s/n)")
            if use_symbols != "s" and use_symbols != "n":
                print ("Le risposte possibili sono 's' e 'n'.")
        
        if use_digit == "s" and use_symbols == "s":
            chars_pool = chars_cleaned + digits_cleanded + symbols
        elif use_digit == "s" and use_symbols == "n":
            chars_pool = chars_cleaned + digits_cleanded
        elif use_digit == "n" and use_symbols == "s":
            chars_pool = chars_cleaned + symbols
        else:
            chars_pool = chars_cleaned
        
        chars_pool_length: int = len(chars_pool)
        for _ in range(password_length):
            random_position = randint(0, chars_pool_length - 1)
            password = password + chars_pool[random_position]
        print(f"\n La password Generata è: {password}\n")
            
    elif user_choice == 'q':
        print("Arrivederci!")
        quit(0)
    else:
        print("Scelta non valida. Riprova.")