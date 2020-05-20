#! /usr/bin/python
# Author:   @BlankGodd

import requests
import ast, json
from bs4 import BeautifulSoup
import re


class BLyrics:

    def __init__(self):
        with open('info.txt', 'r') as f:
            tok = ast.literal_eval(f.read())

        self.access_token = tok['access_token']
        self.root = 'https://api.genius.com'

    def search(self, search_str):
        path = 'search/'
        request_uri = '/'.join([self.root,path])
        print(request_uri + search_str)
        print()

        params = {'q': search_str}
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}

        response = requests.get(request_uri, params=params, headers=headers)
        print(response.status_code)
        return response.text

    def search_song(self, search_str):
        song = self.search(search_str)
        
        # number of songs
        num = len(song['response']['hits'])
        songs = []
        # title, song_id, artist, artist_id, lyrics url,
        for i in range(num):
            title = song['response']['hits'][i]['result']['title']
            song_id = song['response']['hits'][i]['result']['id']
            artist = song['response']['hits'][i]['result']['primary_artist']['name']
            artist_id = song['response']['hits'][i]['result']['primary_artist']['id']
            lyrics_url = song['response']['hits'][i]['result']['url']
            ls = (title, song_id, artist, artist_id, lyrics_url)
            songs.append = ls
        print()
        for k in range(len(songs)):
            print(k+1,': ',songs[k][0], 'by', songs[k][2])

        print()
        rank = int(input('Pick the number for intended song:\n'))
        ranked_song = songs[rank-1]
        print(ranked_song[0], 'by', ranked_song[2])
        print('Getting info...')
        
        # say we have a song id for no role models
        song_id = ranked_song[1]
        path = 'songs/{}'.format(song_id)
        request_uri = '/'.join([self.root,path])

        params = {'text_format':'plain'}
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}
        response = requests.get(request_uri, params=params, headers=headers)
        if response.status_code == 200:
            print('Request successful...')
        information = response.text
        # after getting this we extract the info we need
        print()
        print('Getting Lyrics...')
        url = ranked_song[4]
        response2 = requests.get(url)
        if response.status_code == 200:
            print('Request successful...')
        # i need to understand this part     
        html = BeautifulSoup(response2.text, 'html.parser')
        lyrics = html.find('div', class_='lyrics').get_text()
        # and this part too
        lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
        description = information['response']['song']['description']['plain']
        print()
        print('Title: ',ranked_song[0]) 
        print('Artist: ',ranked_song[2])
        print()
        print('Description: 'description)
        print()
        print('Lyrics: 'lyrics)

    def search_artist(self, artist):
        artist_ = self.search(artist)



b = BLyrics()
x = b.search_song('No Role Modelz')
with open('number_456.json', 'w') as at:
    json.dump(x, at)


