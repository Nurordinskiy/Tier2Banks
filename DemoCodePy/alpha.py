from selenium import webdriver
import requests
import selenium
from bs4 import BeautifulSoup

PATH = "C:\Apps\chromedriver.exe"
driver=webdriver.Chrome(PATH)

url="https://jysanbank.kz/en/deposit/sandyq-plus"
url1="https://bank.forte.kz/deposits"
url2="https://bankffin.kz/ru/deposits/jr/3"
url3="https://www.bcc.kz/product/champion/"


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
#---

#---
data =[]
driver.get(url2)
print(driver.title)
content = driver.page_source
soup = BeautifulSoup(content,"lxml")
for a in soup.findAll(attrs={'class':'other-percentages'}):
    name=a.find('span')
    data.append(name.text)
print(data)
#---

#---
driver.get(url3)
print(driver.title)
bcc= driver.find_element_by_class_name("jq_calc_rate")
print(bcc.text)
driver.quit()
#---


# driver.get(url1)
# print(driver.title)

# elements=driver.find_elements_by_class_name("depositRatesTable__StyledTable-jj2tk2-0 lfwzMN")
# print(elements.text)

# driver.quit()

# req = requests.get(url1)
# html_text = str(req.content.decode())
# soup = BeautifulSoup(html_text, 'html.parser')
# for tag in soup.find_all('td', class_='highlight'):
#     for t in tag.find_all('table', class_='depositRatesTable__StyledTable-jj2tk2-0 lfwzMN'):
#         print(tag.text)

# import csv
# with open("output.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerows(mian[2].text[-3:])


# html = 'https://bankffin.kz/ru/deposits/jr/3'
# req = requests.get(html)
# html_text = str(req.content.decode())
# soup = BeautifulSoup(html_text, 'html.parser')

# for tag in soup.find_all('span'):
#     for t in tag.find_all('div', class_='other-percentages'):
#      print(tag[1].text)
