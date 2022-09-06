from urllib.request import urlopen, Request, urlretrieve
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://alura-site-scraping.herokuapp.com/index.php'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}


cards = []
card = {}

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    numero_pagina = soup.find('span', class_='info-pages').get_text().split()[-1]
    numero_pagina = int(numero_pagina)
    
    for i in range(numero_pagina):
        url = url + '?page=' + str(i + 1)
        response = urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')


        anuncios = soup.find('div', {"id": "container-cards"}).findAll('div', class_="card")

        for anuncio in anuncios:
            card = {}
                    
            card['value'] = anuncio.find('p', {'class': 'txt-value'}).get_text() # Valor do carro

            infos_carros = anuncio.find('div', {'class': 'body-card'}).find_all('p')
            for info in infos_carros:
                card[info.get('class')[0].split('-')[-1]] = (info.get_text()).title()

            acessorios_carro = anuncio.find('div', {'class': 'body-card'}).find_all('li')
            acessorios_carro.pop()
            acessorios = []
            for itens in acessorios_carro:
                acessorios.append(itens.get_text().replace('►', '').title())
            card['items'] = acessorios

            cards.append(card)

            imagem = anuncio.find('div', {'class': 'image-card'}).img
            urlretrieve(imagem.get('src'), 'imagens/' + imagem.get('src').split('/')[-1])     
 
except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)


df_carros = pd.DataFrame(cards)

# df_carros.to_csv('dados/alura_motors_completo.csv', index=False, encoding='utf-8-sig')
