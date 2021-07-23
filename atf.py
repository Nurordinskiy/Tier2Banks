from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

percent =[]
driver.get("https://www.atfbank.kz/phys/deposits")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll(attrs={'class':'product__data'}):
    name=a.find('span', attrs={'class':'product__string'})
    percent.append(name.text)
print(percent)

