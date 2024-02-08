from lyricsgenius import Genius
from lyricsgenius.api.base import HTTPError, Timeout

import os
import json

lyrics_folder = 'lyrics'
genius: Genius

def __path(id: int) -> str:
    return f'{lyrics_folder}/{id}.json'

def __save(id: int, lyrics: dict):
    path = __path(id)
    
    if os.path.exists(lyrics_folder) is not True:
        os.makedirs(lyrics_folder)

    with open(path, 'w') as file:
        json.dump(lyrics, file, indent='\t')

def __download(id: int) -> dict:
    try:
        dict = genius.lyrics(id, remove_section_headers=True)
    except HTTPError as err:
        print(err)
        dict = {}
    except Timeout as err:
        print(err)
        dict = {}
    
    __save(id, dict)
    return dict
    
def load(id: int) -> str:
    path = __path(id)

    if os.path.exists(path) is not True:
        lyric = __download(id)
    else:
        lyric = json.load(open(path))

    return lyric