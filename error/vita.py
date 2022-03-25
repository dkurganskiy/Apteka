import requests
from bs4 import BeautifulSoup
import csv
import datetime


URL = "https://vitaexpress.ru/"
HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
}


now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")


name = " Вита"


linklist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", м]
pages = {}
prep = []
for i in range(len(linklist)):
    respone = requests.get(linklist[i])
    html = respone.text
    print(i)
    print(html)


    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="search-card__content-area")
    if not items:
        print("не туда")


    # берем данные с каждой карточки
    try:
        for item in items:
            prep.append(
                {
                'title': item.find("div", class_="header-card-search").text.strip(),
                'price': item.find("div", class_="price-search__present").text.strip(),
                'link': linklist[i]
                }
            )
    except:
        print("Нет")

print(prep)
with open(f"vita{date}.csv", 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
    for item in prep:
        writer.writerow([date, '', item['title'], name, item['link'], 'Самара', item['price']])

# Города вставь