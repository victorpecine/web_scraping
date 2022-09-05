from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

url = 'https://alura-site-scraping.herokuapp.com/index.php'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}


try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    nome_carro = soup.find('p', {'class': 'txt-name'}).get_text().title()
    valor_carro = soup.find('p', {'class': 'txt-value'}).get_text()
    print('{} = {}'.format(nome_carro, valor_carro))

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)
