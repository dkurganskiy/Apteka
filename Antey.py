import requests
from bs4 import BeautifulSoup
import csv
import datetime

# РАБОТАЕТ КАК НАДО

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")

HOST = "https://aptekaantey.ru/"
URL = "https://aptekaantey.ru/kat/"
HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
}

name = "Антей"

linklist = ["https://aptekaantey.ru/kat/simptom/2979", "https://aptekaantey.ru/kat/simptom/130202",
            "https://aptekaantey.ru/kat/simptom/130074", "https://aptekaantey.ru/kat/simptom/130076",
            "https://aptekaantey.ru/kat/simptom/198928", "https://aptekaantey.ru/kat/simptom/117858",
            "https://aptekaantey.ru/kat/simptom/106209", "https://aptekaantey.ru/kat/simptom/8052",
            "https://aptekaantey.ru/kat/simptom/100472", "https://aptekaantey.ru/kat/simptom/107530",
            "https://aptekaantey.ru/kat/simptom/10381", "https://aptekaantey.ru/kat/simptom/26677",
            "https://aptekaantey.ru/kat/simptom/161191", "https://aptekaantey.ru/kat/simptom/76496",
            "https://aptekaantey.ru/kat/simptom/11415", "https://aptekaantey.ru/kat/simptom/34442",
            "https://aptekaantey.ru/kat/simptom/45554", "https://aptekaantey.ru/kat/simptom/160992",
            "https://aptekaantey.ru/kat/simptom/160210"]
pages = {}
prep = []
for i in range(len(linklist)):
    respone = requests.get(linklist[i])
    respone.encoding = 'windows-1251'
    html = respone.text
    print(i)

    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("body")
    if not items:
        print("не туда")

    try:
        for item in items:
            prep.append(
                {
                    'title': item.find("h1", style="padding-bottom:30px;").text.strip(),
                    'price': item.find("span", style="color:#054c8c; font-size: 40px;").text.strip(),
                    'link': linklist[i],
                    'city': item.find("div", class_="topr").find('a').text.strip()
                }
            )
    except:
        print("Нет в наличии")

print(prep)
with open \
        (rf"C:\Users\danil\OneDrive\Документы\Python\Аптечка\Результаты парсинга\Antey_{date}.csv", 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
         'Ссылка на препарат', 'Город', 'Цена'])
    for item in prep:
        writer.writerow([{date}, '', item['title'], name, item['link'], item['city'], item['price']])