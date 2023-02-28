import hvplot.pandas
import pandas as pd
import numpy as np
import panel as pn
import datetime as dt
import folium
import plotly.express as px
import plotly.graph_objects as go
pn.extension('plotly')


url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
data = pd.read_csv(url)
idata = data.interactive()
data['Date_reported'] = pd.to_datetime(data['Date_reported']).dt.date

date_slider = pn.widgets.DateSlider(
    name='Date', start=dt.date(2020, 1, 3), end=dt.date.today())
column = pn.widgets.Select(name='Column', options=[
                           'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths'])

df = data.loc[data["Date_reported"] == dt.date(2023, 1, 1)]

cov_pipeline = (
    idata[
        (idata.Date_reported == date_slider)
    ]
    .loc[:, ['Date_reported', 'Country']]
)
choropleth = go.Figure(data=go.Choropleth(
    locations=data["Country"],
    z=data["Cumulative_cases"],
    locationmode="country names"
))
layout = go.Layout(
    title='Scatterplot of Cumulative cases',
    width=1500,
    height=700
)
cov_plot = cov_pipeline.hvplot(choropleth)
cov_plot
