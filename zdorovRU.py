import time
import requests
from bs4 import BeautifulSoup
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# НЕ РАБОТАЕТ

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")

URL = "https://zdorov.ru/"
HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
}
cookies = [
    {'name': "Москва и МО", 'cookies': {
        "storage-shipment": "%7B%22stockId%22%3A0%2C%22cityId%22%3A1%2C%22shipAddressId%22%3A0%2C%22shipAddressTitle%22%3A%22%22%2C%22stockTitle%22%3A%22%22%7D"}},
    {'name': "Нижний Новгород", 'cookies': {
        "storage-shipment": "%7B%22stockId%22%3A0%2C%22cityId%22%3A2%2C%22shipAddressId%22%3A0%2C%22shipAddressTitle%22%3A%22%22%2C%22stockTitle%22%3A%22%22%7D"}}
]

name = "ЗдоровРу"

linklist = ["https://zdorov.ru/catalog/search?q=%D0%90%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
            "https://zdorov.ru/catalog/search?q=%D0%90%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
            "https://zdorov.ru/catalog/search?q=%D0%90%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
            "https://zdorov.ru/catalog/search?q=%D0%93%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
            "https://zdorov.ru/catalog/search?q=%D0%93%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
            "https://zdorov.ru/catalog/search?q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
            "https://zdorov.ru/catalog/search?q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
            "https://zdorov.ru/catalog/search?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
            "https://zdorov.ru/catalog/search?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB",
            "https://zdorov.ru/catalog/search?q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
            "https://zdorov.ru/catalog/search?q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82+%D0%BB%D0%BE%D0%BD%D0%B3",
            "https://zdorov.ru/catalog/search?q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
            "https://zdorov.ru/catalog/search?q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
            "https://zdorov.ru/catalog/search?q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
            "https://zdorov.ru/catalog/search?q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
            "https://zdorov.ru/catalog/search?q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
            "https://zdorov.ru/catalog/search?q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82"]
pages = {}

for cookie in cookies:
    prep = []
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    for i in range(len(linklist)):
        try:
            chrome_driver_path = r'C:\Users\danil\OneDrive\Документы\Python\chromedriver.exe'
            s = Service('Chromedriver PATH')
            driver = webdriver.Chrome(service=s, options=options)
            time.sleep(3)
            driver.get(linklist[i])
            print(i)

            with open("seleniumPage.html", "w", encoding='utf-8') as file:
                file.write(driver.page_source)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()

        with open("seleniumPage.html", encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'html.parser')
        items = soup.find_all("div", class_="sc-bcb2baf5-0 cJRXlu")
        if not items:
            print("не туда")

        try:
            for item in items:
                prep.append(
                    {
                        'title': item.find("span",
                                           class_="Goodstyled__FullTitleSpan-sc-1vxg1b5-17").text.strip(),
                        'price': item.find("span",
                                           class_="GoodPriceItemstyled__PriceNumberActualBold-sc-1ofx8o5-2").text.strip(),
                        'link': linklist[i]
                    }
                )
        except:
            print("Нет в наличии")

    print(prep)
    with open(
            rf"C:\Users\danil\OneDrive\Документы\Python\Аптечка\Результаты парсинга\ZdorovRu_{date}.csv",
            'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(('Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки',
                         'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'))
        for item in prep:
            writer.writerow([date, '', item['title'], name, item['link'], cookie['name'], item['price']])