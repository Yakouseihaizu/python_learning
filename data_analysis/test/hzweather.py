import pandas as pd
import requests as req
import json

hz_code = 101210101
hz_re_weather = req.get('http://t.weather.sojson.com/api/weather/city/'+str(hz_code))

hz_data = json.loads(hz_re_weather.text)
forecast = hz_data['data']['forecast']

df = pd.DataFrame(forecast)
aqi = df['aqi']

print("var     : {0:.2f}".format(aqi.var()))
print("mean    : {0:.2f}".format(aqi.mean()))
print("std     : {0:.2f}".format(aqi.std()))