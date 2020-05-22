#! /usr/bin/python
# Author:   @BlankGodd

import json

class DupError(Exception):
    """Duplication Error"""
    pass

class Interact:

    def __init__(self):
        with open('info.txt', 'r') as f:
            tok = ast.literal_eval(f.read())

        self.access_token = tok['access_token']
        self.root = 'https://api.genius.com'

    def get_referents(self, song_id = None, webpage_id = None):
        path = 'referents?'
        if song_id and webpage_id:
            raise DupError('Provide song_id or web_page_id but not both')
        params = {'song_id' :}