import csv
import json
from pathlib import Path
import pandas as pd
import requests
import lxml
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import app

from dash.dependencies import Input, Output

# ignores chained operation warning in pandas
pd.options.mode.chained_assignment = None

import requests

url = 'https://www.usbr.gov/lc/region/g4000/hourly/mead-elv.html'
html = requests.get(url).content
df_list = pd.read_html(html)
df = (df_list[-1]).T
df = df.drop(['Year'])

new_cols = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]

# Renaming the columns
df.columns = new_cols
print(df)

fig0 = px.line(df, x=df.index, y=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021],
labels = {
    "value": "Water Elevation in Feet",
    "index": "Month",
    "variable" : 'Years'
})

fig0.show()
# dash app

app = dash.Dash(__name__)
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
