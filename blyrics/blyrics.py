#!/usr/bin/python
# Author:   @BlankGodd_

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
        """Constructor for package class
        
        Methods:
            - search_song: to search for songs
            - save_song: to save song infomation to file
            - search_artist: to search for artist
            - save artist: to save artist information to file
            - get_annotations: for getting song annotations
            - get_article_links: For getting links and titles of articles currently on the genius home page
            - get_article: For getting an articles currently on the genius home page
            - get_chart: For getting chart of top trending songs
        """
        self.search_bot = Search_Genius()
        self.save_bot = Save()
        self.interact_bot = Interact()
        self.web_bot = Webpage()
    
    def search_song(self, song):
        """For getting song info and lyrics
        
        Params:
            - song: song title
        Returns:
            - dict: a dictionary of song information and lyrics
        """
        response = self.search_bot.search_song(search_str=song)
        if not response:
            raise ResponseError('Could not retrieve response')
        return response

    def save_song(self, song_info):
        """For saving song info
        
        Params:
            - song_info: value returned by search_song
        """
        self.save_bot.save_song(tbs=song_info)

    def search_artist(self, artist):
        """For getting artist info 
        
        Params:
            - artist: artist name
        Returns:
            - dict: a dictionary of artist information
        """
        response = self.search_bot.search_artist(search_str=artist)
        if not response:
            raise ResponseError('Could not retrieve response')
        return response

    def save_artist(self, artist_info):
        """For saving artist info
        
        Params:
            - artist_info: value returned by search_artist
        """
        self.save_bot.save_artist(tbs=artist_info)

    def get_annotations(self, song_id):
        """For getting song annotations
        
        Params:
            - song_id: song id gotten from search_song
        Returns:
            - annotations: list of annotations and other important information
        """
        annots = self.interact_bot.get_referents(song_id=song_id)
        if not annots:
            raise ResponseError('Could not retrieve response')
        return annots

    def get_articles_links(self):
        """For getting links and titles of articles currently on the genius home page
        
        Returns:
            - tuple: headliner and other articles
        """
        articles = self.web_bot.check_articles()
        if not articles:
            raise ResponseError('Could not retrieve response')
        return articles

    def get_article(self, link):
        """For getting an articles currently on the genius home page
        
        Params:
            - link: article link gotten from get_article_links
        Returns:
            - str: article content
        """
        article = self.web_bot.get_article(aritcle_link = link)
        if not article:
            raise ResponseError('Could not retrieve response')
        return article

    def get_chart(self):
        """For getting chart of top trending songs
        
        Returns:
            - tuple: ranks, song title and artist name
        """
        chart = self.web_bot.get_charts()
        if not chart:
            raise ResponseError('Could not retrieve response')
        return chart


if __name__ == '__main__':
    Tool()


