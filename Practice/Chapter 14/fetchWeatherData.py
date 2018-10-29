#! python3

import requests, json, sys

if len(sys.argv) > 3:
	print(len(sys.argv), sys.argv[1],sys.argv[2],sys.argv[3])
	print('Usage: fetchWeatherData.py location')
	sys.exit()

location = ','.join(sys.argv[1:])
appkey = '844b6ee70e130299f79282d04f3b0d9f'

url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&appid=%s' % (location,appkey)
response = requests.get(url)
response.raise_for_status()
weatherData=json.loads(response.text)
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after Tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print()

