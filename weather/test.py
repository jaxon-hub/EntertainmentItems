"""
@Time    : 2020/8/19 0019 23:05
@Author  : jaxon
"""
import os
import datetime
import requests


name = os.getenv("city")
url = f"https://geoapi.heweather.net/v2/city/lookup?location={name}&key=d49a4c5afadc47b9b5fc70e4ae7beefa&range=cn"
a = requests.get(url)
citycode = a.json()["location"][0]["id"]
weather_url = f"http://wthrcdn.etouch.cn/weather_mini?citykey={citycode}"
r_data = requests.get(weather_url).json()
city = r_data["data"]["city"]
ganmao = r_data["data"]["ganmao"]
weather_data = (r_data["data"]["forecast"])
nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"---------------------------当前时间为:{nowTime}---------------------------")
print("|")
for data in weather_data:
    date = data["date"]
    high = data["high"]
    low = data["low"]
    fengxiang = data["fengxiang"]
    type = data["type"]
    print(f"|                      {date}  {city}天气为：{high},{low},{fengxiang},{type}"), "|"
    print("|")
print(f"|                      {ganmao}")
print("----------------------------------------------------------------------------------")