import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import panel as pn
pn.extension()

path = 'res\WHO-COVID-19-global-data.csv'
url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
data = pd.read_csv(url)


def plot_by_country(variable='Hungary'):
    df = data.loc[data['Country'] == variable]
    date = df["Date_reported"]
    cum_cases = df["Cumulative_cases"]

    date = np.asarray(date, dtype='datetime64[s]')
    return [date, cum_cases]


countries = data.loc[data['Country']].tolist()
country = pn.widgets.Select(name='Country', options=countries)

pn.bind(plot_by_country, country=country)


interactive = pn.bind(plot_by_country, country)

first_app = pn.Column(country, interactive)
