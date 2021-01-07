import requests
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get('http://www.cinema.kg/')
response_text = response.text
html = BeautifulSoup(response_text, 'lxml')
sections = html.find('body').find_all('section')
trs = sections[2].find('div', id="afishaContents").find('div').find('table').find_all('tr', class_='tRow tooltips')
trs_list = []
for tr in trs:
    tds = tr.find_all('td')
    tr_list = tds[0].text + ' | ' + tds[1].text + ' | ' + tds[2].text + ' | ' + tds[3].text
    trs_list.append(tr_list)

pprint(trs_list)
