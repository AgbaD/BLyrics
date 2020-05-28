

Welcome to BLyrics's documentation!
===================================

[//]: # (toctree::)
[//]: # (:maxdepth: 2)
[//]: # (:caption: Contents:)



# BLyrics :notes: 
BLyrics is a python client for leveraging the GENIUS API.

A CLI tool for interacting with Genius

It is also used for getting latest articles and song charts

## Package features include
1. Getting infomation 
   - Songs 
   - Artists 
   - Lyrics 
   - Annotations 

2. Saving prefrences :zap:
   - Artist Info
   - Song info and lyrics
   
3. Latest information and articles
   - Headliner from genius.com
   - Oher articles
   - Charts

## Requirements
1. Python3 
2. Any Operating system
3. An open mind

## Installation

1. [Setup virtual enviroment](https://realpython.com/python-virtual-environments-a-primer/)

2. Install from PyPi
```sh
$ pip3 install blyrics
```

## Functions
#### search_song(song)
For getting song info and lyrics
- Params:
  - song: song title
- Returns:
  - dict: a dictionary of song information and lyrics

**Usage:**
```py
>>>song_info = Package.search_song('No Role Modelz')
>>>song_lyrics = song_info['Lyrics']
>>>print(song_lyrics)
```

#### save_song(song_info)
For saving song info
- Params:
  - song_info: value returned by search_song

```py
>>>Package.save_song(song_info)
Saving Complete...
>>>
```

#### search_artist(artist)
For getting artist info 
- Params:
  - artist: artist name
- Returns:
  - dict: a dictionary of artist information

**Usage:**
```py
>>>artist_info = Package.search_artist('Cole')
>>>twitter = artist_info['Twitter Handle']
>>>print(twitter)
```

#### save_artist(artist_info)
For saving artist info
- Params:
  - artist_info: value returned by search_artist

```py
>>>Package.save_artist(artist_info)
Saving Complete...
>>>
```

#### get_annotations(song_id)
For getting song annotations
- Params:
  - song_id: song id gotten from search_song
- Returns:
  - annotations: list of annotations and other important information
    
**Usage:**
```py
>>>song_id = song_info['song_id']
>>>annotations = Package.get_annotations(song_id)
```

#### get_articles_links():
For getting links and titles of articles currently on the genius home page
- Returns:
  - tuple: headliner and other articles
    
**Usage:**
```py
>>>articles = Package.get_articles_links()
>>>print(aritcles)
```

#### get_article(link)
"""For getting an articles currently on the genius home page
- Params:
  - link: article link gotten from get_article_links
- Returns:
  - str: article content

**Usage:**
```py
>>>headline = articles[0]
>>>links = [v for v in headline.values()]
>>>article = Package.get_article(links[0])
>>>print(article)
```

#### get_chart()
For getting chart of top trending songs
- Returns:
  - tuple: ranks, song title and artist name

```py
>>>chart = Package.get_chart()
>>>for i in range(len(chart[0])):
...    print(chart[0][i],'   ',chart[1][i],'  ',chart[2][i])
```

## Contribute
- Issues: https://github.com/BlankGodd/BLyrics/issues
- Source Code: https://github.com/BlankGodd/BLyrics

## License
Project licensed under the MIT license

## Author
- Nick: BlankGodd
- Email: blankgodd33@gmail.com
- Github: https://github.com/BlankGodd
- Twitter: @blankgodd_
   
   
