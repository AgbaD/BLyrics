#!/usr/bin/python
# Author:   @BlankGodd

import os

class Save:
    """For saving information to files"""

    def __init__(self):
        """Constructor for saving files

        Methods:
            - save_artist: saving artist information
            - save_song: saving song information
        """
        self.dir_name = 'Blyrics_Files'

    def save_artist(self, dir_path, tbs):
        """For saving information about artist to a file
        
        Properties:
            -Name: Artist name
            -Alias: Artist aliases
            -Twitter: Twitter handle
            -Instagram: Instagram handle
            -Image: Image Url
            -Songs: List of top songs
        Params:
            - tbs: information to be saved returned by search.search_artist()
        Returns:
            - str: good or bad save (not saved)
        """
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

        vars = """\nName: {0} \nAlias: {1} \nTwitter: {2} \nInstagram: {3} \nImage Url: {4} \nSongs: {5}
        """.format(tbs['artist_name'],tbs['Aliases'],tbs['Twitter Handle'],tbs['Instagram Handle'],
                tbs['image_url'],songs)
        
        file_name = '{}.txt'.format(tbs['artist_name'])
        with open(file_name, 'w') as fn:
            fn.write(vars)

        print()
        print('Saving complete...')

    def save_song(self, dir_path, tbs):
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
        full_path = os.path.join(dir_path, self.dir_name)
        if os.path.exists(full_path):
            pass
        else:
            os.mkdir(full_path)

        vars = """\nTitle: {0} \nArtist: {1} \nRelease Date: {2} \nRecording Location: {3} \nDescription: {4} \nLyrics: {5}
        """.format(tbs['Title'],tbs['Artist'],tbs['release_date'],tbs['recording_location'],tbs['Description'],tbs['Lyrics'])

        file_name = '{}.txt'.format(tbs['Title'])
        with open(file_name, 'w') as fn:
            fn.write(vars)

        print()
        print('Saving complete...')


