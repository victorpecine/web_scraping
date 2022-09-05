from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

url = 'https://www.alura.com.br'
headers = {'User-Agent': 'Chrome/76.0.3809.100'}


try:
    req = Request(url)
    response = urlopen(req)
    print(response.read())

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)
