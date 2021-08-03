#!python
from selenium import webdriver
import requests
import selenium
from bs4 import BeautifulSoup
import pandas as pd
import csv
import io
import schedule
import time
from datetime import date
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# PATH = "C:\Apps\chromedriver.exe"
# driver=webdriver.Chrome(PATH)
# today = date.today() 

url="https://jysanbank.kz/en/deposit/sandyq-plus"
url01="https://jysanbank.kz/en/deposit/tulpar"
url02="https://jysanbank.kz/en/deposit/aqyl"
url1="https://www.sberbank.kz/ru/small_business/sb_deposits/deposits/mobile"
url11="https://www.sberbank.kz/ru/small_business/sb_deposits/deposits/standard"
url12="https://www.sberbank.kz/ru/small_business/sb_deposits/deposits/corporate"
url13="https://www.sberbank.kz/ru/small_business/sb_deposits/deposits/accumulative"
url14="https://www.sberbank.kz/ru/corporate_customers/cc_deposits/cc_deposits"
url2 = "https://kaspi.kz/bank/bpm/products/deposit?startedFrom=main&ap-product=deposit&ae=auth-start,auth-complete"
url3 ="https://www.kdif.kz/bankam/predelnye-stavki-voznagrazhdeniya/"


# url1="https://bank.forte.kz/deposits"
# url2="https://bankffin.kz/ru/deposits/jr/3"
# url3="https://www.bcc.kz/product/champion/"
# url4="https://eubank.kz/deposits/temporary-savings-account-deposit/"
# url5="https://hcsbk.kz/ru/save/deposit-baspana/"
# url6="https://alfabank.kz/persons/deposits/"
# url7="https://www.vtb-bank.kz/individuals/srochnye-vklady/vklad-sberegatelnyy/"

