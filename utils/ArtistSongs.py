from lyricsgenius import Genius
from lyricsgenius.song import Song
from lyricsgenius.artist import Artist

import utils.Charts as Charts

import os
import json

artist_folder = 'artist_songs'
genius: Genius

def __artist_path(artist: Artist) -> str:
    return f'{artist_folder}/{artist._id}.json'

def __save_artist_songs(artist: Artist, songs: dict):
    path = __artist_path(artist)
    
    if os.path.exists(artist_folder) is not True:
        os.makedirs(artist_folder)

    with open(path, 'w') as file:
        json.dump(songs, file, indent='\t')

def __artist_download_songs(artist: Artist) -> dict:
    dict = genius.artist_songs(artist_id=artist._id, sort="popularity", per_page=50)
    __save_artist_songs(artist, dict)
    return dict
    
def artist_load_songs(artist: Artist) -> Artist:
    path = __artist_path(artist)

    if os.path.exists(path) is not True:
        songs_dict = __artist_download_songs(artist)
    else:
        songs_dict = json.load(open(path))

    songs = list(map(lambda song: Song(song), songs_dict['songs']))
    for song in songs:
        artist.add_song(song, include_features=True)

    return artist

def load_from_charts():
    charts = Charts.chart_load()
    for chart in charts:
        print(f'Name: {chart.artist.name}; ID: {chart.artist._id}')
        artist_load_songs(chart.artist)