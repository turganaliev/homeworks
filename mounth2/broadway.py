import requests
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get('https://broadway.kg/reserve/')
response_text = response.text
html = BeautifulSoup(response_text, 'lxml')
section = html.find('body').find_all('section')
uls = section[1].find('div', class_='nano-content').find_all('ul')
list = []
for i in uls:
    list.append(
        {'time': i.find_all('li')[0].text,
         'name': i.find_all('li')[1].text,
         'price': i.find_all('li')[2].text,
         'hall': i.find_all('li')[3].text,
         }
    )

pprint(list)