#---
from time import time, sleep    
while True:
    PATH = "C:\Parser2000\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"')
    driver=webdriver.Chrome(PATH, chrome_options=chrome_options)
    today = date.today() # сегодняшнаяя дата 
    # sleep(86400)
    # sleep(86400 - time() % 86400)
    sleep(60 - time() % 60)
    data=today.strftime("%d/%m/%Y")



    
    #---Jusan1
    driver.get(url)
    print(driver.title)
    jusan= driver.find_elements_by_class_name("promo-features-item-value-text")
    print(jusan[2].text[-3:])
    say1title=driver.find_elements_by_xpath("/html/body/main/div/div/div[1]/div/div/div[1]/div[1]/div")
    justit1=say1title[0].get_attribute('textContent')
    say1=jusan[2].text[-3:]
    #---

    #---Jusan2
    driver.get(url01)
    print(driver.title)
    jusan1= driver.find_elements_by_class_name("promo-features-item-value-text")
    print(jusan1[2].text[-4:])
    say2title=driver.find_elements_by_xpath("/html/body/main/div/div/div[1]/div/div/div[1]/div[1]/div")
    justit2=say2title[0].get_attribute('textContent')
    say2= jusan1[2].text[-4:]
    #---

    #---Jusan3
    driver.get(url02)
    print(driver.title)
    jusan2= driver.find_elements_by_class_name("promo-features-item-value-text")
    print(jusan2[2].text[-4:])
    say3title=driver.find_elements_by_xpath("/html/body/main/div/div/div[1]/div/div/div[1]/div[1]/div")
    justit3=say3title[0].get_attribute('textContent')
    say3= jusan2[2].text[-4:]
    #---

    #---Sber
    driver.get(url1)
    print(driver.title)
    sber1title=driver.title
    sber1= driver.find_elements_by_xpath("//*[@id=\"main\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[5]/div[2]/div/div/div/div[3]/div/div/div/div/table/tbody/tr[2]/td[2]/p")
    print(sber1[0].get_attribute('textContent'))
    sber1title=driver.find_elements_by_xpath("//*[@id=\"main\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/h1")
    sbertit1=sber1title[0].get_attribute('textContent')
    sbData1=sber1[0].get_attribute('textContent')
    #---

    #---Sber2
    driver.get(url11)
    print(driver.title)
    sber2= driver.find_elements_by_xpath("//*[@id=\"main\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[5]/div[2]/div/div/div/div[3]/div/div/div/div/table/tbody/tr[2]/td[2]/p")
    print(sber2[0].get_attribute('textContent'))
    sber2title=driver.find_elements_by_xpath("//*[@id=\"main\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/h1")
    sbertit2=sber2title[0].get_attribute('textContent')
    sbData2=sber2[0].get_attribute('textContent')
    #---

    #---Sber3
    driver.get(url12)
    print(driver.title)
    sber3= driver.find_elements_by_xpath("//*[@id=\"main\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[4]/div[2]/div/div/div/div[3]/div/div/div/div/table/tbody/tr[2]/td[2]/p")
    print(sber3[0].get_attribute('textContent'))
    sber3title=driver.find_elements_by_xpath("//*[@id=\"main\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/h1")
    sbertit3=sber3title[0].get_attribute('textContent')
    sbData3=sber3[0].get_attribute('textContent')
    #---

    #---Sber4
    driver.get(url13)
    print(driver.title)
    sber4= driver.find_elements_by_xpath("//*[@id=\"main\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[5]/div[2]/div/div/div/div[3]/div/div/div/div/table/tbody/tr[2]/td[2]/p")
    print(sber4[0].get_attribute('textContent'))
    sber4title=driver.find_elements_by_xpath("//*[@id=\"main\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/h1")
    sbertit4=sber4title[0].get_attribute('textContent')
    sbData4=sber4[0].get_attribute('textContent')
    #---

    #---Kaspi
    driver.get(url2)
    print(driver.title)
    kaspi= driver.find_elements_by_xpath("//*[@id=\"app\"]/div[2]/div[1]/div[2]/div[1]/div[2]")
    print(kaspi[0].get_attribute('textContent')[-2:])
    kaspitit='Каспи Депозит'
    ksp=kaspi[0].get_attribute('textContent')[-2:]

    
    #---KFGD1
    driver.get(url3)
    print(driver.title)
    kfgd1= driver.find_elements_by_xpath("/html/body/main/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[4]")
    print(kfgd1[0].get_attribute('textContent')+'%')
    kfgdper1=kfgd1[0].get_attribute('textContent')+'%'
    kfgdtitle=driver.title
    
    #---
    #---KFGD2
    driver.get(url3)
    print(driver.title)
    kfgd2= driver.find_elements_by_xpath("/html/body/main/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[6]")
    print(kfgd2[0].get_attribute('textContent')+'%')
    kfgdper2=kfgd2[0].get_attribute('textContent')+'%'
    kfgdtitle=driver.title
    #---
    #---KFGD3
    driver.get(url3)
    print(driver.title)
    kfgd3= driver.find_elements_by_xpath("/html/body/main/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[4]")
    print(kfgd3[0].get_attribute('textContent')+'%')
    kfgdper3=kfgd3[0].get_attribute('textContent')+'%'
    kfgdtitle=driver.title
    #---
    #---KFGD4
    driver.get(url3)
    print(driver.title)
    kfgd4= driver.find_elements_by_xpath("/html/body/main/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[6]")
    print(kfgd4[0].get_attribute('textContent')+'%')
    kfgdper4=kfgd4[0].get_attribute('textContent')+'%'
    kfgdtitle=driver.title
    #---
    #---KFGD5
    driver.get(url3)
    print(driver.title)
    kfgd5= driver.find_elements_by_xpath("/html/body/main/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[11]/td[4]")
    print(kfgd5[0].get_attribute('textContent')+'%')
    kfgdper5=kfgd5[0].get_attribute('textContent')+'%'
    kfgdtitle=driver.title
    #---
    #---KFGD6
    driver.get(url3)
    print(driver.title)
    kfgd6= driver.find_elements_by_xpath("/html/body/main/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[11]/td[6]")
    print(kfgd6[0].get_attribute('textContent')+'%')
    kfgdper6=kfgd6[0].get_attribute('textContent')+'%'
    kfgdtitle=driver.title
    with io.open('BVUDB.csv', mode='a', encoding="utf-8", newline='') as parsBank:
        fieldnames = ['Дата', 'Банк/КФГД', 'Депозит', 'Тип', 'C/без попол.', 'процент']
        writer = csv.DictWriter(parsBank, fieldnames=fieldnames)

        # writer.writeheader()
        writer.writerow({'Дата': data,'Банк/КФГД': 'Jusan Bank','Депозит': justit1.strip(),'Тип': 'сберегательный','C/без попол.': 'без пополнения', 'процент': say1})
        writer.writerow({'Дата': data,'Банк/КФГД': 'Jusan Bank','Депозит': justit2.strip(),'Тип': 'сберегательный','C/без попол.': 'с пополнениями',  'процент': say2})
        writer.writerow({'Дата': data,'Банк/КФГД': 'Jusan Bank','Депозит': justit3.strip(),'Тип': 'сберегательный','C/без попол.': 'с пополнениями',  'процент': say3})
        writer.writerow({'Дата': data,'Банк/КФГД': 'Sber Bank','Депозит': sbertit1.strip(),'Тип': 'несрочный','C/без попол.': 'с пополнениями',  'процент': sbData1})
        writer.writerow({'Дата': data,'Банк/КФГД': 'Sber Bank','Депозит': sbertit2.strip(),'Тип': 'срочный','C/без попол.': 'без пополнения', 'процент': sbData2})
        writer.writerow({'Дата': data,'Банк/КФГД': 'Sber Bank','Депозит': sbertit3.strip(),'Тип': 'несрочный','C/без попол.': 'с пополнениями',  'процент': sbData3})
        writer.writerow({'Дата': data,'Банк/КФГД': 'Sber Bank','Депозит': sbertit4.strip(),'Тип': 'сберегательный','C/без попол.': 'с пополнениями',  'процент': sbData4})
        writer.writerow({'Дата': data,'Банк/КФГД': 'Kaspi Bank','Депозит': kaspitit.strip(),'Тип': 'несрочный','C/без попол.': 'с пополнениями',  'процент': ksp})
        writer.writerow({'Дата': data,'Банк/КФГД': 'КФГД','Депозит': 'Несрочный депозит','Тип': 'несрочный','C/без попол.': 'с пополнениями',  'процент': kfgdper1})
        writer.writerow({'Дата': data,'Банк/КФГД': 'КФГД','Депозит': 'Несрочный депозит','Тип': 'несрочный','C/без попол.': 'без пополнения',  'процент': kfgdper2})
        writer.writerow({'Дата': data,'Банк/КФГД': 'КФГД','Депозит': 'Срочный депозит','Тип': 'срочный','C/без попол.': 'с пополнениями',  'процент': kfgdper3})
        writer.writerow({'Дата': data,'Банк/КФГД': 'КФГД','Депозит': 'Срочный депозит','Тип': 'срочный','C/без попол.': 'без пополнения',  'процент': kfgdper4})
        writer.writerow({'Дата': data,'Банк/КФГД': 'КФГД','Депозит': 'Сберегательный депозит','Тип': 'сберегательный','C/без попол.': 'с пополнениями',  'процент': kfgdper5})
        writer.writerow({'Дата': data,'Банк/КФГД': 'КФГД','Депозит': 'Сберегательный депозит','Тип': 'сберегательный','C/без попол.': 'без пополнения',  'процент': kfgdper6})


    data = [] # Дата
    bank = [] # Банк Второго Уровня
    deposit = [] # название депозита
    sroch = [] # срочный или несрочный
    popol = [] # с пополнением или без
    percent =[] # процент ставки


    #FORTEBank
    while True:
        try:
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
            break
        except:
            driver.refresh()
   
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

    data.append(today.strftime("%d/%m/%Y"))
    bank.append("HalykBank")
    deposit.append("Оптимальный")
    sroch.append("срочныый")
    popol.append("с пополнениями")

    halyk1 = soup.find("div", "swiper-slide swiper-slide-visible")
    percent.append(halyk1.find('div', attrs={'class':'item-num'}).text)

    #HALYKBank


    df = pd.DataFrame({'Дата':data, 'БВУ':bank, 'Депозит':deposit, 'Сроч/несроч': sroch, 'C/без попол.': popol, 'процент':percent}) 

    df.to_csv('BVUDB.csv', mode='a', header=False, index=False)

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
        
    driver.quit()

    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)

    spreadsheet = client.open("База данных депозитов БВУ РК ")

    with open('BVUDB.csv', 'r' , encoding="latin-1") as file_obj:
        content = file_obj.read()
        client.import_csv(spreadsheet.id, data=content)



    #---


