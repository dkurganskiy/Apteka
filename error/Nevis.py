import requests
from bs4 import BeautifulSoup
import csv
import datetime
from random import choice
from time import sleep
from random import uniform
from selenium import webdriver


now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")

HOST = "https://aptekanevis.ru/"
URL = "https://aptekanevis.ru/catalog/"


cookies = [
    {'name': "Ленинградская Область", 'cookies': {"BITRIX_CONVERSION_CONTEXT_s1": "%7B%22ID%22%3A47%2C%22EXPIRE%22%3A1636059540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; PHPSESSID=aogsqmgsc849o6asr9qg4bfffk; region=2"}},
    {'name': "Санкт-Петербург", 'cookies': {"BITRIX_CONVERSION_CONTEXT_s1": "%7B%22ID%22%3A47%2C%22EXPIRE%22%3A1636059540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; PHPSESSID=aogsqmgsc849o6asr9qg4bfffk; region=1"}},
    {'name': "Новгородская область", 'cookies': {"BITRIX_CONVERSION_CONTEXT_s1": "%7B%22ID%22%3A47%2C%22EXPIRE%22%3A1636059540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; PHPSESSID=aogsqmgsc849o6asr9qg4bfffk; region=3"}},
    {'name': "Псковская область", 'cookies': {"BITRIX_CONVERSION_CONTEXT_s1": "%7B%22ID%22%3A47%2C%22EXPIRE%22%3A1636059540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; PHPSESSID=aogsqmgsc849o6asr9qg4bfffk; region=4"}},
    {'name': "Республика Карелия", 'cookies': {"BITRIX_CONVERSION_CONTEXT_s1": "%7B%22ID%22%3A47%2C%22EXPIRE%22%3A1636059540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; PHPSESSID=aogsqmgsc849o6asr9qg4bfffk; region=5"}},
    {'name': "Мурманская область", 'cookies': {"BITRIX_CONVERSION_CONTEXT_s1": "%7B%22ID%22%3A47%2C%22EXPIRE%22%3A1636059540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; PHPSESSID=aogsqmgsc849o6asr9qg4bfffk; region=6"}}
]


name = "Невис"


linklist = ["https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B0%D0%B4%D0%B0%D0%BD%D1%82",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D1%80%D0%BE%D0%BC",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B4%D0%BE%D0%BD%D0%B0",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%BE%D0%BB",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
            "https://aptekanevis.ru/catalog/poisk-preparata.php?s=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
pages = {}


for cookie in cookies:
    prep = []

    options = webdriver.FirefoxOptions()
    options.set_preference("dom.webdriver.enabled", False)
    options.headless = True

    for i in range(len(linklist)):
        try:
            driver = webdriver.Firefox(options=options)
            sleep(uniform(0, 2))
            driver.get(linklist[i])
            print(i)

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
        items = soup.find_all("div", class_="item")
        if not items:
            print("не туда")

        try:
            for item in items:
                prep.append(
                    {
                    'title': item.find("a", class_="title").find("span").text.strip(),
                    'price': item.find("div", class_="price").text.strip(),
                    'link': "https://aptekanevis.ru" + item.find('a', class_='title').get('href')
                    }
                )
        except:
            print("Нет в наличии")


    print(prep)
    with open(f"Nevis_{date}.csv", 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
        for item in prep:
            writer.writerow([date, '', item['title'], name, item['link'], cookie['name'], item['price']])

# Разобраться в ошибке
