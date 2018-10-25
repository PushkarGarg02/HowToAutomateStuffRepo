#! python3

import requests, json, sys

if len(sys.argv) > 3:
	print('Usage: fetchWeatherData.py location')
	sys.exit()

location = ','.join(sys.argv[1:])

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()
weatherData=json.loads(response.text)
print(weatherData)


'''
http://api.openweathermap.org/data/2.5/forecast/daily?q=Sanfrancisco,CA&cnt=3
'''

