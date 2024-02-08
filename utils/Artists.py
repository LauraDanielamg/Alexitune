from lyricsgenius import Genius
from lyricsgenius.artist import Artist
from lyricsgenius.api.base import HTTPError, Timeout
import os
import json

artists_folder = 'artists'
genius: Genius

def artists_path(id: int) -> str:
    return f'{artists_folder}/{id}.json'

def artists_save(dict: dict, id: int):
    path = artists_path(id)

    if os.path.exists(artists_folder) is not True:
        os.makedirs(artists_folder)

    with open(path, 'w') as file:
        json.dump(dict, file, indent='\t')

def artist_load(path: str) -> Artist:
    with open(path, 'r') as file:
        data = json.load(file)
        return Artist(genius, data)

def artists_load_single(id: int) -> Artist:
    path = artists_path(id)
    if os.path.exists(path) is True:
        return artist_load(path)

    try:
        artist = genius.artist(id)
    except HTTPError as err:
        print(err)
        artist = {}
    except Timeout as err:
        print(err)

    print(f'id: {id}, artist:\n{artist}')
    artists_save(artist, id)
    return Artist(genius, artist)

def artists_is_loaded() -> bool:
    return len(os.listdir(artists_folder)) > 0

def artists_download(from_id: int = 1):
    id = from_id
    
    while True:
        artists_load_single(id)
        id += 1

