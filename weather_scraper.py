# Class to scrape the weather for the 2011 season
# Berlin coords 52.52437,13.41053
#######======================check which api key to use before running==============##############
from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
from apikey import *


class weather_prepare:
    def __init__(self):
        self.df = df

    # prepare date for use in dark sky api -> convert to unix time
    def prepare_dataframe_for_weather(self):
        
        df.set_index('Match_ID', inplace = True)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Unix_Date'] = (df['Date'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')
    

class weather_scrape:
    def __init__(self):
        self.url = 'https://api.darksky.net/forecast'
        self.key = API_Key
        self.latitude = "52.5200"
        self.longitude = "13.4050"
        self.exclude = 'currently,flags,minutely,hourly,alerts'

    def api_call(self,date):
    
        good_url = "{}/{}/{},{},{}?exclude={}".format(self.url,self.key,self.latitude, self.longitude, date, self.exclude)
        
        response = requests.get(good_url)
        print(response)
        weather = response.json()['daily']['data'][0]['icon']
        return weather


    def all_the_weather(self,dates):
        weather_dict = {}
        for date in dates:
            weather_data = api_call(date)
            weather_dict.update({date: weather_data})
        return weather_dict
            

    def adding_weather_to_df(self):
        weather_dict = get_all_weather(self, df.Unix_Date)
        wdf = pd.DataFrame(weather_dict, index = ['weather'])
        wdf2 = pd.DataFrame.transpose(wdf)
        wdf2 = wdf2.reset_index()
        wdf2.rename(columns={'index': 'Unix_Date'}, inplace=True)
        pd.merge(df, wdf2, how = 'left', on = 'Unix_Date')
        return df.head()

        


