from lyricsgenius import Genius
from lyricsgenius.api.base import HTTPError, Timeout

from utils import ArtistSongs, Songs

import os
import json
from functools import reduce

folder = 'lyrics'
genius: Genius

def __path(id: int) -> str:
    return f'{folder}/{id}.json'

def __save(id: int, lyrics: str):
    path = __path(id)
    
    if os.path.exists(folder) is not True:
        os.makedirs(folder)

    with open(path, 'w') as file:
        json.dump(lyrics, file, indent='\t')

def __load(path: str) -> str:
    with open(path, 'r') as file:
        return json.load(file)

def __download(id: int) -> str:
    path = __path(id)

    if os.path.exists(path):
        return __load(path)

    try:
        lyricts = genius.lyrics(id, remove_section_headers=True)
    except HTTPError as err:
        print(err)
        lyricts = ''
    except Timeout as err:
        print(err)
        lyricts = ''
    
    __save(id, lyricts)
    return lyricts
    
def lyrics(id: int) -> str:
    if type(id) is not int: return ''
    return __download(id)

def remove(id: int):
    with open(__path(id), 'w') as file:
        json.dump('', file, indent='\t')

def load_from_artist_songs():
    folder = ArtistSongs.folder

    data = os.listdir(folder)
    data = map(ArtistSongs.__path, data)
    data = map(open, data)
    data = map(json.load, data)
    data = map(lambda dict: dict.get('songs', []), data)
    data = reduce(lambda x, y: x + y, data, [])
    data = map(lambda dict: dict.get('id'), data)
    data = list(data)

    for id in data:
        Songs.song(id)
        __download(id)