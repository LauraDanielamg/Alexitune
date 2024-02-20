#flask --app server run

from flask import Flask, request
from pandas import DataFrame, read_csv

from functools import reduce

app = Flask(__name__, instance_relative_config=True)

songsDataFrame: DataFrame = read_csv('songs.csv')

sentimentsDataFrame: DataFrame = read_csv('sentiments.csv')
sentiments = sentimentsDataFrame.columns.values
sentiments = filter(lambda x: x != 'ID', sentiments)
sentiments = filter(lambda x: x != 'Unnamed: 0', sentiments)
sentiments = list(sentiments)

@app.route('/sentiments')
def all_sentiments():
    return sentiments

@app.route('/search', methods=['POST'])
def search():
    json = request.json
    json = map(lambda dict: {dict.get('name'): dict.get('value')}, json)
    json = reduce(lambda x, y: x | y, json, {})
    keys = json.keys()

    dataFrame = sentimentsDataFrame

    dataFrame['Diff'] = 0
    for key in keys:
        dataFrame['Diff'] = dataFrame['Diff'] + pow(dataFrame[key] - json[key], 2)
    dataFrame['Diff'] = pow(dataFrame['Diff'], 0.5)

    result = dataFrame.sort_values(by=['Diff'], ascending=True).sample(10)['ID']
    resultFilter = songsDataFrame['ID'].isin(result)
    result = songsDataFrame[resultFilter]

    return result[['Name', 'Artist', 'Lyrics', 'URL', 'Image']].to_json(orient='records')