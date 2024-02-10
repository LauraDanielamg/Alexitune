from lyricsgenius import Genius
from lyricsgenius.song import Song
from lyricsgenius.api.base import HTTPError, Timeout

import os
import json
from typing import Union

folder = 'songs'
genius: Genius

def __path(id: Union[int, str]) -> str:
    if type(id) is int:
        return __path(f'{id}.json')
    else:
        return f'{folder}/{id}' 

def __save(dict: dict, id: int):
    path = __path(id)

    if os.path.exists(folder) is not True:
        os.makedirs(folder)

    with open(path, 'w') as file:
        json.dump(dict, file, indent='\t')

def __load(path: str) -> Song:
    with open(path, 'r') as file:
        data = json.load(file)
        return Song(data)

def __download(id: int) -> Song:
    path = __path(id)
    if os.path.exists(path) is True:
        return __load(path)

    try:
        song_dict = genius.song(id)
    except HTTPError as err:
        print(f'ID: {id} HTTPError: {err}.')
        song_dict = {'url':'', 'api_path': '', 'id':'', 'language': ''}
    except Timeout as err:
        print(f'ID: {id} Timeout: {err}.')
        song_dict = {'url':'', 'api_path': '', 'id':'', 'language': ''}

    __save(song_dict, id)
    return Song(song_dict)

def song(id: int) -> Song:
    return __download(id)

def remove(id: int):
    path = __path(id)

    if os.path.exists(path) is not True:
        os.remove(path)

def songs() -> list[Song]:
    dirs = os.listdir(folder)
    dirs = map(__path, dirs)

    files = map(open, dirs)
    jsons = map(json.load, files)

    songs = map(lambda json: Song(json), jsons)
    return list(songs)