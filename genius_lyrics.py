#! /usr/bin/python3
# Author:   @BlankGodd

import requests
import ast, json
from bs4 import BeautifulSoup
import sys

class BLyrics:

    def __init__(self):
        with open('info.txt', 'r') as f:
            tok = ast.literal_eval(f.read())

        self.access_token = tok['access_token']
        self.root = 'https://api.genius.com'

    def search(self, search_str):
        try:
            search_str = search_str.replace(' ', '%20')
        except:
            pass
        path = 'search/'
        request_uri = '/'.join([self.root,path])
        print(request_uri + search_str)

        params = {'q': search_str}
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}

        response = requests.get(request_uri, params=params, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            with open('test_search.json', 'a') as ts:
                json.dump(response.text, ts)
        else:
            response.raise_for_status()


b = BLyrics()
b.search('Cole')



