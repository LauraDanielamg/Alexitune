from lyricsgenius import Genius
from lyricsgenius.artist import Artist
from lyricsgenius.api.base import HTTPError, Timeout

import os
import json

folder = 'artists'
genius: Genius

def __path(id: int) -> str:
    return f'{folder}/{id}.json'

def __save(dict: dict, id: int):
    path = __path(id)

    if os.path.exists(folder) is not True:
        os.makedirs(folder)

    with open(path, 'w') as file:
        json.dump(dict, file, indent='\t')

def __load(path: str) -> Artist:
    with open(path, 'r') as file:
        data = json.load(file)
        return Artist(genius, data)

def __download(id: int) -> Artist:
    path = __path(id)
    if os.path.exists(path):
        return __load(path)

    try:
        artist = genius.artist(id)
    except HTTPError as err:
        print(err)
        artist = {}
    except Timeout as err:
        print(err)
        artist = {}

    print(f'id: {id}, artist:\n{artist}')
    __save(artist, id)
    return Artist(genius, artist)

def artist(id: int) -> Artist:
    return __download(id)

