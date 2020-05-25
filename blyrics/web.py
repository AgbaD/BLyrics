#!/usr/bin/python
# Author:   @BlankGodd

import requests
from bs4 import BeautifulSoup
import re, ast

class Webpage:
    """For getting articles from www.genius.com"""

    def __init__(self):
        """Constructor for Webpage class
        
        Methods:
            - get_page: get the genius home page
            - check_articles: get top 5 articles(names and links)
            - get_article: get the complete article based on the link
            - get_chart: get top 10 songs and artist name
        """

        self.access_token = 'pX_ZcyoBxAKt8Z2F9oCOASPTzspv9er17wWCAPNIwIWcr5Lg_AyMRgGsx846LVAE'
        self.url = 'https://genius.com'

    def get_page(self, url):
        """For retriving a page

        Params:
            - url: url of page to be retrieved
        Returns:
            - response: response from request.get(url)
        """
        headers = {'User-Agent': 'https://github.com/BlankGodd/Blyrics',
                    'application': 'BLyrics'}
        i = 0
        while i < 3: # try reconnecting 2 times if status_Code != 200
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    return response
            except:
                pass
            i += 1
        print()
        print("Could not retrieve page. Please check connection and retry!")
        print()
        return None

    def check_articles(self):
        """For scrapping article title and links
        
        Returns
            - tuple: contains dictionary with title as keys and links as values
        """
        response = self.get_page(self.url)
        if not response:
            return None
        print('Getting Articles...')
        print()
        html = BeautifulSoup(response.text, 'html.parser')
        headline = html.find('div', class_='EditorialPlacement__Title-sc-11ot04a-1 elKqNh').get_text()
        link =  html.find('a', class_= 'EditorialPlacement__Link-sc-11ot04a-2 bCpoMC')
        headline_link = link['href']
        
        other_news_raw = html.find_all('div', class_='EditorialPlacement__Title-sc-11ot04a-1 ABTJt')
        other_links_raw = html.find_all('a', class_="EditorialPlacement__Link-sc-11ot04a-2 hyRooK")
        other_news = []
        other_links = []
        for val in other_news_raw:
            other_news.append(val.text)
        for val in other_links_raw:
            other_links.append(val['href'])
        print()
        print('Request Successful...')
        print()

        headline_d = {headline:headline_link}
        other_news_d = {}
        for i in range(len(other_links)):
            other_news_d[other_news[i]] = other_links[i]

        articles = (headline_d, other_news_d)

        return articles
    
    def get_article(self, article_link):
        article = self.get_page(article_link)
        if not article:
            return None
        html = BeautifulSoup(article.text, 'html.parser')
        


if __name__ == '__main__':
    w = Webpage()
    a = w.check_articles()




    