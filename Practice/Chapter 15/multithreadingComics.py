#! python3

import requests, bs4, os, threading

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'})

os.makedirs('D:\\Scripts\\xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
	for urlNumber in range(startComic, endComic):
		res = requests.get('https://www.xkcd.com/%s/' % (urlNumber))
		res.raise_for_status()
		print('I am here###############################')
		soup = bs4.BeautifulSoup(res.text)
		
		comicElem = soup.select('#comic img')
		if comicElem == []:
			print('Could not find comic image.')
		else:
			comicUrl = comicElem[0].get('src')
			res = requests.get(comicUrl)
			res.raise_for_status()
			
			imageFile = open(os.path.join('D:\\Scripts\\xkcd',os.path.basename(comicUrl)),'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()
			
		
downloadThreads=[]
for i in range(1,100,10):
	downloadThread = threading.Thread(target=downloadXkcd,args=(i,i+9))
	downloadThreads.append(downloadThread)
	downloadThread.start()
	
for downloadThread in downloadThreads:
	downloadThread.join()

print('Done')
