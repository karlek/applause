import sqlite3
import time
import datetime
from dateutil.parser import parse
from collections import defaultdict
import pprint
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
import plotly.plotly as py
import plotly.offline as pyoff
import plotly.graph_objs as go

style.use('fivethirtyeight')

conn = sqlite3.connect('norm.db')

# enable extension loading
conn.enable_load_extension(True)

# Load the fulltext search extension
conn.load_extension("./icu.so")

c = conn.cursor()

pp = pprint.PrettyPrinter(indent=3)

parties = ['c', 'kd', 'l', 'm', 'mp', 's', 'sd', 'v']
long_names = {
    'c':  '(C) Centerpartiet',
    'kd': '(KD) Kristdemokraterna',
    'l':  '(L) Liberalerna',
    'm':  '(M) Moderaterna',
    'mp': '(MP) Miljöpartiet',
    's':  '(S) Socialdemokraterna',
    'sd': '(SD) Sverigedemokraterna',
    'v':  '(V) Vänsterpartiet',
}
colors = {
    'c':  '#009933',
    'kd': '#231977',
    'l':  '#6BB7EC',
    'm':  '#1B49DD',
    'mp': '#83CF39',
    's':  '#EE2020',
    'sd': '#DDDD00',
    'v':  '#AF0000',
}

def by_party():
    query = ''
    with open('by_parti.sql', 'r') as f:
        query = f.read()

    if query == '':
        die('File not found!')

    c.execute(query)
    data = c.fetchall()

    values = defaultdict(list)
    total = defaultdict(int)
    applauded = defaultdict(int)
    last = defaultdict(str)
    for row in data:
        party = row[0]
        datum = row[1]
        number_of_speeches = row[2]
        applauded_speeches = row[3]

        last_date = last[party]
        print("'%s'" % (last_date))
        if last_date != '':
            d = parse(datum)
            dd = datetime.timedelta(days=14)
            if d-dd > parse(last_date):
                values[party].append((d-dd, None))

        ratio = 0
        if total[party] != 0:
            ratio = round(applauded[party]/total[party], 4)

        values[party].append((datum, ratio))

        total[party] += number_of_speeches
        applauded[party] += applauded_speeches
        last[party] = datum


    # pp.pprint(values)

    # Remove the first non-representative ratios.
    for party in values:
        for i in range(60):
        # for i in range(50):
            del values[party][0]

    data = []
    for party in values:
        trace = go.Scatter(
            x = [x[0] for x in values[party]],
            y = [x[1] for x in values[party]],
            name = long_names[party],
            mode = 'lines',
            connectgaps = False,
            line = dict(
                color = (colors[party]),
                width = 1,
                # line = dict(width = 1),
                # dash = 'dot',
            ))
        data.append(trace)

    # Edit the layout
    layout = dict(
        # title = 'Antal procent av anföranden som efterföljs med applåder per parti',
        # xaxis = dict(title = 'Mandatperiod'),
        yaxis = dict(title = 'Procent applåder'),
    )

    layout.update(dict(shapes = [ {
            'type': 'rect',
            # x-reference is assigned to the x-values
            'xref': 'x',
            # y-reference is assigned to the plot paper [0,1]
            'yref': 'y',
            'x0': '2014-10-13',
            'y0': 0,
            'x1': '2014-10-16',
            'y1': 0.2,
            'fillcolor': '#333333',
            # 'fillcolor': '#d3d3d3',
            'opacity': 1.0,
            # 'opacity': 0.3,
            'line': {
                'width': 0,
            }
        }]
        ))

    fig = dict(data=data, layout=layout)
    pyoff.plot(fig, filename='styled-line.html')

    return


by_party()
