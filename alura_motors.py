from urllib.request import urlopen, Request, urlretrieve
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://alura-site-scraping.herokuapp.com/index.php'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}


cards = []
card = {}
acessorios = []

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    infos_carro = soup.find('div', {'class': 'body-card'}).find_all('p')
    acessorios_carro = soup.find('div', {'class': 'body-card'}).find_all('li')
    acessorios_carro.pop()

    for info in infos_carro:
        card[info.get('class')[0].split('-')[-1]] = (info.get_text()).title()

    for itens in acessorios_carro:
        acessorios.append(itens.get_text().replace('►', '').title())
        card['items'] = acessorios
 
except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)


df_carros = pd.DataFrame.from_dict(card, orient='index').transpose()

# df_carros.to_csv('dados/alura_motors.csv', index=False, encoding='utf-8-sig')


imagem = soup.find('div', {'class':'image-card'}).img
imagem.get('src').split('/')[-1]

urlretrieve(imagem.get('src'), 'imagens/' + imagem.get('src').split('/')[-1])
