import requests
from bs4 import BeautifulSoup

main_url = 'https://timesofindia.indiatimes.com/rss.cms'

resp = requests.get(main_url)
rss = resp.content
soup = BeautifulSoup(rss,'html.parser')

table = soup.find('div',{'id':'main-copy'}).find_all('p')[1].table.find_all('tr')

data = []

for tr in table:
	data.append({'title':tr.td.a.text, 'link':tr.td.a.get('href')})

# for d in data:
# 	print(d['title'],'   ',d['link'],'\n\n')

d = data[0]
print(d['title'],' ',d['link'],'\n\n')

rss_url = d['link']
rss_resp = requests.get(rss_url)
rss_index = rss_resp.content
rss_soup = BeautifulSoup(rss_index,'xml')

rss_data = []

rss_item = rss_soup.find_all('item')

for rss_each_item in rss_item:
	rss_data.append(
					{
					 'title':rss_each_item.title.text,
					 'description':rss_each_item.description.text,
					 'date':rss_each_item.pubDate.text
					 }
					)

for rss_d in rss_data:
	print(rss_d['title'],'\n\n',rss_d['description'],'\n\n',rss_d['date'],'\n\n')

input()