from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver.get("https://coincodex.com/crypto/bitcoin/historical-data/")
headers = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table.full-size-table th")))]
dates = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table.full-size-table tr td:nth-child(1)")))]
opens = [my_elem.text.replace('\u202f', ' ') for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table.full-size-table tr td:nth-child(2)")))]
highs = [my_elem.text.replace('\u202f', ' ') for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table.full-size-table tr td:nth-child(3)")))]
lows = [my_elem.text.replace('\u202f', ' ') for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table.full-size-table tr td:nth-child(4)")))]
closes = [my_elem.text.replace('\u202f', ' ') for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table.full-size-table tr td:nth-child(5)")))]
volumes = [my_elem.text.replace('\u202f', ' ') for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table.full-size-table tr td:nth-child(6)")))]
marketcaps = [my_elem.text.replace('\u202f', ' ') for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table.full-size-table tr td:nth-child(7)")))]
df = pd.DataFrame(data=list(zip(dates, opens, highs, lows, closes, volumes, marketcaps)), columns=headers)
print(df)
driver.quit()
