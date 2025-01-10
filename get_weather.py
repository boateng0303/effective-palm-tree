import urllib.request
import json


def get_weather(lat,lon):
    key='2ff976d64032a7f026ba1e1e7e769cf0'
    url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'

    request = urllib.request.urlopen(url)
    result=json.loads(request.read()) 

    return result


