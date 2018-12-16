import pandas as pd
import numpy as np


## 1. Get the list of songs and their peak positions on hot 100 chart during a specific period
import billboard

song_dict = {}
song_dict['name'] = []
song_dict['peak'] = []
chart = billboard.ChartData(name = 'hot-100', date = '2017-12-31')
while chart.previousDate:
    for track in chart:
        if track.title not in song_dict['name']:
            song_dict['name'].append(track.title)
            song_dict['peak'].append(track.peakPos)
    prevDate = chart.previousDate
    if int(prevDate.split('-')[0]) < 2016:
        break
    chart = billboard.ChartData('hot-100', prevDate)
    print(chart.previousDate)