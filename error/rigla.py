import requests
from bs4 import BeautifulSoup
import csv
import datetime
from selenium import webdriver


URL = "https://www.rigla.ru/"
HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
}


now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")


name = "Ригла"


linklist = ["https://www.rigla.ru/search?q=%D0%B0%D0%B4%D0%B0%D0%BD%D1%82", "https://www.rigla.ru/search?q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD", "https://www.rigla.ru/search?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA", "https://www.rigla.ru/search?q=%D0%B0%D1%82%D1%80%D0%B8%20%D0%B8%D0%BD%D0%B6", "https://www.rigla.ru/search?q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE", "https://www.rigla.ru/search?q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA%20%D0%BE%D1%80%D1%82%D0%BE", "https://www.rigla.ru/search?q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82", "https://www.rigla.ru/search?q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD%20%D1%84%D0%BB%D1%8E%D0%B8%D0%B4", "https://www.rigla.ru/search?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81", "https://www.rigla.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD%20%D1%84%D0%B8%D0%B4%D0%B8%D1%8F", "https://www.rigla.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD", "https://www.rigla.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C%20%D0%B0%D1%80%D1%82%D1%80%D0%BE", "https://www.rigla.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC", "https://www.rigla.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC", "https://www.rigla.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81", "https://www.rigla.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE", "https://www.rigla.ru/search?q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82", "https://www.rigla.ru/search?q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD", "https://www.rigla.ru/search?q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD", "https://www.rigla.ru/search?q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82", "https://www.rigla.ru/search?q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD", "https://www.rigla.ru/search?q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD", "https://www.rigla.ru/search?q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82", "https://www.rigla.ru/search?q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD", "https://www.rigla.ru/search?q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD", "https://www.rigla.ru/search?q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB", "https://www.rigla.ru/search?q=%D0%BE%D1%81%D1%82%20%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD", "https://www.rigla.ru/search?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB", "https://www.rigla.ru/search?q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D0%B8%D0%BD%D1%82%D1%80%D0%B0", "https://www.rigla.ru/search?q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA", "https://www.rigla.ru/search?q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81", "https://www.rigla.ru/search?q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82", "https://www.rigla.ru/search?q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA", "https://www.rigla.ru/search?q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA", "https://www.rigla.ru/search?q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB", "https://www.rigla.ru/search?q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC", "https://www.rigla.ru/search?q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD", "https://www.rigla.ru/search?q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C", "https://www.rigla.ru/search?q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD", "https://www.rigla.ru/search?q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD", "https://www.rigla.ru/search?q=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81", "https://www.rigla.ru/search?q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD", "https://www.rigla.ru/search?q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0", "https://www.rigla.ru/search?q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81", "https://www.rigla.ru/search?q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81", "https://www.rigla.ru/search?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC", "https://www.rigla.ru/search?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD", "https://www.rigla.ru/search?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC%20%D0%B1%D1%83%D1%84%D1%83%D1%81", "https://www.rigla.ru/search?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC%20%D0%B4%D1%81", "https://www.rigla.ru/search?q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC", "https://www.rigla.ru/search?q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD", "https://www.rigla.ru/search?q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD", "https://www.rigla.ru/search?q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81", "https://www.rigla.ru/search?q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA", "https://www.rigla.ru/search?q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC", "https://www.rigla.ru/search?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC%20%D1%82%D0%B5%D0%B2%D0%B0", "https://www.rigla.ru/search?q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF", "https://www.rigla.ru/search?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4", "https://www.rigla.ru/search?q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF", "https://www.rigla.ru/search?q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82", "https://www.rigla.ru/search?q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD", "https://www.rigla.ru/search?q=%D0%B4%D0%BE%D0%BD%D0%B0", "https://www.rigla.ru/search?q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD", "https://www.rigla.ru/search?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD", "https://www.rigla.ru/search?q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD", "https://www.rigla.ru/search?q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5%20%D0%B1%D0%B8%D0%BE", "https://www.rigla.ru/search?q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4%20%D0%B0%D1%80%D1%82%D1%80%D0%BE", "https://www.rigla.ru/search?q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB", "https://www.rigla.ru/search?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0%20%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82", "https://www.rigla.ru/search?q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0", "https://www.rigla.ru/search?q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82", "https://www.rigla.ru/search?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82", "https://www.rigla.ru/search?q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80%20%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC", "https://www.rigla.ru/search?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4", "https://www.rigla.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80", "https://www.rigla.ru/search?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB", "https://www.rigla.ru/search?q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD", "https://www.rigla.ru/search?q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C", "https://www.rigla.ru/search?q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
pages = {}
prep = []


options = webdriver.FirefoxOptions()
options.set_preference("dom.webdriver.enabled", False)
options.headless = True


for i in range(len(linklist)):
    try:
        driver = webdriver.Firefox(options=options)
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
    items = soup.find_all("div", class_="product-list-mode-grid__item")
    if not items:
        print(items)


    # берем данные с каждой карточки
    try:
        for item in items:
            prep.append(
                {
                'title': item.find("a", class_="product__title").find(".//title").text.strip(),
                'price': item.find("div", class_="product__active-price").text.strip(),
                'link': linklist[i]
                }
            )
    except:
        print("Нет")

print(prep)
with open(f"Rigla{date}.csv", 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
    for item in prep:
        writer.writerow([date, '', item['title'], name, item['link'], '', item['price']])

#  Защищено хз чем