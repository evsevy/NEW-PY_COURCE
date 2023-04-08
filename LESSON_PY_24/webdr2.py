from selenium import webdriver
import time

URL = "https://coincodex.com/crypto/bitcoin/historical-data/"

driver = webdriver.Chrome(executable_path = "/usr/local/bin/chromedriver")
driver.get(URL)
time.sleep(2)

webpage = driver.page_source

from bs4 import BeautifulSoup

HTMLPage = BeautifulSoup(driver.page_source, 'html.parser')

Table = HTMLPage.find('table', class_='styled-table full-size-table')

Rows = Table.find_all('tr', class_='ng-star-inserted')
len(Rows)

# Empty list is created to store the data
extracted_data = []
# Loop to go through each row of table
for i in range(0, len(Rows)):
 try:
  # Empty dictionary to store data present in each row
  RowDict = {}
  # Extracted all the columns of a row and stored in a variable
  Values = Rows[i].find_all('td')
  
  # Values (Open, High, Close etc.) are extracted and stored in dictionary
  if len(Values) == 7:
   RowDict["Date"] = Values[0].text.replace(',', '')
   RowDict["Open"] = Values[1].text.replace(',', '')
   RowDict["High"] = Values[2].text.replace(',', '')
   RowDict["Low"] = Values[3].text.replace(',', '')
   RowDict["Close"] = Values[4].text.replace(',', '')
   RowDict["Volume"] = Values[5].text.replace(',', '')
   RowDict["Market Cap"] = Values[6].text.replace(',', '')
   extracted_data.append(RowDict)
 except:
  print("Row Number: " + str(i))
 finally:
  # To move to the next row
  i = i + 1

extracted_data = pd.DataFrame(extracted_data)
print(extracted_data)
