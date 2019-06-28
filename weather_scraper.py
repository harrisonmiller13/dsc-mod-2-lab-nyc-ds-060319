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
        self.df['unix_Date'] = (df['Date'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')
        self.df.sort_values(by = 'Date', inplace = True)



class weather_scrape(self):
    def __init__(self):
        self.url = 'https://api.darksky.net/forecast/'
        self.key = "API_Key"
        self.berlin_lat = "52.5200"
        self.berlin_long = "13.4050"
        self.url_base = "https://api.darksky.net/forecast"
        self.exclude = 'daily,flags,minutely,hourly,alerts'

    def api_call(self,date):
        
        payload = {'key':API_Key,'latitude':'52.52437','longitude': '13.41053','time':df['Date'],'exclude': ['minutely','hourly','daily','alerts','flags']}
        response = requests.get(self.url,params=payload)
       #dark sky not liking how requests is forming the url query... T-T
        if response.status_code == 200:
            return response
        else:
            return ValueError
        weather_data = response.json()['currently']['summary']

    def its_gon_rain(self,weather_data):
        if weather_data == 'rain':
            return True
        else:
            return False

    def all_the_weather(self,dates):
        weather_dict = {}

        for date in dates:
            
        


