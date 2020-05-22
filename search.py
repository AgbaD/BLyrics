#! /usr/bin/python
# Author:   @BlankGodd

import requests
import ast, json
from bs4 import BeautifulSoup
import re


class Genius_Lyrics:

    def __init__(self):
        with open('info.txt', 'r') as f:
            tok = ast.literal_eval(f.read())

        self.access_token = tok['access_token']
        self.root = 'https://api.genius.com'

    def search(self, search_str):
        path = 'search/'
        request_url = '/'.join([self.root,path])
        print(request_url + search_str)
        print()

        params = {'q': search_str}
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}

        response = requests.get(request_url, params=params, headers=headers)
        print(response.status_code)
        return response.text

    def search_artist_song(self, song_title, artist_name):
        pass

    def search_song(self, search_str):
        song = self.search(search_str)
        song = json.loads(song)
        
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
            songs.append(ls)
        print()
        for k in range(len(songs)):
            print(k+1,': ',songs[k][0], 'by', songs[k][2])

        print()
        print('If preferred song not in list, enter -1')
        rank = int(input('Pick the number for intended song:\n'))
        print()
        if rank == -1:
            name_of_artist = input('Enter name of artist: ')
            return self.search_artist_song(search_str, name_of_artist)
        else:
            pass
        ranked_song = songs[rank-1]
        print(ranked_song[0], 'by', ranked_song[2])
        print()
        print('Getting info...')
        
        # say we have a song id for no role models
        song_id = ranked_song[1]
        path = 'songs/{}'.format(song_id)
        request_url = '/'.join([self.root,path])

        params = {'text_format':'plain'}
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}
        response = requests.get(request_url, params=params, headers=headers)
        if response.status_code == 200:
            print('Request successful...')
        information = response.text
        information = json.loads(information)
        # after getting this we extract the info we need
        print()
        print('Getting Lyrics...')
        url = ranked_song[4]
        response2 = requests.get(url)
        if response.status_code == 200:
            print('Request successful...')
            print()
        # i need to understand this part     
        html = BeautifulSoup(response2.text, 'html.parser')
        lyrics = html.find('div', class_='lyrics').get_text()
        # and this part too
        lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
        description = information['response']['song']['description']['plain']
        final = {'Title' : ranked_song[0], 'Artist' : ranked_song[2], 
            'Description' : description, 'Lyrics' : lyrics}

        return final

    def search_artist(self, search_str):
        artist_ = self.search(search_str)
        artist = json.loads(artist_)
        
        num = len(artist['response']['hits'])
        all_artist = []
        for i in range(num):
            name = artist['response']['hits'][i]['result']['primary_artist']['name']
            artist_id = artist['response']['hits'][i]['result']['primary_artist']['id']
            ls = (name, artist_id)
            all_artist.append(ls)
        for i in range(len(all_artist)):
            print(i+1, all_artist[i][0])

        print()
        print("If artist not on list, enter 'e-x'")
        try:
            rank = int(input('Pick the number of intended artist: \n'))
        except:
            return
        ranked_artist = all_artist[rank-1]
        print()
        artist_id = ranked_artist[1]
        print()
        print('Getting Info...')
        path = 'artists/{}'.format(artist_id)
        request_url = '/'.join([self.root, path])

        params = {'text_format':'plain'}
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}
        response = requests.get(request_url, params=params, headers=headers)
        if response.status_code == 200:
            print('Request successful...')
            print()
        information = response.text
        information = json.loads(information)

        aka = information['response']['artist']['alternate_names']
        twitter_name = information['response']['artist']['twitter_name']
        facebook_name = information['response']['artist']['facebook_name']
        instagram_name = information['response']['artist']['instagram_name']
        description = information['response']['artist']['description']['plain']
        akas = ','.join(aka)

        num = len(artist['response']['hits'])
        songs_by = []
        for i in range(num):
            song_title = artist['response']['hits'][i]['result']['title']
            songs_by.append(song_title)

        final = {'artist_name' : ranked_artist[0], 'Aliases' : akas, 
        'Twitter Handle' : twitter_name, 'Instagram Handle' : instagram_name, 
        'Facebook Name' : facebook_name, 'Description' : description,
        'songs' : songs_by}

        return final

        


if __name__ == '__main__':
    b = Genius_Lyrics()
    b.search_artist('Cole')


