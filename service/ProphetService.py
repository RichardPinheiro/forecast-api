from fbprophet import Prophet
from datetime import datetime
from fbprophet.diagnostics import cross_validation, performance_metrics 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def removeOutlier(df, cutoff, column):
    df.loc[df[column] > cutoff, [column]] = None
    return df

def discreteForecast(column, value, fileinfo, periods, season_type):
    df = pd.read_csv(fileinfo)
    df['Emissão'] = pd.to_datetime(df['Emissão'])

    forecastDataset = df[df[column]==value][['Emissão', column]].sort_values(by=['Emissão']).groupby(['Emissão']).count().reset_index()
    model = Prophet().fit(forecastDataset.rename(columns={'Emissão': 'ds', column: 'y'}))
    df_cv = cross_validation(model, horizon='365 days')
    forecast = model.predict(model.make_future_dataframe(periods=periods, freq=season_type))

def continousForecast(fileinfo, periods, season_type):
    df = pd.read_csv(fileinfo, decimal=',')
    df['Emissão'] = pd.to_datetime(df['Emissão'])

    forecastDataset = df[['Emissão', 'Vl Mercad Liq']].sort_values(by=['Emissão']).groupby(['Emissão'])['Vl Mercad Liq'].sum().reset_index()
    forecastDataset = removeOutlier(forecastDataset, 600000, 'Vl Mercad Liq')

    model = Prophet().fit(forecastDataset.rename(columns={'Emissão': 'ds', continuousVar: 'y'}))
    df_p = performance_metrics(cross_validation(model, horizon='200 days', initial='500 days', period='100 days'))

    forecast = model.predict(model.make_future_dataframe(periods=periods, freq=season_type))
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv('./forcast.csv')
    # fig1 = model.plot(forecast)
    # fig1.suptitle(value, va='baseline', fontsize=15)
    # fig1.savefig('teste.png', bbox_inches = "tight")