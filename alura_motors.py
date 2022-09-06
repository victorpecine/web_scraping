from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

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
        card[info.get('class')[0].split('-')[-1]] = info.get_text()

    for itens in acessorios_carro:
        card['itens'] = acessorios.append(itens.get_text().replace('►', ''))

    print(card)

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)
