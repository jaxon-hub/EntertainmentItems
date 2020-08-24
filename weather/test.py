"""
@Time    : 2020/8/19 0019 23:05
@Author  : jaxon
"""
import os

import requests


name = os.getenv("city")
url = f"https://geoapi.heweather.net/v2/city/lookup?location={name}&key=d49a4c5afadc47b9b5fc70e4ae7beefa&range=cn"
a = requests.get(url)
# print(a.content)
citycode = a.json()["location"][0]["id"]
weather_url = f"http://wthrcdn.etouch.cn/weather_mini?citykey={citycode}"
b = requests.get(weather_url)
print(b.json())
# https://dev.heweather.com/docs/api/weather
# https://www.seniverse.com/pricing
# https://github.com/heweather/LocationList