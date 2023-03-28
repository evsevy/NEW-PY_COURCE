import random
import re
import time
import pandas
import requests
from bs4 import BeautifulSoup
from pandas import ExcelWriter

def parse(url):
    search = input('Введите запрос поиска: ')
    min_price = input('Введите минимальную стоимость: ')
    max_price = input('Введите максимальную стоимость: ')
    html = get_html(url, params={'bt': 1, 'pmax': max_price, 'pmin': min_price, 'q': search, 's': '2', 'view': 'gallery'})
    soup = BeautifulSoup(html.text, 'lxml')
    print(soup.h1.get_text())
    print('Ссылка со всеми параметрами:\n', html.url)
    print('Статус код сайта: ', html.status_code)
    data = []
    # проверка сайта на доступ
    if html.status_code == 200:
        # вызов функции для вывода количества найденных страниц
        get_pages(html)
        pagination = int(input('Сколько страниц спарсить? '))
        for page in range(1, pagination + 1):
            html = get_html(url, params={'bt': 1, 'p': page, 'pmax': max_price, 'pmin': min_price, 'q': search, 's': '2', 'view': 'gallery'})
            print(f'Парсинг страницы {page} из {pagination}...')
            data.extend((get_content(html)))
            time.sleep(random.randint(1, 3))
        print(f'Получили {len(data)} позиций')
        # сохраняем в эксель, передав наши собранные данные и запрос
        save_excel(data, search)
    else:
        print('Ошибка доступа к сайту')
if __name__ == "__main__":
     parse(url)
