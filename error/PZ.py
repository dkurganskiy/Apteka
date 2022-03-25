import requests
from bs4 import BeautifulSoup
import csv
import datetime



HOST = "https://planetazdorovo.ru/"
URL = "https://planetazdorovo.ru/catalog/"


now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")


name = "Планета Здоровья"


linklist = ["https://planetazdorovo.ru/search/?q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
            "https://planetazdorovo.ru/search/?q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6",
            "https://planetazdorovo.ru/search/?q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
            "https://planetazdorovo.ru/search/?q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE",
            "https://planetazdorovo.ru/search/?q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82",
            "https://planetazdorovo.ru/search/?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
            "https://planetazdorovo.ru/search/?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB",
            "https://planetazdorovo.ru/search/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F",
            "https://planetazdorovo.ru/search/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
            "https://planetazdorovo.ru/search/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
            "https://planetazdorovo.ru/search/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C",
            "https://planetazdorovo.ru/search/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
            "https://planetazdorovo.ru/search/?q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
            "https://planetazdorovo.ru/search/?q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
            "https://planetazdorovo.ru/search/?q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
            "https://planetazdorovo.ru/search/?q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
            "https://planetazdorovo.ru/search/?q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
            "https://planetazdorovo.ru/search/?q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB",
            "https://planetazdorovo.ru/search/?q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
            "https://planetazdorovo.ru/search/?q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
            "https://planetazdorovo.ru/search/?q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
            "https://planetazdorovo.ru/search/?q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
            "https://planetazdorovo.ru/search/?q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
            "https://planetazdorovo.ru/search/?q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
            "https://planetazdorovo.ru/search/?q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
            "https://planetazdorovo.ru/search/?q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D1%80%D0%BE%D0%BC",
            "https://planetazdorovo.ru/search/?q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
            "https://planetazdorovo.ru/search/?q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
            "https://planetazdorovo.ru/search/?q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
            "https://planetazdorovo.ru/search/?q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
            "https://planetazdorovo.ru/search/?q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
            "https://planetazdorovo.ru/search/?q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
            "https://planetazdorovo.ru/search/?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
            "https://planetazdorovo.ru/search/?PAGEN_1=2&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
            "https://planetazdorovo.ru/search/?PAGEN_1=3&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
            "https://planetazdorovo.ru/search/?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC",
            "https://planetazdorovo.ru/search/?q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81",
            "https://planetazdorovo.ru/search/?q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA",
            "https://planetazdorovo.ru/search/?q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
            "https://planetazdorovo.ru/search/?q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF",
            "https://planetazdorovo.ru/search/?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
            "https://planetazdorovo.ru/search/?q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
            "https://planetazdorovo.ru/search/?q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
            "https://planetazdorovo.ru/search/?q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%B4%D0%BE%D0%BD%D0%B0",
            "https://planetazdorovo.ru/search/?q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE",
            "https://planetazdorovo.ru/search/?q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
            "https://planetazdorovo.ru/search/?q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB",
            "https://planetazdorovo.ru/search/?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82",
            "https://planetazdorovo.ru/search/?q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
            "https://planetazdorovo.ru/search/?q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
            "https://planetazdorovo.ru/search/?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
            "https://planetazdorovo.ru/search/?q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D0%BB+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
            "https://planetazdorovo.ru/search/?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
            "https://planetazdorovo.ru/search/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
            "https://planetazdorovo.ru/search/?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
            "https://planetazdorovo.ru/search/?q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
            "https://planetazdorovo.ru/search/?q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
            "https://planetazdorovo.ru/search/?q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
pages = {}
prep = []
for i in range(len(linklist)):
    respone = requests.get(linklist[i])
    html = respone.text
    print(html)



    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="card-list__element")
    if not items:
        print("не туда")


    # берем данные с каждой карточки
    for item in items:
        prep.append(
            {
            'title': item.find("div", class_="product-card__title").find("span").text.strip(),
            'price': item.find("div", class_="product-card__price").text.strip(),
            'link': "https://planetazdorovo.ru/" + item.find("div", class_="product-card__title").find("a").get("href")
            }
        )


print(prep)
with open(f"PZ_{date}.csv", 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
    for item in prep:
        writer.writerow([date, '', item['title'], name, item['link'], 'Москва и МО', item['price']])


# Qrator защищает