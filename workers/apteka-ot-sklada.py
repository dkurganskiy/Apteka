import requests
from bs4 import BeautifulSoup
import csv
import datetime


HOST = "https://planetazdorovo.ru/"
URL = "https://planetazdorovo.ru/catalog/"
HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
}



now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")


name = "Аптека от склада"


linklist = ["https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA", "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%82%D1%80%D0%B8%20%D0%B8%D0%BD%D0%B6", "https://apteka-ot-sklada.ru/catalog?q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE", "https://apteka-ot-sklada.ru/catalog?q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA%20%D0%BE%D1%80%D1%82%D0%BE", "https://apteka-ot-sklada.ru/catalog?q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82", "https://apteka-ot-sklada.ru/catalog?q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81", "https://apteka-ot-sklada.ru/catalog?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB", "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD%20%D1%84%D0%B8%D0%B4%D0%B8%D1%8F", "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C%20%D0%B0%D1%80%D1%82%D1%80%D0%BE", "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC", "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC%20%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B8%D0%B0%D0%BB%D1%8C", "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81", "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE", "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82", "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82", "https://apteka-ot-sklada.ru/catalog?q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82", "https://apteka-ot-sklada.ru/catalog?q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB", "https://apteka-ot-sklada.ru/catalog?q=%D0%9E%D0%A1%D0%A2%20%D0%A2%D0%95%D0%9D%D0%94%D0%9E%D0%9D", "https://apteka-ot-sklada.ru/catalog?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB", "https://apteka-ot-sklada.ru/catalog?q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D0%B8%D0%BD%D1%82%D1%80%D0%B0", "https://apteka-ot-sklada.ru/catalog?q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA", "https://apteka-ot-sklada.ru/catalog?q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81", "https://apteka-ot-sklada.ru/catalog?q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82", "https://apteka-ot-sklada.ru/catalog?q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA", "https://apteka-ot-sklada.ru/catalog?q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA", "https://apteka-ot-sklada.ru/catalog?q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB", "https://apteka-ot-sklada.ru/catalog?q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D1%80%D0%BE%D0%BB", "https://apteka-ot-sklada.ru/catalog?q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C", "https://apteka-ot-sklada.ru/catalog?q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81", "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81", "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0", "https://apteka-ot-sklada.ru/catalog?q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81", "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81", "https://apteka-ot-sklada.ru/catalog?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC", "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC", "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC", "https://apteka-ot-sklada.ru/catalog?q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81", "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81", "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D0%BB%D1%84%D1%83%D1%82%D0%BE%D0%BF", "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4", "https://apteka-ot-sklada.ru/catalog?q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF", "https://apteka-ot-sklada.ru/catalog?q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82", "https://apteka-ot-sklada.ru/catalog?q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%B4%D0%BE%D0%BD%D0%B0", "https://apteka-ot-sklada.ru/catalog?q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4", "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB", "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0", "https://apteka-ot-sklada.ru/catalog?q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0", "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82", "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82", "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%80", "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4", "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80", "https://apteka-ot-sklada.ru/catalog?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB", "https://apteka-ot-sklada.ru/catalog?q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD", "https://apteka-ot-sklada.ru/catalog?q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C", "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
pages = {}
prep = []
for i in range(len(linklist)):
    respone = requests.get(linklist[i])
    html = respone.text
    print(html)

    try:
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all("div", class_="ui-card ui-card_size_default goods-card goods-grid__cell goods-grid__cell_size_3")
        if not items:
            print("не туда")


        # берем данные с каждой карточки
        for item in items:
            prep.append(
                {
                'title': item.find("div", class_="goods-card__name text text_size_default text_weight_medium").find("span").text.strip(),
                'price': item.find("div", class_="goods-card__cost-area text").text.strip(),
                'link': linklist[i]
                }
            )
    except:
        print("нет")

print(prep)
with open(f"apteka-ot-sklada{date}.csv", 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
    for item in prep:
        writer.writerow([date, '', item['title'], name, item['link'], 'Пермь', item['price']])


#  выводит как надо по поиску 1 город
