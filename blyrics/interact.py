#!/usr/bin/python
# Author:   @BlankGodd_

import json
import ast
import requests

class DupError(Exception):
    """Duplication Error"""
    pass

class Interact:
    """For getting referents"""
    def __init__(self):
        """Interact class constructor
        
        Method:
            - get_referents: for getting referents and annotations 
                Params:
                    - song_id
                    - creator_id
        """

        self.access_token = 'pX_ZcyoBxAKt8Z2F9oCOASPTzspv9er17wWCAPNIwIWcr5Lg_AyMRgGsx846LVAE'
        self.root = 'https://api.genius.com'

    def get_referents(self, song_id = None, webpage_id = None,
                        creator_id = None):
        """For getting referents and annotations to a song
        
        Params:
            - song_id = None
            - creator_id = None
            ('Must provide song or creator id BUT not both)

        Returns:
            - list: list containing tuples of referents, annotations and other information
        """
        path = 'referents?'
        request_url = '/'.join([self.root, path])

        if (song_id and creator_id) or (song_id and webpage_id) or (webpage_id and song_id):
            raise DupError('Provide only one id')

        print('Getting Referents...')
        params = {'song_id' : song_id, 'web_page_id' : webpage_id,
                    'created_by_id' : creator_id, 'text_format' : 'plain',
                    'per_page' : 23, 'page' : 1}
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 'application' : 'BLyrics',
            'User-Agent':'https://github.com/AgbaD/BLyrics'}
        
        response = None
        i = 0
        while i < 3:    # try reconnecting 2 times if status_Code != 200
            try:
                response = requests.get(request_url, params=params, headers=headers)
                if response.status_code == 200:
                    print('Request Successful...')
                    print()
                    break
            except:
                pass
            i += 1
        if not response:
            return response

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


    

