from lyricsgenius import Genius
from lyricsgenius.artist import Artist
from lyricsgenius.api.base import HTTPError, Timeout

import utils.Charts as Charts

import os
import json
from typing import Union

folder = 'artist_songs'
genius: Genius

def __path(id: Union[int, str]) -> str:
    if type(id) is int:
        return __path(f'{id}.json')
    else:
        return f'{folder}/{id}'

def __save(artist: Artist, songs: dict):
    path = __path(artist._id)
    
    if os.path.exists(folder) is not True:
        os.makedirs(folder)

    with open(path, 'w') as file:
        json.dump(songs, file, indent='\t')

def __load(path: str) -> dict:
    with open(path, 'r') as file:
        return json.load(file)

def __download(artist: Artist) -> dict:
    path = __path(artist._id)

    if os.path.exists(path):
        return __load(path)

    try:
        dict = genius.artist_songs(artist_id=artist._id, sort="popularity", per_page=50)
    except HTTPError as err:
        print(err)
        dict = {}
    except Timeout as err:
        print(err)
        dict = {}

    __save(artist, dict)
    return dict

def load_from_charts():
    charts = Charts.charts()
    for chart in charts:
        __download(chart.artist)