import requests


'''
response success

{
  "coord": {
    "lon": -122.08,
    "lat": 37.39
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 10000,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645,
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627,
    "sunset": 1560396563
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
}           
'''

API_KEY = 'YOUR_API_KEY'


def get_city(city_name):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    return requests.get(url.format(city_name, API_KEY)).json()


def is_city_exist(city):
    return city['cod'] == 200


def get_less_weather_info(city):
    temperature = city['main']['temp']

    return {
        'city': city['name'],
        'degrees_fahrenheit': temperature,
        'degrees_celsius': (temperature - 32) // 1.8,
        'description': city['weather'][0]['description'],
        'icon': city['weather'][0]['icon'],

    }
