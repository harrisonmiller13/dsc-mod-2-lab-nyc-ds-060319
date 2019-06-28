# Class to scrape the weather for the 2011 season
# Berlin coords 52.52437,13.41053

from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
from apikey import API_Key


class weather_prepare(self)
   def __init__(self):
        self.df = df
        
    # prepare date for use in dark sky api -> convert to unix time
    def prepare_dataframe(self):
        # self.df.drop(['Div','FTHG','FTAG','FTR','AwayTeam','HomeTeam','Season'],axis = 1, inplace = True)
        self.df.set_index('Match_ID', inplace = True)
        self.df['Date'] = pd.to_datetime(df['Date'])
        self.df['Date'] = (
            df['Date'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')
        self.df.sort_values(by = 'Date', inplace = True)



class weather_scrape(self):
    def __init__(self):
        self.url = 'https://api.darksky.net/forecast/API_Key/52.52437,13.41053,dates?exclude=minutely,hourly,daily,alerts,flags'
        self.secret_key = "API_Key"
        self.berlin_lat = "52.5200"
        self.berlin_long = "13.4050"
        self.url_base = "https://api.darksky.net/forecast"
        self.exclude = 'daily,flags,minutely,hourly,alerts'
        
    def api_call(self):
        payload = {'key':API_Key,'latitude':'52.52437','longitude': '13.41053','time':df['Date'],'exclude': ['minutely','hourly','daily','alerts','flags']}
        response = requests.get(self.url, params=payload)
        weather_data = response.json()['currently']['summary']
        for date in dates:

        return json.dumps(weather_data, indent = 2)
