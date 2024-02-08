from lyricsgenius import Genius
from lyricsgenius.song import Song
from lyricsgenius.api.base import HTTPError, Timeout
import os
import json

folder = 'songs'
genius: Genius

def __path(id: int or str) -> str:
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
        print(err)
        song_dict = {'url':'', 'api_path': ' ', 'id':' '}
    except Timeout as err:
        print(err)
        song_dict = {'url':' ', 'api_path': ' ', 'id':' '}

    __save(song_dict, id)
    return Song(song_dict)

def song(id: int) -> Song:
    return __download(id)

def song_batch(from_id: int = 1):
    id = from_id
    
    while True:
        __download(id)
        id += 1
        
def song_is_loaded() -> bool:
    return len(os.listdir(folder)) > 0

def songs() -> [Song]:
    dirs = os.listdir(folder)
    dirs = map(__path, dirs)

    files = map(open, dirs)
    jsons = map(json.load, files)

    songs = map(lambda json: Song(json), jsons)
    return list(songs)