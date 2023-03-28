import requests
from bs4 import BeautifulSoup

response = requests.get('https://ru.investing.com/crypto/bitcoin')

soup = BeautifulSoup(response.text, 'html.parser')

scope = soup.find_all('div', 'top bold inlineblock')

for elements in scope:
    price = elements.find('span', 'pid-1057391-last').text
    print(price)