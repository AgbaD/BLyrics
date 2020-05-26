#!/usr/bin/python
# Author:   @BlankGodd

from search import Search_Genius
from interact import Interact
from save import Save
from web import Webpage
from tool import Tool


class ResponseError(Exception):
    """Response error class"""
    pass

class Package:
    """class for using blyrics as a module"""
    def __init__(self):
        self.search_bot = Search_Genius()
        self.save_bot = Save()
        self.interact_bot = Interact()
    
    def search_song(self, song):
        """For getting song info and lyrics
        
        Returns:
            - dict: a dictionary of song information and lyrics
        """
        response = self.search_bot.search_song(search_str=song)
        if not response:
            raise ResponseError('Could not retrieve response')
        return response

    def save_song(self, song):
        """For saving song info
        
        Params:
            - song: value returned by search_song
        """
        self.save_bot.save_song(tbs=song)

    def search_artist(self, artist):
        """For getting artist info 
        
        Returns:
            - dict: a dictionary of artist information
        """
        response = self.search_bot.search_artist(search_str=artist)
        if not response:
            raise ResponseError('Could not retrieve response')
        return response

    def save_artist(self, artist):
        """For saving artist info
        
        Params:
            - song: value returned by search_artist
        """
        self.save_bot.save_artist(tbs=artist)

    def get_annotations(self, song):
        song = self.search_song(song)
        if not song:
            raise ResponseError('Could not retrieve response')
        song_id = song['song_id']
        annots = self.interact_bot.get_referents(song_id=song_id)
        if not annots:
            raise ResponseError('Could not retrieve response')
        return annots

    def get_articles(self):
        pass

    def get_charts(self):
        pass



if __name__ == '__main__':
    Tool()
