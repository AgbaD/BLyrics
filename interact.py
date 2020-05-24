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

        if (song_id and creator_id) or (song_id and webpage_id) or (webpage_id and song_id):
            raise DupError('Provide only one id')

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

    def create_annotations(self, page_url, page_title, 
                            canonical_url=None, og_url=None):
        path = '/annotations'
        request_url = ''.join([self.root, path])

        print('Type in the referent/highlight (the part of the lyrics you want to add an annotation to).')  
        fragment = input(': ')
        if fragment == '':
            print("Can't be left empty!")
            return

        print('To be more accurate, you can type in some part of the lyrics before and after your highlight \
        or leave it empty.')
        before_html = input('Before: ')
        after_html = input('After: ')

        print('Enter the note/annotation you want to add to your highlight')
        markdown = input(': ')
        if markdown == '':
            print("Can't be left empty!")
            return
        
        if not canonical_url:
            canonical_url = 'null'
        if not og_url:
            og_url = 'null'

        payload = {
            'annotation': {
                'body': {
                    'markdown': markdown
                }
            },
            'referent': {
                'raw_annotatable_url': page_url,
                'fragment': fragment
            },
            'web_page': {
                'canonical_url': canonical_url,
                'og_url': og_url,
                'title': page_title
            }
        }

        cfd = {}
        if before_html != '':
            cfd['before_html'] = before_html
        if after_html != '':
            cfd['after_html'] = after_html

        if cfd != {}:
            payload['referent']['context_for_display'] = cfd

        print('Creating Annotation...')
        print(payload)
        params = payload
        access_token = 'Bearer {}'.format(self.access_token)
        headers = {'Authorization': access_token, 'application' : 'BLyrics',
            'User-Agent':'https://github.com/BlankGodd/BLyrics'}
        
        response = requests.post(request_url, params=params, headers=headers)
        if response.status_code == 200:
            print('Creation successful...')
            print()
        else:
            print('Could not create annotaton :( ')
            print('Please try again.')



if __name__ == '__main__':
    b = Interact()
    b.create_annotations(page_url='https://genius.com/J-cole-fire-squad-lyrics',
                page_title='J. Cole – Fire Squad Lyrics | Genius Lyrics')
    

