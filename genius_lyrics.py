#! /usr/bin/python
# Author:   @BlankGodd

import requests
import ast, json
from bs4 import BeautifulSoup


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

        params = {'q': search_str}
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}

        response = requests.get(request_uri, params=params, headers=headers)
        print(response.status_code)
        return response.text

    def search_song(self, search_str):
        # song = self.search(search_str)
        # search for the song
        # get the song id
        # get the lyrics
        # say we have a song id for no role models
        song_id = '599427'
        path = 'songs/{}'.format(song_id)
        request_uri = '/'.join([self.root,path])
        print(request_uri + search_str)

        params = {'text_format':'plain'}
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}
        response = requests.get(request_uri, params=params, headers=headers)
        print(response.status_code)
        text = response.text
        # after getting this we extract the link to the lyrics and other info
        url = 'https://genius.com/J-cole-no-role-modelz-lyrics'
        response2 = requests.get(url)
        print(response2.status_code)
        if response2.status_code == 200:
            return response2.text


b = BLyrics()
x = b.search_song('No Role Modelz')
with open('number_456.json', 'w') as at:
    json.dump(x, at)


