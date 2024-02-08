from lyricsgenius import Genius
from lyricsgenius.artist import Artist

import os
import json
from functools import reduce

from utils import Artists

charts_folder = 'charts'
genius: Genius

class Chart(object):
    def __init__(self, json: dict):
        self._json = json

    @property
    def artist(self) -> Artist:
        return Artists.artists_load_single(self.artist_id)
    
    @property
    def artist_id(self) -> int:
        return self._json['item']['id']

class ChartList(object):
    def __init__(self, json: dict):
        self._json = json
    
    @staticmethod
    def __map_chart(chart: dict) -> Chart:
        return Chart(chart)

    @property
    def __items(self) -> [dict]:
        return self._json['chart_items']
    
    @property
    def charts(self) -> [Chart]:
        charts = self.__items
        charts = map(self.__map_chart, charts)
        return list(charts)

def chart_path(page: int) -> str:
    return f'{charts_folder}/{page}.json'

def chart_save(dict: dict, page: int):
    path = chart_path(page)

    if os.path.exists(charts_folder) is not True:
        os.makedirs(charts_folder)

    with open(path, 'w') as file:
        json.dump(dict, file, indent='\t')

def chart_download_single(page: int) -> str:
    chart = genius.charts(per_page=50, page=page, type_='artists', time_period='all_time')
    print(f'page: {page}, charts:\n{chart}')
    chart_save(chart, page)
    return chart

def chart_download(from_page: int = 1):
    page = from_page
    while True:
        path = chart_path(page)

        if os.path.exists(path) is not True:
            chart = chart_download_single(page)
        else:
            chart = json.load(open(path))
        
        if len(chart['chart_items']) == 0:
            print('No more charts')
            break

        page += 1

def chart_is_loaded() -> bool:
    return True
    return len(os.listdir(charts_folder)) > 0

def chart_load() -> [Chart]:
    def load_chart_list(file_name) -> ChartList:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return ChartList(data)

    files = os.listdir(charts_folder)
    files = map(lambda name: f'{charts_folder}/{name}', files)

    charts = map(load_chart_list, files)
    charts = map(lambda chart_list: chart_list.charts, charts)
    charts = reduce(lambda x, y: x + y, charts, [])
    return list(charts)
