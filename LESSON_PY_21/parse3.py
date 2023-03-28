import random
import re
import time
import pandas
import requests
from bs4 import BeautifulSoup
from pandas import ExcelWriter

def get_html(url, params=None):
    """ получение кода страницы """
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0)"
    }
    html = requests.get(url, headers=headers, params=params)
    return html

def get_pages(html):
    """ получаем количество страниц """
    soup = BeautifulSoup(html.text, 'html.parser')
    # находим кол-во страниц, иначе количество страниц равно 1
    try:
        pages = soup.find('span', {'data-marker': 'pagination-button/next'}).previous_element
    except:
        pages = 1
    print('Количество найденных страниц: ', pages)
    return pages

def get_content(html):
    """ сбор контента со страницы """
    soup = BeautifulSoup(html.text, 'lxml')
    blocks = soup.find_all('div', class_=re.compile('iva-item-content'))
    # сбор данных с страницы
    data = []
    for block in blocks:
        data.append({
            "Наименование": block.find('h3', class_=re.compile('title-root')).get_text(strip=True),
            'Цена': block.find('span', class_=re.compile('price-text')).get_text(strip=True).replace('₽', '').replace('\xa0', ''),
            'Город': block.find('a', class_=re.compile('link-link')).get('href').split('/')[1],
            'Район': block.find('div', class_=re.compile('geo-root')).get_text(strip=True),
            'Ссылка': url + block.find('a', class_=re.compile('link-link')).get('href'),
        })
    return data

# Создали фрейм собранных данных:

df_data = pandas.DataFrame(data)
# Далее чистим данные от дубликатов

data_clear = df_data.drop_duplicates('Ссылка')
# и само сохранение в файл .xlsx

writer = ExcelWriter(f'{file_name}.xlsx')
data_clear.to_excel(writer, f'{file_name}')
writer.save()

def save_excel(data, file_name):
    # сохраняем полученные данные в эксель через pandas
    df_data = pandas.DataFrame(data)
    print(f'До удаления дубликатов: {len(df_data)} записей')
    # чистим дубликаты записей (проплаченные посты дублируются на разных страницах)
    data_clear = df_data.drop_duplicates('Ссылка')
    print(f'После удаления дубликатов: {len(data_clear)} записей')
    writer = ExcelWriter(f'{file_name}.xlsx')
    data_clear.to_excel(writer, f'{file_name}')
    writer.save()
    print(f'Данные сохранены в файл "{file_name}.xlsx"')
    
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
