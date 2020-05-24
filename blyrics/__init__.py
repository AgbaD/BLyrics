#!/usr/bin/python
# Author:   @BlankGodd

from pyfiglet import Figlet


banner = Figlet(font='standard')
print(banner.renderText("BLyrics"))

print()
print("Welcome To BLyrics")
print('To get information about songs and artists')
print()

print('Information')
print('1: Search Artist')
print('2: Search Song Lyrics')
print()

def start():
    cod = int(input('Enter number to proceed:\n'))
    if cod == 1:
        pass

song = input('Enter name of song: \n')
Genius_Lyrics.search_song(song)
