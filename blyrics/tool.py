#!/usr/bin/python
# Author:   @BlankGodd

from pyfiglet import Figlet
from search import Search_Genius
from interact import Interact
from save import Save
from web import Webpage
import time, os


class Tool:
    """For using BLyrics as a script instead of a module"""
    def __init__(self):
        """Constructor for Script class
        
        Methods:
            - start: to start the main script
            - get_articles: to retrieve articles from the genius web page
            - print_articles: for printing articles to screen
            - get_Searching: to initiate the searching module
            - get_chart: to retrieve a chart of the top 10 songs
        """
        banner = Figlet(font='standard')
        print(banner.renderText("BLyrics"))

        # i have to make objects for each class
        # the script isn't working without ding it like this
        self.search_bot = Search_Genius() 
        self.interact_bot = Interact()
        self.save_bot = Save()
        self.web_bot = Webpage()
        # and add positional arguments

        print()
        print("Welcome To BLyrics")
        print()
        print('If you are new to BLyrics please check the help guide by typing help')
        print('Ignore to continue')
        print()
        comd = input(": ").lower()
        if comd == 'help':
            print('Welcome to BLyrics')
            print("To go back, enter 'back'(lower case)")
            print("To return to start page, enter 'menu'(lower case)")
            print("To exit, enter 'ctrl+Z'")
            print('Follow the prompt and you should be fine :)')
            time.sleep(3)
            for i in range(2):
                print()
        self.start()

    def start(self):
        print()
        print("To get latest articles from www.genius.com, press 1")
        print("To get a chart of the top trending songs, press 2")
        print('To get information about songs and artists, get song lyrics, press #')
        print()

        command = input(': ')
        if command == '1':
            self.get_articles()
        elif command == '2':
            self.get_chart()
        elif command == '3' or command == '#':
            self.get_searching()
        elif command == 'back' or 'command' == 'menu':
            self.start()
        else:
            print("Invalid input")
            self.start()
        self.start()
        
    def get_articles(self):
        """To get news and articles
        
        Returns:
            - Title: Article title
            - Body: Body of article
        """
        print()
        articles_titles = self.web_bot.check_articles()
        if not articles_titles:
            print('Service Timeout. Please Retry!')
            print()
            self.start()
            return
        # (headline_d, other_news_d)
        headline_d = articles_titles[0]
        for k,v in headline_d.items():
            self.headline = k
            self.headline_link = v
        other_news_d = articles_titles[1]
        self.other_news_title = []
        self.other_news_link = []
        for k,v in other_news_d.items():
            self.other_news_title.append(k)
            self.other_news_link.append(v)
        self.print_articles()

    def print_articles(self):
        print()
        print('Headline')
        print('1. {}'.format(self.headline))
        print()
        print('Other News')
        pos = 2
        for i in self.other_news_title:
            print('{}. {}'.format(pos, i))
            pos += 1
        print()
        print('Enter article number to read')
        numb = input(': ')
        if numb == 'back' or numb == 'menu':
            self.start()
            return
        print('Getting Article...')
        article = ''
        article_title = ''
        if numb == '1':
            url = self.headline_link
            article = self.web_bot.get_article(url)
            if not article:
                print('Could not retrieve article. Please Retry')
                self.get_articles()
                return
            article_title = self.headline
        else:
            ind = int(numb)-2
            url = self.other_news_link[ind]
            article = self.web_bot.get_article(url)
            if not article:
                print('Could not retrieve article. Please Retry')
                self.get_articles()
                return
            article_title = self.other_news_title[ind]

        print()
        print('Title: {}'.format(article_title))
        print()
        print('Article: \n{}'.format(article))
        print()
        print()
        print('Read other articles or exit to menu')
        move = input('Read more(r) or exit (e): ')
        if move == 'r':
            self.print_articles()
            return
        self.start()

    def get_chart(self):
        pass

    def get_searching(self):
        """To starting searching
        
        Properties:
            Artist:
                -Name: Artist name
                -Alias: Artist aliases
                -Description: Information about artist
                -Twitter: Twitter handle
                -Instagram: Instagram handle
                -Facebook: Facebook name
                -Songs: List of top songs
            Songs:
                -Title: Song title
                -Artist: Artist name
                -Description: Song description
                -Release Date: Song release date
                -Recording Location
                -Lyrics: Song lyrics
        """
        print()
        print('Information')
        print('1: Search Artist')
        print('2: Search Song ')
        print()
        command = input('Enter 1 or 2: ').lower()
        if command == 'back' or command == 'menu':
            self.start()
            return
        print()
        response = None
        search_str = ''
        if command == '1':
            while search_str == '':
                print("Please enter valid input!")
                search_str = input('Enter Artist name: ')
            if search_str == 'back' or search_str == 'menu':
                self.start()
                return
            response = self.search_bot.search_artist(search_str = search_str)
        elif command == '2':
            while search_str == '':
                print("Please enter valid input!")
                search_str = input('Enter Song title: ')
            if search_str == 'back' or search_str == 'menu':
                self.start()
                return
            response = self.search_bot.search_song(search_str = search_str)
        else:
            print('Invalid input!')
            self.get_searching()
            return

        if not response:
            print('{} not found. (Service Timeout) Please retry!'.format(search_str))
            self.get_searching()
            return

        if command == '1':
            name = response['artist_name']
            alias = response['Aliases']
            twitter = response['Twitter Handle']
            ig = response['Instagram Handle']
            facebook = response['Facebook Name']
            description = response['Description']
            songs = response['songs']
            
            print()
            print('Artist Name: {}'.format(name))
            print('Aliases: {}'.format(alias))
            print()
            print('Twitter Handle: {}'.format(twitter))
            print('Instagram Handle: {}'.format(ig))
            print('Facebook Name: {}'.format(facebook))
            print()
            print('Description: \n{}'.format(description))
            print()
            print('Songs by {}'.format(name))
            if type(songs) == list:
                for song in songs:
                    print(song)
            else:
                for k,v in songs.items():
                    print(v)   
        else:
            title = response['Title']
            artist = response['Artist']
            description = response['Description']
            lyrics = response['Lyrics']
            recording_location = response['recording_location']
            release_date = response['release_date']
            song_id = response['song_id']

            print()
            print('Song Title: {}'.format(title))
            print('Artist: {}'.format(artist))
            print()
            print('Record Location: {}'.format(recording_location))
            print('Release Date: {}'.format(release_date))
            print()
            print('Description: \n{}'.format(description))
            print()
            print('Lyrics: \n{}'.format(lyrics))
            print()
            print()

            print('Would you like to view annotations')
            an = input('y/n: ').lower()
            print()
            if an == 'back' or an == 'menu':
                self.start()
                return
            if an == 'y':
                referents = self.interact_bot.get_referents(song_id = song_id)
                num = len(referents)
                annotations = {}
                for i in range(num):
                    annotator_name = referents[i][0]
                    fragment = referents[i][3]
                    annotation = referents[i][5]
                    ls = (annotator_name, fragment, annotation)
                    annotations[i+1] = ls
                print()
                print('There are {} annotations for the track'.format(num))
                print('1: View all annotations')
                print('2: Cancel')
                commandd = input(': ')
                if commandd == '1':
                    for k,v in annotations.items():
                        print()
                        print('---------------------------------------------------------------------------------')
                        print(k)
                        print('Annotator: {}'.format(v[0]))
                        print()
                        print('Highlight: \n{}'.format(v[1]))
                        print()
                        print('Annotations/Notes \n{}'.format(v[2]))
                        print('---------------------------------------------------------------------------------')
                elif commandd == 'back' or commandd == 'menu':
                    self.start()
                    return
                else:
                    pass
            else:
                pass

        print()
        print('Would you like to save information to file')
        sv = input('y/n: ').lower()
        if sv == 'y':
            if command == '1':
                self.save_bot.save_artist(tbs = response)
            else:
                self.save_bot.save_song(tbs = response)
            print('File saved to BLyrics_Files directory')
        self.start()
        
        
if __name__ == '__main__':
    Tool()        

