#!/usr/bin/python
# Author:   @BlankGodd

import json
import ast
import requests

class DupError(Exception):
    """Duplication Error"""
    pass

class Interact:

    def __init__(self):
        with open('info.txt', 'r') as f:
            tok = ast.literal_eval(f.read())

        self.access_token = tok['access_token']
        self.root = 'https://api.genius.com'

    def get_referents(self, song_id = None, webpage_id = None,
                        creator_id = None):
        path = 'referents?'
        request_url = '/'.join([self.root, path])

        if song_id and webpage_id:
            raise DupError('Provide song_id or web_page_id but not both')

        print('Getting Referents...')
        params = {'song_id' : song_id, 'web_page_id' : webpage_id,
                    'created_by_id' : creator_id, 'text_format' : 'plain',
                    'per_page' : 23, 'page' : 1}
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 'application' : 'BLyrics',
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}
        
        response = requests.get(request_url, params=params, headers=headers)
        if response.status_code == 200:
            print('Request Successful...')
            print()
        else:
            return None

        referents = response.text
        referents = json.loads(response.text)
        
        referents_total = []
        num = len(referents['response']['referents'])
        for i in range(num):
            annotator_name = referents['response']['referents'][i]['annotator_login']
            annotator_id = referents['response']['referents'][i]['annotator_id']
            song_id_from = referents['response']['referents'][i]['annotatable']['id']
            fragment = referents['response']['referents'][i]['fragment']
            annotations_id = referents['response']['referents'][i]['annotations'][0]['id']
            annotation = referents['response']['referents'][i]['annotations'][0]['body']['plain']
            ls = (annotator_name, annotator_id, song_id_from, fragment,
                    annotations_id, annotation)
            referents_total.append(ls)

        return referents_total


if __name__ == '__main__':
    b = Interact()
    a = b.get_referents(song_id = '599417')
    for i in range(len(a)):
        print()
        print(i+1)
        print('---------------------------------------------------------------------------------------------------')
        print(a[i][0])
        print()
        print(a[i][3])
        print()
        print(a[i][5])
        print('---------------------------------------------------------------------------------------------------')
        print()

