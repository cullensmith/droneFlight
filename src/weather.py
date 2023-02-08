import requests


s = requests.session()

def get_cell(x,y):
    url = f'https://api.weather.gov/points/{x},{y}'
    r = s.get(url)
    props = r.json()['properties']
    return props

def get_forecast(props):
    gx, gy = props["gridX"],props["gridY"]
    url = f'https://api.weather.gov/gridpoints/TOP/{gx},{gy}/forecast/hourly'
    r = s.get(url)
    hourly = r.json()['properties']['periods']
    return hourly
    # for i in r.json()['properties']['periods']:
    #     print(i)
 