#------Working Code for future usage------

#---
# data =[]
# driver.get(url2)
# print(driver.title)
# content = driver.page_source
# soup = BeautifulSoup(content,"lxml")
# for a in soup.findAll(attrs={'class':'other-percentages'}):
#     name=a.find('span')
#     data.append(name.text)
# print(data)
#---

#---
# driver.get(url3)
# print(driver.title)
# bcc= driver.find_element_by_class_name("jq_calc_rate")
# print(bcc.text)
#---

#---
# driver.get(url4)
# print(driver.title)
# eubank= driver.find_elements_by_class_name("elementor-element-overlay")
# print(eubank[1].text)
#---

#---
# driver.get(url5)
# print(driver.title)
# hcsbk= driver.find_elements_by_class_name("dc-interest-rate")
# print(hcsbk[0].text[:3])
#---

#---
# driver.get(url6)
# print(driver.title)
# alphabank= driver.find_elements_by_class_name("CompactLoanFeatures__title")
# print(alphabank[2].text[-5:])
#---

#---
# driver.get(url7)
# print(driver.title)
# vtb= driver.find_elements_by_class_name("table-wrap")
# print(vtb[1].text[190: -58]+' %')
# driver.quit()
#---




#---------Code under work--------

# driver.get(url4)
# print(driver.title)
# req = requests.get(url4)
# html_text = str(req.content.decode())
# soup = BeautifulSoup(html_text, 'html.parser')
# for tag in soup.find_all('p'):
#     for t in tag.find_all('div', class_='elementor-element-overlay'):
#         print(tag.text)

# tbl = driver.find_element_by_xpath("/html/body/div[1]/div/div/main/section[2]/div/table").get_attribute('strong')
# df  = pd.read_html(tbl)

# response = requests.get(url).text
# soup = BeautifulSoup(response, "lxml")
# tags = soup.find_all('table', class_='responsive')

# data = {}

# gdp_table = soup.find("table", attrs={"class": "wikitable"})
# gdp_table_data = gdp_table.tbody.find_all("tr")
# print(tags.text)

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
