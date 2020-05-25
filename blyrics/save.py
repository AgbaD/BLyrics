#!/usr/bin/python
# Author:   @BlankGodd

import os
import json

class Save:
    """For saving information to files"""

    def __init__(self):
        """Constructor for saving files

        Methods:
            - save_artist: saving artist information
            - save_song: saving song information
        """
        self.dir_name = 'Blyrics_Files'
        working_dir = os.getcwd()
        os.chdir('..')
        self.path = os.getcwd()
        os.chdir(working_dir)

    def save_artist(self, tbs):
        """For saving information about artist to a file
        
        Properties:
            -Name: Artist name
            -Alias: Artist aliases
            -Description: Information about artist
            -Twitter: Twitter handle
            -Instagram: Instagram handle
            -Image: Image Url
            -Songs: List of top songs
        Params:
            - tbs: information to be saved returned by search.search_artist()
        Returns:
            - str: good or bad save (not saved)
        """
        dir_path = self.path
        full_path = os.path.join(dir_path, self.dir_name)
        if os.path.exists(full_path):
            pass
        else:
            os.mkdir(full_path)

        songs = tbs[songs]
        if type(songs) == list:
            songs = '\n'.join(songs)
        else:
            song_list = []
            for k,v in songs.items():
                song_list.append(v)
            songs = '\n'.join(song_list)

        vars = {'Name': tbs['artist_name'],'Alias': tbs['Aliases'],
                'Description': tbs['Description'],'Twitter': tbs['Twitter Handle'],
                'Instagram': tbs['Instagram Handle'],'Image Url': tbs['image_url'],
                'Songs': songs}
        
        f_name = '{}.json'.format(tbs['artist_name'])
        file_name = os.path.join(full_path, f_name)
        with open(file_name, 'w') as fn:
            json.dump(vars, fn)

        print()
        print('Saving complete...')

    def save_song(self, tbs):
        """For saving information about song and song lyrics
        
        Properties:
            -Title: Song title
            -Artist: Artist name
            -Description: Song description
            -Release Date: Song release date
            -Recording Location
            -Lyrics: Song lyrics
        Params:
            - tbs: information to be saved returned by search.search_song()
        Returns:
            - str: good or bad save (not saved)
        """
        dir_path = self.path
        full_path = os.path.join(dir_path, self.dir_name)
        if os.path.exists(full_path):
            pass
        else:
            os.mkdir(full_path)

        vars = {'Title': tbs['Title'],'Artist': tbs['Artist'],'Release Date': tbs['release_date'],
                'Recording Location': tbs['recording_location'],'Description': tbs['Description'],
                'Lyrics': tbs['Lyrics']}

        f_name = '{}.json'.format(tbs['Title'])
        file_name = os.path.join(full_path, f_name)
        with open(file_name, 'w') as fn:
            json.dump(vars, fn)

        print()
        print('Saving complete...')


