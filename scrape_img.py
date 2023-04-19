from bs4 import BeautifulSoup
import requests
import urllib.request

URL = 'https://brigandine.fandom.com/wiki/Characters_(The_Legend_of_Runersia)'

source = requests.get(URL).text
soup = BeautifulSoup(source, 'lxml')

tables = soup.find_all('table', class_='fandom-table')

character_urls = {}

for table in tables:
    for anchor in table.find_all('a'):
        href = anchor.get('href')
        title = anchor.get('title')
        character_urls[title] = f'https://brigandine.fandom.com{href}'

for character_name, character_url in list(character_urls.items()):
    soup = BeautifulSoup(requests.get(character_url).text, 'lxml')
    try:
        character_img_url = soup.find('a', class_='image image-thumbnail').get('href')
        img_extension = character_img_url.split('revision')[0].split('.')[-1].split('/')[0]
        img_data = requests.get(character_url).content
        urllib.request.urlretrieve(character_img_url, f"data\photo\{character_name}.{img_extension}")
        # with open(f'data\photo\{character_name}.{img_extension}', 'wb') as handler:
        #     handler.write(img_data)
    except AttributeError:
        pass