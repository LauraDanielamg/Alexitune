from lyricsgenius import Genius
from lyricsgenius.artist import Artist

from utils import Artists

import os
import json
from functools import reduce

folder = 'charts'
genius: Genius

class Chart(object):
    def __init__(self, json: dict):
        self._json = json
    
    @property
    def artist_id(self) -> int:
        return self._json['item']['id']
    
    @property
    def artist(self) -> Artist:
        return Artists.artist(self.artist_id)

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

def __path(page: int or str) -> str:
    if type(page) is int:
        return __path(f'{page}.json')
    else:
        return f'{folder}/{page}'

def __save(dict: dict, page: int):
    path = __path(page)

    if os.path.exists(folder) is not True:
        os.makedirs(folder)

    with open(path, 'w') as file:
        json.dump(dict, file, indent='\t')

def __load(path: str) -> ChartList:
    with open(path, 'r') as file:
        data = json.load(file)
        return ChartList(data)

def __download(page: int) -> ChartList:
    path = __path(page)

    if os.path.exists(path):
        return __load(path)

    chart = genius.charts(per_page=50, page=page, type_='artists', time_period='all_time')
    __save(chart, page)
    return ChartList(chart)

def chart_download():
    page = 1
    while len(__download(page).charts) > 0:
        page += 1

def charts() -> [Chart]:
    files = os.listdir(folder)
    files = map(__path, files)

    charts = map(__load, files)
    charts = map(lambda chart_list: chart_list.charts, charts)
    charts = reduce(lambda x, y: x + y, charts, [])
    return list(charts)
