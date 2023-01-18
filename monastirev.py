import time
import requests
from bs4 import BeautifulSoup
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


URL = "https://monastirev.ru/"
HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
}

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")

name = "Монастырев"

linklist = ["https://monastirev.ru/search?term=%D0%B0%D0%B4%D0%B0%D0%BD%D1%82",
            "https://monastirev.ru/search?term=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
            "https://monastirev.ru/search?term=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
            "https://monastirev.ru/search?term=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6",
            "https://monastirev.ru/search?term=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
            "https://monastirev.ru/search?term=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE",
            "https://monastirev.ru/search?term=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82",
            "https://monastirev.ru/search?term=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4",
            "https://monastirev.ru/search?term=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
            "https://monastirev.ru/search?term=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F",
            "https://monastirev.ru/search?term=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
            "https://monastirev.ru/search?term=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
            "https://monastirev.ru/search?term=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
            "https://monastirev.ru/search?term=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C",
            "https://monastirev.ru/search?term=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
            "https://monastirev.ru/search?term=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
            "https://monastirev.ru/search?term=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
            "https://monastirev.ru/search?term=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
            "https://monastirev.ru/search?term=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
            "https://monastirev.ru/search?term=%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
            "https://monastirev.ru/search?term=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
            "https://monastirev.ru/search?term=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
            "https://monastirev.ru/search?term=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
            "https://monastirev.ru/search?term=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
            "https://monastirev.ru/search?term=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
            "https://monastirev.ru/search?term=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
            "https://monastirev.ru/search?term=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD",
            "https://monastirev.ru/search?term=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB",
            "https://monastirev.ru/search?term=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
            "https://monastirev.ru/search?term=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
            "https://monastirev.ru/search?term=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
            "https://monastirev.ru/search?term=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
            "https://monastirev.ru/search?term=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
            "https://monastirev.ru/search?term=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
            "https://monastirev.ru/search?term=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
            "https://monastirev.ru/search?term=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC",
            "https://monastirev.ru/search?term=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
            "https://monastirev.ru/search?term=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
            "https://monastirev.ru/search?term=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
            "https://monastirev.ru/search?term=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
            "https://monastirev.ru/search?term=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
            "https://monastirev.ru/search?term=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
            "https://monastirev.ru/search?term=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
            "https://monastirev.ru/search?term=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
            "https://monastirev.ru/search?term=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
            "https://monastirev.ru/search?term=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
            "https://monastirev.ru/search?term=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
            "https://monastirev.ru/search?term=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
            "https://monastirev.ru/search?term=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81+%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC",
            "https://monastirev.ru/search?term=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD",
            "https://monastirev.ru/search?term=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
            "https://monastirev.ru/search?term=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
            "https://monastirev.ru/search?term=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA",
            "https://monastirev.ru/search?term=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
            "https://monastirev.ru/search?term=%D0%B0%D0%BB%D1%83%D1%84%D0%BB%D0%BE%D0%BF",
            "https://monastirev.ru/search?term=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
            "https://monastirev.ru/search?term=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
            "https://monastirev.ru/search?term=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
            "https://monastirev.ru/search?term=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
            "https://monastirev.ru/search?term=%D0%B4%D0%BE%D0%BD%D0%B0",
            "https://monastirev.ru/search?term=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
            "https://monastirev.ru/search?term=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
            "https://monastirev.ru/search?term=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
            "https://monastirev.ru/search?term=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE",
            "https://monastirev.ru/search?term=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
            "https://monastirev.ru/search?term=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB",
            "https://monastirev.ru/search?term=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82",
            "https://monastirev.ru/search?term=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
            "https://monastirev.ru/search?term=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
            "https://monastirev.ru/search?term=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
            "https://monastirev.ru/search?term=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
            "https://monastirev.ru/search?term=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
            "https://monastirev.ru/search?term=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
            "https://monastirev.ru/search?term=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
            "https://monastirev.ru/search?term=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
            "https://monastirev.ru/search?term=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
            "https://monastirev.ru/search?term=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
pages = {}
prep = []
for i in range(len(linklist)):
    respone = requests.get(linklist[i])
    html = respone.text
    print(i)

    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="offer")
    if not items:
        print("не туда")

    # берем данные с каждой карточки
    try:
        for item in items:
            prep.append(
                {
                    'title': item.find("div", class_="offer__title").text.strip(),
                    'title2': item.find("div", class_="offer__description").text.strip(),
                    'price': item.find("div", class_="offer__price-current").text.strip(),
                    'link': linklist[i]
                }
            )
    except:
        print("Нет")

print(prep)
with open(rf"C:\Users\danil\OneDrive\Документы\Python\Аптечка\Результаты парсинга\monastirev{date}.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
         'Ссылка на препарат', 'Город', 'Цена'])
    for item in prep:
        writer.writerow([date, '', item['title'] + item['title2'], name, item['link'], 'Москва', item['price']])