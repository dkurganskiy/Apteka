

import time
import requests
from bs4 import BeautifulSoup
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


# Дата прогона скрипта
now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")


# Имя аптечной сети
name = "Апрель"


# Список ссылок на препараты
linklist = ["https://apteka-april.ru/search/%D0%B0%D0%B4%D0%B0%D0%BD%D1%82", "https://apteka-april.ru/search/%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD", "https://apteka-april.ru/search/%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA", "https://apteka-april.ru/search/%D0%B0%D1%82%D1%80%D0%B8%20%D0%B8%D0%BD%D0%B6", "https://apteka-april.ru/search/%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE", "https://apteka-april.ru/search/%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA%20%D0%BE%D1%80%D1%82%D0%BE", "https://apteka-april.ru/search/%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82", "https://apteka-april.ru/search/%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD%20%D1%84%D0%BB%D1%8E%D0%B8%D0%B4", "https://apteka-april.ru/search/%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81", "https://apteka-april.ru/search/%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB", "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD%20%D1%84%D0%B8%D0%B4%D0%B8%D1%8F", "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD", "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C%20%D0%B0%D1%80%D1%82%D1%80%D0%BE", "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC", "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC%20%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C", "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81", "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE", "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82", "https://apteka-april.ru/search/%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD", "https://apteka-april.ru/search/%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD", "https://apteka-april.ru/search/%D0%B4%D0%B8%D0%B0%D1%80%D1%82", "https://apteka-april.ru/search/%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD", "https://apteka-april.ru/search/%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD", "https://apteka-april.ru/search/%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82", "https://apteka-april.ru/search/%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD", "https://apteka-april.ru/search/%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD", "https://apteka-april.ru/search/%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB", "https://apteka-april.ru/search/%D0%BE%D1%81%D1%82%20%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD", "https://apteka-april.ru/search/%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB", "https://apteka-april.ru/search/%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D0%B8%D0%BD%D1%82%D1%80%D0%B0", "https://apteka-april.ru/search/%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA", "https://apteka-april.ru/search/%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81", "https://apteka-april.ru/search/%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82", "https://apteka-april.ru/search/%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA", "https://apteka-april.ru/search/%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA", "https://apteka-april.ru/search/%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB", "https://apteka-april.ru/search/%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC", "https://apteka-april.ru/search/%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD", "https://apteka-april.ru/search/%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C", "https://apteka-april.ru/search/%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD", "https://apteka-april.ru/search/%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD", "https://apteka-april.ru/search/%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81", "https://apteka-april.ru/search/%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81", "https://apteka-april.ru/search/%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD", "https://apteka-april.ru/search/%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0", "https://apteka-april.ru/search/%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81", "https://apteka-april.ru/search/%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81", "https://apteka-april.ru/search/%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC", "https://apteka-april.ru/search/%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD", "https://apteka-april.ru/search/%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC", "https://apteka-april.ru/search/%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD", "https://apteka-april.ru/search/%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD", "https://apteka-april.ru/search/%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC", "https://apteka-april.ru/search/%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA", "https://apteka-april.ru/search/%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC", "https://apteka-april.ru/search/%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC%20%D1%82%D0%B5%D0%B2%D0%B0", "https://apteka-april.ru/search/%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF", "https://apteka-april.ru/search/%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4", "https://apteka-april.ru/search/%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF", "https://apteka-april.ru/search/%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82", "https://apteka-april.ru/search/%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD", "https://apteka-april.ru/search/%D0%B4%D0%BE%D0%BD%D0%B0", "https://apteka-april.ru/search/%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD", "https://apteka-april.ru/search/%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD", "https://apteka-april.ru/search/%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD", "https://apteka-april.ru/search/%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5%20%D0%B1%D0%B8%D0%BE", "https://apteka-april.ru/search/%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4%20%D0%B0%D1%80%D1%82%D1%80%D0%BE", "https://apteka-april.ru/search/%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB", "https://apteka-april.ru/search/%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0%20%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82", "https://apteka-april.ru/search/%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0", "https://apteka-april.ru/search/%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82", "https://apteka-april.ru/search/%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82", "https://apteka-april.ru/search/%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80%20%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC", "https://apteka-april.ru/search/%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4", "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80", "https://apteka-april.ru/search/%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB", "https://apteka-april.ru/search/%D0%BF%D1%80%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD", "https://apteka-april.ru/search/%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C", "https://apteka-april.ru/search/%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
pages = {}
prep = []


options = webdriver.FirefoxOptions()
options.set_preference("dom.webdriver.enabled", False)
options.headless = True


for i in range(len(linklist)):
    try:
        driver = webdriver.Firefox()
        driver.get(linklist[i])
        print(i)
        time.sleep(4)
        with open("seleniumPage.html", "w") as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    with open("seleniumPage.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'html.parser')
    items = soup.find_all("div", class_="c-product-card")
    if not items:
        print("не туда")


    # берем данные с каждой карточки
    try:
        for item in items:
            prep.append(
                {
                'title': item.find("span", itemprop="name").text.strip(),
                'price': item.find("div", itemprop="price").text.strip(),
                'link': linklist[i]
                }
            )
    except:
        print("Нет")

    with open(f"april{date}.csv", 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
        for item in prep:
            writer.writerow([date, '', item['title'], name, item['link'], 'Москва', item['price']])