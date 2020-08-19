"""
@Time    : 2020/8/19 0019 23:05
@Author  : jaxon
"""
import requests

url = "http://wthrcdn.etouch.cn/weather_mini?citykey=101010100"
a = requests.get(url)
# print(a.content)
print(a.json()["data"]["forecast"])
# https://dev.heweather.com/docs/api/weather
# https://www.seniverse.com/pricing