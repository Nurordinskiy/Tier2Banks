from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd

driver = webdriver.Chrome("/usr/local/bin/chromedriver")



#driver.implicitly_wait(20)




today = date.today() # сегодняшнаяя дата 


data = [] # Дата
bank = [] # Банк Второго Уровня
deposit = [] # название депозита
sroch = [] # срочный или несрочный
popol = [] # с пополнением или без
percent =[] # процент ставки


#FORTEBank
driver.get("https://bank.forte.kz/deposits")
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")


data.append(today.strftime("%d/%m/%Y"))
bank.append("ForteBank")
deposit.append("в приложении")
sroch.append("несрочный")
popol.append("с пополнениями")

forte = soup.find_all("td", "MuiTableCell-root MuiTableCell-body")
percent.append((forte[10].find('span')).text)
#FORTEBank


#HALYKBank
driver.get("https://halykbank.kz/deposit/srochnye-vklady")
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")


data.append(today.strftime("%d/%m/%Y"))
bank.append("HalykBank")
deposit.append("Универсальный")
sroch.append("несрочный")
popol.append("с пополнениями")

halyk1 = soup.find("div", "swiper-slide swiper-slide-visible swiper-slide-active")
percent.append(halyk1.find('div', attrs={'class':'item-num'}).text)


data.append(today.strftime("%d/%m/%Y"))
bank.append("HalykBank")
deposit.append("Максимальный")
sroch.append("сберегательный")
popol.append("без пополнения")

halyk1 = soup.find("div", "swiper-slide swiper-slide-visible swiper-slide-next")
percent.append(halyk1.find('div', attrs={'class':'item-num'}).text)

#HALYKBank

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
