#!/usr/bin/python
# Author:   @BlankGodd

import requests
import ast, json
from bs4 import BeautifulSoup
import re


class Search_Genius:
    """Songs, Artists and Search"""
    def __init__(self):
        """Constructor for search genius 

        Methods
            - search: to make a general search
            - search_song: searching for songs using song_id
                leverages the search method first
            - search_artist: searches for artist info using artist_id
                leverages the search method first
            - search_artist_song: searches for songs by artist
        """

        self.access_token = 'pX_ZcyoBxAKt8Z2F9oCOASPTzspv9er17wWCAPNIwIWcr5Lg_AyMRgGsx846LVAE'
        self.root = 'https://api.genius.com'

    def search(self, search_str):
        """To make a general query with the api
        
        Params:
            - search_str: value to be searched
        Returns:
            - response object
        """
        path = 'search/'
        request_url = '/'.join([self.root,path])
        print()

        params = {'q': search_str}
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 'application' : 'BLyrics',
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}

        i = 0
        while i < 3: # try reconnecting 2 times if status_code != 200
            try:
                response = requests.get(request_url, params=params, headers=headers)
                if response.status_code == 200:
                    return response.text
            except:
                pass
            i += 1
        return None

    def search_song(self, search_str):
        """Search songs

        Params:
            - song title
        Return:
            - dict object
            - information about song
            - song lyrics
        """
        song = self.search(search_str)
        if not song:
            return None
        song = json.loads(song)
        
        # number of songs
        num = len(song['response']['hits'])
        songs = []
        # title, song_id, artist, artist_id, lyrics url,
        for i in range(num):
            title = song['response']['hits'][i]['result']['title_with_featured']
            song_id = song['response']['hits'][i]['result']['id']
            artist = song['response']['hits'][i]['result']['primary_artist']['name']
            artist_id = song['response']['hits'][i]['result']['primary_artist']['id']
            lyrics_url = song['response']['hits'][i]['result']['url']
            ls = (title, song_id, artist, artist_id, lyrics_url)
            songs.append(ls)
        print()
        for k in range(len(songs)):
            print(k+1,':', songs[k][0], 'by', songs[k][2])

        print()
        print('If preferred song not in list, search artist name')
        try:
            rank = int(input('Pick the number for intended song:\n'))
        except:
            return None
        print()
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
        headers = {'Authorization': access_token, 'application' : 'BLyrics',
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}
        i = 0
        information = None
        while i < 3:
            try:
                response = requests.get(request_url, params=params, headers=headers)
                if response.status_code == 200:
                    print('Request successful...')
                    information = response.text
                    information = json.loads(information)
                    break
            except:
                pass
            i += 1
        
        # after getting this we extract the info we need
        print()
        print('Getting Lyrics...')
        url = ranked_song[4]
        headers_ = {'application' : 'BLyrics',
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}
        lyrics = None
        page_title = ''
        i = 0
        while i < 5:
            j = 0
            while j < 3:
                try:
                    response2 = requests.get(url, headers=headers_)
                    if response2.status_code == 200:
                        print('Request{} successful...'.format(i + 1))
                        print()    
                        html = BeautifulSoup(response2.text, 'html.parser')
                        page_title = html.find('title').get_text()
                        lyrics = html.find('div', class_='lyrics').get_text()
                        lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
                        break
                except:
                    pass
                j += 1
            i += 1

        try:
            description = information['response']['song']['description']['plain']
            release_date = information['response']['song']['release_date_for_display']
            recording_location = information['response']['song']['recording_location']
        except:
            description = None
            recording_location = None
            release_date = None
        final = {'Title' : ranked_song[0], 'Artist' : ranked_song[2], 
            'Description' : description, 'Lyrics' : lyrics, 
            'song_id' : song_id, 'lyrics_url' : ranked_song[4],
            'page_title' : page_title, 'recording_location' : recording_location,
            'release_date' : release_date}

        return final

    def search_artist(self, search_str):
        """Search about a particular artist
        For getting information

        Params:
            - Artist name (str)
        Return:
            - dict object
            - Information about artist
        """
        artist_ = self.search(search_str)
        if not artist_:
            return None
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
        headers = {'Authorization': access_token, 'application' : 'BLyrics',
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}
        i = 0
        response = None
        while i < 3:
            try:
                response = requests.get(request_url, params=params, headers=headers)
                if response.status_code == 200:
                    print('Request successful...')
                    print()
                    break
            except:
                pass
            i += 1
        if not response:
            return response
        information = response.text
        information = json.loads(information)

        aka = information['response']['artist']['alternate_names']
        twitter_name = information['response']['artist']['twitter_name']
        facebook_name = information['response']['artist']['facebook_name']
        instagram_name = information['response']['artist']['instagram_name']
        description = information['response']['artist']['description']['plain']
        image_url = information['response']['artist']['image_url']
        akas = ', '.join(aka)

        # dictionary id : song title
        artist_songs = self.search_artist_song(artist_id)

        if not artist_songs:
            num = len(artist['response']['hits'])
            artist_songs = []
            for i in range(num):
                song_title = artist['response']['hits'][i]['result']['title_with_featured']
                artist_songs.append(song_title)

        final = {'artist_name' : ranked_artist[0], 'Aliases' : akas, 
        'Twitter Handle' : twitter_name, 'Instagram Handle' : instagram_name, 
        'Facebook Name' : facebook_name, 'Description' : description,
        'songs' : artist_songs, 'image_url' : image_url}

        return final

    def search_artist_song(self, artist_id):
        """Searching for all songs by artist

        Params:
            - artist_id : Genius id for artist

        Returns:
            - dict object containing songs
            - key = song_id
            - value = song_title
        """
        path = 'artists/{}/songs'.format(artist_id)
        request_url = '/'.join([self.root, path])
        print('Getting songs by Artist...')

        params = {'sort':'popularity','per_page': 23, 'page': 1}
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 'application' : 'BLyrics',
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}
        i = 0
        response = None
        while i < 3:
            try:
                response = requests.get(request_url, params=params, headers=headers)
                if response.status_code == 200:
                    print('Request successful...')
                    print()
                    break
            except:
                pass
            i += 1
        if not response:
            return response
        returned = json.loads(response.text)

        final = {}
        num = len(returned['response']['songs'])
        for i in range(num):
            song_id = returned['response']['songs'][i]['id']
            song_title = returned['response']['songs'][i]['title_with_featured']
            final[song_id] = song_title
            
        return final
        

    

