import urllib.request
import json



def address(lat,lon):
    key='bdc_e37e247a86e143b8b1e86fd62ecbe215'
    url=f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={key}'
    request = urllib.request.urlopen(url)
    result=json.loads(request.read())
    return result