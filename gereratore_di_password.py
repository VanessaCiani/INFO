import string
from random import randint

chars: str = string.ascii_letters
chars_cleaned: str = chars.replace ("O", "").replace ("l", "").replace ("i", "")
digits: str = string.digits
digits_cleanded: str = digits.replace ("0", "").replace("1", "")
symbols: str = string.punctuation


print( """ scegli una voce dal menu: 
      1. genera una password con me opzioni di default
      2. procedura guidata per la creazione di una password personalizzata
      q. esci 
""")

while True:
    user_choice: str = input()

    if user_choice == '1':
        password_length: int = 12
        chars_pool= chars_cleaned + digits_cleanded + symbols
        chars_pool_length: int = len(chars_pool)
        for _ in range(password_length):
            random_position = randint(0, chars_pool_length - 1)
            password = password + chars_pool [random_position]
        print(password)
    elif user_choice == '2':
        print()
        
    elif user_choice == 'q':
        print("Arrivederci!")
        quit(0)
    