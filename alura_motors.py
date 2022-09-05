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

    for item in soup.find_all('img', alt='Foto'):
        links_imagens = item.get('src')
        print(links_imagens)

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)
