from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

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


df = pd.DataFrame({'Дата':data, 'БВУ':bank, 'Депозит':deposit, 'Сроч/несроч': sroch, 'C/без попол.': popol, 'процент':percent}) 


# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

sheet = client.open("База данных депозитов БВУ РК ")
sheet_instance = sheet.get_worksheet(1)

sheet_instance.insert_rows(df.values.tolist())
