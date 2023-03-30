import requests  # для URL запроса
from bs4 import BeautifulSoup  # для работы с HTML
import time  # для установки задержки в цикле программы

sleep = 3  # время задержки


def update_ticker():
    # ссылка на тикер (Я использовал сайт google finance)
    GAZP = "https://www.google.com/" \
           "finance/quote/" \
           "GAZP:MCX?sa=X&ved=2ahUKEwjK5-z-yJLyAhUhpIsKHXbMBh0Q_AUoAXoECAEQAw"

    # заголовки для URL запроса.(добавляется к ссылке при URL запросе)
    headers = {
        'user agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.135 Safari/537.36"}

    # запрашиваем страницу по ссылке и помещаем в переменную html
    html = requests.get(GAZP, headers)

    # парсим данные в переменную soup
    soup = BeautifulSoup(html.content, 'html.parser')

    # находим интересующий нас тэг с текущим курсом
    # (В браузере используем просмотр кода элемента для того чтобы найти это значение)
    convert = soup.findAll('div', {'class': 'YMlKec fxKbKc'})

    # считываем 1й элемент как текст.
    # Делаем срез и избавляемся от знака ₽ в начале строки,
    # конвертируем строку в число типа float
    price = float(convert[0].text[1:])

    print("Цена акции Газпром: ", price)
    # устанавливаем задержку
    time.sleep(sleep)
    update_ticker()  # вызываем эту же функцию снова


update_ticker()
