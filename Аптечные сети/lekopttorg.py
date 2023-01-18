import time
import requests
from bs4 import BeautifulSoup
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# РАБОТАЕТ КАК НАДО


now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")

HOST = "https://lekopttorg.ru/"
URL = "https://lekopttorg.ru/catalog/"
HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
}

name = "Лекоптторг"

linklist = ["https://lekopttorg.ru/catalog/index.php?q=%D0%B0%D0%B4%D0%B0%D0%BD%D1%82&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%BE%D0%BD+%D0%B0%D1%80%D1%82%D1%80%D0%BE&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%80%D0%B8%D1%81%D0%B2%D0%B8%D1%81%D0%BA&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D1%80%D0%BE%D0%BC&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81+%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B4%D0%BE%D0%BD%D0%B0&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD&s=",
            "https://lekopttorg.ru/catalog/index.php?q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C&s="]
pages = {}
prep = []
for i in range(len(linklist)):
    respone = requests.get(linklist[i])
    html = respone.text
    print(i)

    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="col")
    if not items:
        print("не туда")

    try:
        for item in items:
            prep.append(
                {
                    'title': item.find("a", class_="product__title").text.strip(),
                    'price': item.find("span", class_="price__regular").text.strip(),
                    'link': "https://lekopttorg.ru" + item.find("a", class_="product__title").get("href")
                }
            )
    except:
        print("Нет в наличии")

print(prep)

with open(rf"C:\Users\danil\OneDrive\Документы\Python\Аптечка\Результаты парсинга\lekopttorg_{date}.csv", 'w', newline='',  encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
         'Ссылка на препарат', 'Город', 'Цена'])
    for item in prep:
        writer.writerow([date, '', item['title'], name, item['link'], 'Ижевск', item['price']])
