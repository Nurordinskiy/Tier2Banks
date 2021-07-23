from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get("https://bank.forte.kz/deposits")

driver.maximize_window()
driver.implicitly_wait(20)

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")


today = date.today() # сегодняшнаяя дата 


data = [] # Дата
bank = [] # Банк Второго Уровня
deposit = [] # название депозита
sroch = [] # срочный или несрочный
popol = [] # с пополнением или без
percent =[] # процент ставки


#FORTEBank
data.append(today.strftime("%d/%m/%Y"))
bank.append("ForteBank")
deposit.append("в приложении")
sroch.append("срочный")
popol.append("с пополнениями")

forte = soup.find_all("span", {"class": "MuiTypography-root sc-bdnylx lTPpd MuiTypography-colorInherit"})
percent.append(forte[0].text)

print(forte)

'''
for a in soup.findAll(attrs={'class':'product__data'}):

    data.append(today.strftime("%d/%m/%Y"))
    bank.append("ForteBank")
    deposit.append("в приложении")
    sroch.append("срочный")
    popol.append("с пополнениями")

    name=a.find('span', attrs={'class':'product__string'})
    percent.append(name.text)
'''

df = pd.DataFrame({'Дата':data, 'БВУ':bank, 'Депозит':deposit, 'Сроч/несроч': sroch, 'C/без попол.': popol, 'процент':percent}) 
df.to_csv('BVU.csv', index=False, encoding='utf-8')