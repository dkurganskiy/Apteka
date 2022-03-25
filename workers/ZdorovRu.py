import requests
from bs4 import BeautifulSoup
import csv
import datetime

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")


URL = "https://zdorov.ru/"
HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
}
cookies = [
    {'name': "Москва и МО", 'cookies': {"storage-shipment": "%7B%22stockId%22%3A0%2C%22cityId%22%3A1%2C%22shipAddressId%22%3A0%2C%22shipAddressTitle%22%3A%22%22%2C%22stockTitle%22%3A%22%22%7D"}},
    {'name': "Нижний Новгород", 'cookies': {"storage-shipment": "%7B%22stockId%22%3A0%2C%22cityId%22%3A2%2C%22shipAddressId%22%3A0%2C%22shipAddressTitle%22%3A%22%22%2C%22stockTitle%22%3A%22%22%7D"}}
]


name = "ЗдоровРу"


linklist = ["https://zdorov.ru/catalog/344/390/1690/ameloteks-38636",
            "https://zdorov.ru/catalog/344/470/473/armaviskon-104353",
            "https://zdorov.ru/catalog/344/470/473/armaviskon-104352",
            "https://zdorov.ru/catalog/344/470/473/armaviskon-forte-105447",
            "https://zdorov.ru/catalog/344/470/473/armaviskon-hondro-127921",
            "https://zdorov.ru/catalog/344/470/1683/artogistan-103746",
            "https://zdorov.ru/catalog/344/470/1683/artogistan-103746",
            "https://zdorov.ru/catalog/344/470/473/gialripayer-10-hondroreparant-89683",
            "https://zdorov.ru/catalog/344/470/473/gialurom-60845",
            "https://zdorov.ru/catalog/344/470/473/gialurom-cs-88711",
            "https://zdorov.ru/catalog/344/470/473/dyuralan-implantant-vyazkouprugiy-sterilnyy-96075",
            "https://zdorov.ru/catalog/344/470/473/inektran-102818",
            "https://zdorov.ru/catalog/344/390/1319/meloksikam-akrihin-105829",
            "https://zdorov.ru/catalog/344/390/1319/meloksikam-akrihin-105829",
            "https://zdorov.ru/catalog/344/470/473/osteokoll-implantat-kollagen-soderzhashiy-126635",
            "https://zdorov.ru/catalog/344/470/473/pleksatron-implantat-kollagen-soder-126634",
            "https://zdorov.ru/catalog/344/470/473/ripart-long-109031",
            "https://zdorov.ru/catalog/344/470/473/ripart-long-104413",
            "https://zdorov.ru/catalog/344/470/473/ripart-forte-125206",
            "https://zdorov.ru/catalog/344/470/1683/rumalon-1ml-10-91537",
            "https://zdorov.ru/catalog/344/390/1690/traumel-s-14214",
            "https://zdorov.ru/catalog/344/470/473/fermatron-33451",
            "https://zdorov.ru/catalog/344/470/473/fermatron-plyus-48385",
            "https://zdorov.ru/catalog/344/470/473/fermatron-s-49485",
            "https://zdorov.ru/catalog/344/470/473/fleksotron-kross-108327",
            "https://zdorov.ru/catalog/344/470/473/fleksotron-solo-implantat-126156",
            "https://zdorov.ru/catalog/344/470/473/fleksotron-ultra-implantat-126160",
            "https://zdorov.ru/catalog/344/470/473/fermatron-33451",
            "https://zdorov.ru/catalog/344/470/473/hialubriks-91163",
            "https://zdorov.ru/catalog/344/470/473/intradzhekt-109397"]
pages = {}


for cookie in cookies:
    prep = []
    for i in range(len(linklist)):
        respone = requests.get(linklist[i], cookies=cookie["cookies"])
        html = respone.text
        print(i)

        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all("div", class_="Goodstyled__Container-sc-1vxg1b5-0")
        if not items:
            print("не туда")

        try:
            for item in items:
                prep.append(
                    {
                    'title': item.find("span", class_="Goodstyled__FullTitleSpan-sc-1vxg1b5-17").text.strip(),
                    'price': item.find("span", class_="GoodPriceItemstyled__PriceNumberActualBold-sc-1ofx8o5-2").text.strip(),
                    'link': linklist[i]
                    }
                )
        except:
            print("Нет в наличии")

    print(prep)
    with open(f"ZdorovRu_{date}.csv", 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(('Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'))
        for item in prep:
            writer.writerow([date, '', item['title'], name, item['link'], cookie['name'], item['price']])


#   как надо
