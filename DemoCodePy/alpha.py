from selenium import webdriver
import requests
import selenium
from bs4 import BeautifulSoup

PATH = "C:\Apps\chromedriver.exe"
driver=webdriver.Chrome(PATH)

url="https://jysanbank.kz/en/deposit/sandyq-plus"
url1="https://bank.forte.kz/deposits"

# response = requests.get(url).text
# soup = BeautifulSoup(response, "lxml")
# tags = soup.find_all('table', class_='responsive')

# data = {}

# gdp_table = soup.find("table", attrs={"class": "wikitable"})
# gdp_table_data = gdp_table.tbody.find_all("tr")
# print(tags.text)

#---
driver.get(url)
print(driver.title)
mian= driver.find_elements_by_class_name("promo-features-item-value-text")
print(mian[2].text[-3:])
driver.quit()
#---

# driver.get(url1)
# print(driver.title)

# elements=driver.find_elements_by_class_name("depositRatesTable__StyledTable-jj2tk2-0 lfwzMN")
# print(elements.text)

# driver.quit()