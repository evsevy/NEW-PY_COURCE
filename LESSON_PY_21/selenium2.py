
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


url = 'https://www.wildberries.ru/'

service = Service(executable_path='C:/chromedriver/chromedriver')  # указываем путь до драйвера
browser = webdriver.Chrome(service=service)

try:
    browser.get(url)
    time.sleep(2)
    wb_search = browser.find_element(By.ID, 'searchInput')
    wb_search .send_keys('iphone')
    wb_search .send_keys(Keys.ENTER)
    time.sleep(5)

    goods = browser.find_elements(By.CLASS_NAME, 'product-card')  # находим все товары на странице
    goods[0].click()  # выбор 1 элемента из списка товаров на странице
    time.sleep(5)

    """Вытаскиваем название, артикул, количество продаж и отзывов"""
    good_name = browser.find_element(By.CLASS_NAME, 'product-page__header')
    good_id = browser.find_element(By.ID, 'productNmId')
    good_sells = browser.find_element(By.CLASS_NAME, 'product-order-quantity')
    review = browser.find_element(By.CLASS_NAME, 'product-review__count-review')
    print(f'Название: {good_name.text}\nАртикул: {good_id.text}\n{good_sells.text} {review.text}')
    time.sleep(1)

    if int(review.text.split(' ')[0]) > 0:  # если отзывов более 0, то пролистываем страницу
        while True:
            browser.execute_script("window.scrollBy(0,575)")
            try:
                """применим неявные ожидания, будем пролистывать, пока элемент не станет кликабельным"""
                WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Смотреть все отзывы'))).click()
                break  # как нажали элемент выходим с цикла
            except:
                continue
    else:
        print('У данного товара нет отзывов')
    time.sleep(3)

    feedbacks_list = browser.find_elements(By.CLASS_NAME, 'comments__item')
    for feedback in feedbacks_list:
        autor = feedback.find_element(By.CLASS_NAME, 'feedback__info').text.replace('\n', ' ')
        text_review = feedback.find_element(By.CSS_SELECTOR, 'p[itemprop="reviewBody"]').text
        vote = feedback.find_element(By.CLASS_NAME, 'vote__wrap').text.split('\n')
        print(f'{autor}\nОтзыв:\n{text_review}\nОценка отзыва:\nположительно: {vote[0]}\nотрицательно: {vote[-1]}\n')

    browser.quit()
    
except Exception as ex:
    print(ex)
    browser.quit()
browser.quit()
