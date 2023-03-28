import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
urls = [
    'searchenginejournal.com',
    'moz.com',
    'searchengineland.com'
    ]
 
indexes = {}
xpath = '//*[@id="result-stats"]'
 
def get_index(url,xpath,headless=True):
    '''
    Run Selenium.
    Get number of indexed pages.
    url: full url that you want to extract
    headless: define if your want to see the browser opening or not.
    '''
    print(f'Opening {url}')
    options = Options()
    options.headless = headless
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    index = driver.find_element_by_xpath(xpath).text
    index = index.split('About ')[1].split(' results')[0]
    print(f'Index: {index}')
    driver.quit()
    return index
 
for url in urls:
    search_url = f'https://www.google.com/search?q=site%3A{url}&oq=site%3A{url}&aqs=chrome..69i57j69i58.6029j0j1&sourceid=chrome&ie=UTF-8'
    index = get_index(search_url,xpath,headless=True)
    indexes[url] = index 
    time.sleep(1)
 
df = pd.DataFrame.from_dict(indexes, orient='index', columns=['indexed_pages'])
df.to_csv('indexed_pages.csv')
