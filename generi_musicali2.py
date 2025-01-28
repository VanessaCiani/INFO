# Name: Fabio Monaco
# Partner: Vanessa Ciani
# Date: 24/11/2024
# Class: 3A INFO
# Lab: MUSICAL ARTISTS AND GENRES Part 2 


#6: FUNZIONI - GENERI MUSICALI

def getGenres(times):
    print('\n')
    genres = []  

    for i in range(times):  
        genre = input(f"Inserisci il genere musicale #{i+1}: ") 
        genres.append(genre)  
    
    return genres  
genres = getGenres(3) 
#7: FUNZIONI - ARTISTI MUSICALI

def getArtists(music_genres):
    favorite_artists = []  

    for genre in music_genres:  
        artist = input(f"Qual è il tuo artista preferito nel genere '{genre}'? ")  
        favorite_artists.append(artist)  
        
    return favorite_artists  

artists = getArtists(genres)  

#8: FUNZIIONI - STAMPA PREFERITI

def printFavorites(music_genres, favorite_artists):
    print("I tuoi generi musicali preferiti sono:")
    for i in range(len(music_genres)):  
        print(f"{music_genres[i]} - Artista preferito: {favorite_artists[i]}")  

printFavorites(genres, artists)  

#9: FUNZIONI - STAMPA PERMUTAZIONI

def printPermutations(music_genres, favorite_artists):
    print("Permutazioni di generi musicali e artisti preferiti:")
    for genre in music_genres:  
        for artist in favorite_artists:  
            print(f"Genere: {genre} - Artista: {artist}")  

printPermutations(genres, artists)  

#10: FUNZIONI - PARLARE

def talkAboutMusic():
    num_genres = int(input("Quanti generi musicali preferiti hai? "))  
    genres = getGenres(num_genres)  
    artists = getArtists(genres)  
    printFavorites(genres, artists)  
    printPermutations(genres, artists)  

talkAboutMusic()  
talkAboutMusic()  

