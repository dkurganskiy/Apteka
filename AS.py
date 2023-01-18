import time
import requests
from bs4 import BeautifulSoup
import csv
import datetime
from selenium import webdriver
import schedule

def job():
    try:
        class threeSixSix(object):
            URL = "https://366.ru/"
            HEADERS = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
            }

            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            name = "36 и 6"

            linklist = ["https://366.ru/search/?text=%D0%B0%D0%B4%D0%B0%D0%BD%D1%82",
                        "https://366.ru/search/?text=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
                        "https://366.ru/search/?text=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://366.ru/search/?text=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6",
                        "https://366.ru/search/?text=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://366.ru/search/?text=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE",
                        "https://366.ru/search/?text=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82",
                        "https://366.ru/search/?text=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4",
                        "https://366.ru/search/?text=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
                        "https://366.ru/search/?text=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB",
                        "https://366.ru/search/?text=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F",
                        "https://366.ru/search/?text=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://366.ru/search/?text=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://366.ru/search/?text=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
                        "https://366.ru/search/?text=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C",
                        "https://366.ru/search/?text=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
                        "https://366.ru/search/?text=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
                        "https://366.ru/search/?text=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
                        "https://366.ru/search/?text=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
                        "https://366.ru/search/?text=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
                        "https://366.ru/search/?text=%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
                        "https://366.ru/search/?text=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                        "https://366.ru/search/?text=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
                        "https://366.ru/search/?text=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://366.ru/search/?text=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
                        "https://366.ru/search/?text=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
                        "https://366.ru/search/?text=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
                        "https://366.ru/search/?text=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD",
                        "https://366.ru/search/?text=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB",
                        "https://366.ru/search/?text=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
                        "https://366.ru/search/?text=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://366.ru/search/?text=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
                        "https://366.ru/search/?text=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
                        "https://366.ru/search/?text=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://366.ru/search/?text=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
                        "https://366.ru/search/?text=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
                        "https://366.ru/search/?text=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC",
                        "https://366.ru/search/?text=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
                        "https://366.ru/search/?text=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
                        "https://366.ru/search/?text=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://366.ru/search/?text=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://366.ru/search/?text=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
                        "https://366.ru/search/?text=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
                        "https://366.ru/search/?text=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://366.ru/search/?text=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
                        "https://366.ru/search/?text=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
                        "https://366.ru/search/?text=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
                        "https://366.ru/search/?text=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://366.ru/search/?text=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
                        "https://366.ru/search/?text=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC",
                        "https://366.ru/search/?text=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD",
                        "https://366.ru/search/?text=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
                        "https://366.ru/search/?text=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81",
                        "https://366.ru/search/?text=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA",
                        "https://366.ru/search/?text=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://366.ru/search/?text=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF",
                        "https://366.ru/search/?text=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
                        "https://366.ru/search/?text=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
                        "https://366.ru/search/?text=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
                        "https://366.ru/search/?text=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://366.ru/search/?text=%D0%B4%D0%BE%D0%BD%D0%B0",
                        "https://366.ru/search/?text=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
                        "https://366.ru/search/?text=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
                        "https://366.ru/search/?text=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
                        "https://366.ru/search/?text=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE",
                        "https://366.ru/search/?text=%D1%81%D1%83%D1%82%D1%80%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://366.ru/search/?text=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB",
                        "https://366.ru/search/?text=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82",
                        "https://366.ru/search/?text=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
                        "https://366.ru/search/?text=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
                        "https://366.ru/search/?text=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://366.ru/search/?text=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
                        "https://366.ru/search/?text=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
                        "https://366.ru/search/?text=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
                        "https://366.ru/search/?text=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                        "https://366.ru/search/?text=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://366.ru/search/?text=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
                        "https://366.ru/search/?text=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
            pages = {}
            prep = []

            options = webdriver.FirefoxOptions()
            options.set_preference("dom.webdriver.enabled", False)
            options.headless = True

            for i in range(len(linklist)):
                try:
                    driver = webdriver.Firefox(executable_path=r"C:\Users\Danil\Desktop\Python\Apteka\workers\geckodriver")
                    time.sleep(15)
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
                items = soup.find_all("div", class_="listing_product")
                if not items:
                    print("не туда")

                # берем данные с каждой карточки
                try:
                    for item in items:
                        prep.append(
                            {
                                'title': item.find("a", class_="listing_product__title").text.strip(),
                                'price': item.find("div", class_="listing_product__price").find("span").text.strip(),
                                'link': linklist[i]
                            }
                        )
                except:
                    print("Нет")

            print(prep)
            with open(rf"C:\Users\danil\OneDrive\Документы\Python\Аптечка\36&6_{date}.csv", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки',
                     'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'], name, item['link'], 'Москва', item['price']])
    except:
        print("error 36.6")


    try:
        class antey(object):
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
                print(html)

                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all("body")
                if not items:
                    print("не туда")

                try:
                    for item in items:
                        prep.append(
                            {
                                'title': item.find("h1", style="padding-bottom:30px;").text.strip(),
                                'price': item.find("span").text.strip(),
                                'link': linklist[i],
                                'city': item.find("div", class_="topr").find('a').text.strip()
                            }
                        )
                except:
                    print("Нет в наличии")

            print(prep)
            with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\Antey_{date}.csv", 'w', newline='', encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([{date}, '', item['title'], name, item['link'], item['city'], item['price']])
    except:
        print("error Antey")


    try:
        class aprilSelenium(object):
            # Дата прогона скрипта
            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            # Имя аптечной сети
            name = "Апрель"

            # Список ссылок на препараты
            linklist = ["https://apteka-april.ru/search/%D0%B0%D0%B4%D0%B0%D0%BD%D1%82",
                        "https://apteka-april.ru/search/%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
                        "https://apteka-april.ru/search/%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://apteka-april.ru/search/%D0%B0%D1%82%D1%80%D0%B8%20%D0%B8%D0%BD%D0%B6",
                        "https://apteka-april.ru/search/%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://apteka-april.ru/search/%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA%20%D0%BE%D1%80%D1%82%D0%BE",
                        "https://apteka-april.ru/search/%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82",
                        "https://apteka-april.ru/search/%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD%20%D1%84%D0%BB%D1%8E%D0%B8%D0%B4",
                        "https://apteka-april.ru/search/%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
                        "https://apteka-april.ru/search/%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB",
                        "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD%20%D1%84%D0%B8%D0%B4%D0%B8%D1%8F",
                        "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C%20%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
                        "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC%20%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C",
                        "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
                        "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
                        "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
                        "https://apteka-april.ru/search/%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
                        "https://apteka-april.ru/search/%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
                        "https://apteka-april.ru/search/%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
                        "https://apteka-april.ru/search/%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                        "https://apteka-april.ru/search/%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
                        "https://apteka-april.ru/search/%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://apteka-april.ru/search/%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
                        "https://apteka-april.ru/search/%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
                        "https://apteka-april.ru/search/%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
                        "https://apteka-april.ru/search/%D0%BE%D1%81%D1%82%20%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD",
                        "https://apteka-april.ru/search/%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB",
                        "https://apteka-april.ru/search/%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
                        "https://apteka-april.ru/search/%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://apteka-april.ru/search/%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
                        "https://apteka-april.ru/search/%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
                        "https://apteka-april.ru/search/%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://apteka-april.ru/search/%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
                        "https://apteka-april.ru/search/%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
                        "https://apteka-april.ru/search/%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC",
                        "https://apteka-april.ru/search/%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
                        "https://apteka-april.ru/search/%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
                        "https://apteka-april.ru/search/%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://apteka-april.ru/search/%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://apteka-april.ru/search/%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
                        "https://apteka-april.ru/search/%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
                        "https://apteka-april.ru/search/%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://apteka-april.ru/search/%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
                        "https://apteka-april.ru/search/%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
                        "https://apteka-april.ru/search/%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
                        "https://apteka-april.ru/search/%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://apteka-april.ru/search/%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
                        "https://apteka-april.ru/search/%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC",
                        "https://apteka-april.ru/search/%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD",
                        "https://apteka-april.ru/search/%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
                        "https://apteka-april.ru/search/%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
                        "https://apteka-april.ru/search/%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA",
                        "https://apteka-april.ru/search/%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://apteka-april.ru/search/%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC%20%D1%82%D0%B5%D0%B2%D0%B0",
                        "https://apteka-april.ru/search/%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF",
                        "https://apteka-april.ru/search/%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
                        "https://apteka-april.ru/search/%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
                        "https://apteka-april.ru/search/%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
                        "https://apteka-april.ru/search/%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://apteka-april.ru/search/%D0%B4%D0%BE%D0%BD%D0%B0",
                        "https://apteka-april.ru/search/%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
                        "https://apteka-april.ru/search/%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
                        "https://apteka-april.ru/search/%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
                        "https://apteka-april.ru/search/%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5%20%D0%B1%D0%B8%D0%BE",
                        "https://apteka-april.ru/search/%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4%20%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://apteka-april.ru/search/%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB",
                        "https://apteka-april.ru/search/%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0%20%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82",
                        "https://apteka-april.ru/search/%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
                        "https://apteka-april.ru/search/%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
                        "https://apteka-april.ru/search/%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://apteka-april.ru/search/%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80%20%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
                        "https://apteka-april.ru/search/%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
                        "https://apteka-april.ru/search/%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
                        "https://apteka-april.ru/search/%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                        "https://apteka-april.ru/search/%D0%BF%D1%80%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://apteka-april.ru/search/%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
                        "https://apteka-april.ru/search/%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
            pages = {}
            prep = []

            options = webdriver.FirefoxOptions()
            options.set_preference("dom.webdriver.enabled", False)
            options.headless = True

            for i in range(len(linklist)):
                try:
                    driver = webdriver.Firefox(executable_path=r"C:\Users\Danil\Desktop\Python\Apteka\workers\geckodriver")
                    driver.get(linklist[i])
                    print(i)
                    time.sleep(15)
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
                items = soup.find_all("div", class_="c-product-card")
                if not items:
                    print("не туда")

                # берем данные с каждой карточки
                try:
                    for item in items:
                        prep.append(
                            {
                                'title': item.find("span", itemprop="name").text.strip(),
                                'price': item.find("div", itemprop="price").text.strip(),
                                'link': linklist[i]
                            }
                        )
                except:
                    print("Нет")

                with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\april{date}.csv", 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow(
                        ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки',
                         'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
                    for item in prep:
                        writer.writerow([date, '', item['title'], name, item['link'], 'Москва', item['price']])
    except:
        print("error April")

    try:
        class aptekaOtSklada(object):
            HOST = "https://planetazdorovo.ru/"
            URL = "https://planetazdorovo.ru/catalog/"
            HEADERS = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
            }

            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            name = "Аптека от склада"

            linklist = [
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%82%D1%80%D0%B8%20%D0%B8%D0%BD%D0%B6",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA%20%D0%BE%D1%80%D1%82%D0%BE",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD%20%D1%84%D0%B8%D0%B4%D0%B8%D1%8F",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C%20%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC%20%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B8%D0%B0%D0%BB%D1%8C",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%9E%D0%A1%D0%A2%20%D0%A2%D0%95%D0%9D%D0%94%D0%9E%D0%9D",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D1%80%D0%BE%D0%BB",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D0%BB%D1%84%D1%83%D1%82%D0%BE%D0%BF",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B4%D0%BE%D0%BD%D0%B0",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%80",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                "https://apteka-ot-sklada.ru/catalog?q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
                "https://apteka-ot-sklada.ru/catalog?q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
            pages = {}
            prep = []
            for i in range(len(linklist)):
                respone = requests.get(linklist[i])
                html = respone.text
                print(html)

                try:
                    soup = BeautifulSoup(html, 'html.parser')
                    items = soup.find_all("div",
                                          class_="ui-card ui-card_size_default goods-card goods-grid__cell goods-grid__cell_size_3")
                    if not items:
                        print("не туда")

                    # берем данные с каждой карточки
                    for item in items:
                        prep.append(
                            {
                                'title': item.find("div",
                                                   class_="goods-card__name text text_size_default text_weight_medium").find(
                                    "span").text.strip(),
                                'price': item.find("div", class_="goods-card__cost-area text").text.strip(),
                                'link': linklist[i]
                            }
                        )
                except:
                    print("нет")

            print(prep)
            with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\apteka-ot-sklada{date}.csv", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'], name, item['link'], 'Пермь', item['price']])
    except:
        print("error AptekaOtSklada")

    try:
        class aptekaRu(object):
            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            HOST = "https://apteka.ru/"
            URL = "https://apteka.ru/product/"
            HEADERS = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
            }

            name = "АптекаРу"

            linklist = ["https://apteka.ru/search/?q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
                        "https://apteka.ru/product/armaviskon-sredstvo-dlya-vnutrisustavnogo-vvedeniya-1-2ml-n1-shpricz-5e326545f5a9ae0001406b1b/",
                        "https://apteka.ru/product/armaviskon-plyus-sredstvo-dlya-vnutrisustavnogo-vvedeniya-15-2ml-n1-shpricz-5e32647dca7bdc000192b092/",
                        "https://apteka.ru/product/armaviskon-forte-sredstvo-dlya-vnutrisustavnogo-vvedeniya-23-3ml-n1-shpricz-5e3267c165b5ab0001650e1b/",
                        "https://apteka.ru/product/armaviskon-xondro-protez-sinovialnoj-zhidkosti-3ml-n1-shpricz-610aa73f010f1c2949d0201e/",
                        "https://apteka.ru/product/gialripajer-10-xondroreparant-5ml-flakon-5e32680dca7bdc000192cae3/",
                        "https://apteka.ru/product/gialurom-15-2ml-n1-shpricz-r-r-vsustav-5e3263d765b5ab000164f15b/",
                        "https://apteka.ru/product/gialurom-cs-protez-sin-zhidk-0063ml0093ml-n1shpr-5e327152ca7bdc00019313f9/",
                        "https://apteka.ru/product/dyuralan-0063ml-implantat-vyazkouprug-n1-shpricz-5e327845f5a9ae0001410081/?q=%D0%94%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                        "https://apteka.ru/product/inektran-01ml-2ml-n10-amp-r-r-vm-5e3276c5f5a9ae000140f182/?q=%D0%98%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
                        "https://apteka.ru/product/meloksikam-001ml-15ml-n3-amp-r-r-vmfkp-kurskaya-biofabrika-5fa11acb7c9fdd0001c3faf3/",
                        "https://apteka.ru/product/mukosat-01ml-1ml-n10-amp-r-r-vm-vsustavn-5e327261f5a9ae000140cfc3/",
                        "https://apteka.ru/product/osteokoll-osteocoll-implantat-kollagen-soderzhashhij-dlya-periartikulyarnogo-vved-2ml-n5-flak-5fe1b9314d2c6918dc435fc4/?q=%D0%9E%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                        "https://apteka.ru/product/osteokoll-osteocoll-implantat-kollagen-soderzhashhij-dlya-periartikulyarnogo-vved-2ml-n5-flak-5fe1b9314d2c6918dc435fc4/?q=%D0%9E%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                        "https://apteka.ru/product/osteokoll-osteocoll-implantat-kollagen-soderzhashhij-dlya-periartikulyarnogo-vved-2ml-n5-flak-5fe1b9314d2c6918dc435fc4/?q=%D0%9E%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                        "https://apteka.ru/product/ripart-long-sredstvo-dlya-zameshheniya-sinovialnoj-zhidkosti-3ml-n1-shpricz-5e32643a65b5ab000164f43a/",
                        "https://apteka.ru/product/ripart-forte-sredstvo-dlya-zameshheniya-sinovialnoj-zhidkosti-3ml-n1-shpricz-5fbf90cdc894b90001bf7f61/?q=%D0%A0%D0%B8%D0%BF%D0%B0%D1%80%D1%82%20%D1%84%D0%BE%D1%80%D1%82%D0%B5",
                        "https://apteka.ru/product/ripart-forte-sredstvo-dlya-zameshheniya-sinovialnoj-zhidkosti-3ml-n1-shpricz-5fbf90cdc894b90001bf7f61/?q=%D0%A0%D0%B8%D0%BF%D0%B0%D1%80%D1%82%20%D1%84%D0%BE%D1%80%D1%82%D0%B5",
                        "https://apteka.ru/product/traumel-s-22ml-n5-amp-r-r-vm-okolosustav-gomeopat-5e32683765b5ab00016511d2/",
                        "https://apteka.ru/product/fermatron-protez-sinovialnoj-zhidk-1-2ml-n1-shpricz-5e326aca65b5ab000165261b/",
                        "https://apteka.ru/product/fermatron-plyus-protez-sinov-zhidk-15-0032mln1shp-5e32772b65b5ab00016584bc/",
                        "https://apteka.ru/product/fleksotron-kross-implantant-dlya-vnutrisustavnyx-inekczij-na-osnove-perekrestno-sshitogo-gialuronata-natriya-60mg30ml-3ml-n1-shpricz-5e327419ca7bdc0001932400/",
                        "https://apteka.ru/product/fleksotron-solo-implantant-vyazkoelastichnyj-ster-dlya-vnutrisustavnoj-inekczii-gialuronat-natriya-22-22mgml-2ml-n1-shpricz-60100a99fb1788f83e2268a6/",
                        "https://apteka.ru/product/fleksotron-ultra-implantant-vyazkoelastichnyj-ster-dlya-vnutrisustavnoj-inekczii-gialuronat-natriya-25-25mgml-48ml-n1-shpricz-60100b19fd63dd365e6a55d1/",
                        "https://apteka.ru/product/xronotron-implantant-inekczionnyj-v-vide-gelya-na-osnove-polinukleotidov-dlya-vnutrisustavnogo-vvedeniya-20mgml-2ml-n1-shpricz-5e9d611282197f00010ed7e7/?q=%D0%A5%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://apteka.ru/product/xialubriks-30mg2ml-r-r--dvnutrisust-vved-n1-5e32717cca7bdc0001931541/?suggestion=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&q=%D0%A5%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
                        "https://apteka.ru/product/intradzhekt-sredstvo-dlya-zameshheniya-sinovialnoj-zhidkosti-18-2ml-n1-shpricz-604b3469d07d75eed705f6ae/?q=%D0%98%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82"]
            pages = {}
            prep = []
            for i in range(len(linklist)):
                respone = requests.get(linklist[i])
                html = respone.text
                print(html)

                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all("div", class_="body")
                if not items:
                    print("не туда")

                try:
                    for item in items:
                        prep.append(
                            {
                                'title': item.find("h1", itemprop="name").text.strip(),
                                'price': item.find("span", class_="moneyprice__content").text.strip(),
                                'link': linklist[i]
                            }
                        )
                except:
                    print("Нет в наличии")

            print(prep)
            with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\AptekaRu_{date}.csv", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'], name, item['link'], 'Москва', item['price']])
    except:
        print("error AptekaRu")

    # try:
    #     class farmaimpeks(object):
    #         URL = "https://b-apteka.ru/"
    #
    #         now = datetime.datetime.now()
    #         date = now.strftime("%d-%m-%Y")
    #
    #         name = "Фармаимпекс"
    #
    #         linklist = ["https://b-apteka.ru/search?q=%D0%B0%D0%B4%D0%B0%D0%BD%D1%82",
    #                     "https://b-apteka.ru/search?q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
    #                     "https://b-apteka.ru/search?q=%D0%B0%D1%82%D1%80%D0%B8%20%D0%B8%D0%BD%D0%B6",
    #                     "https://b-apteka.ru/search?q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
    #                     "https://b-apteka.ru/search?q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA%20%D0%BE%D1%80%D1%82%D0%BE",
    #                     "https://b-apteka.ru/search?q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82",
    #                     "https://b-apteka.ru/search?q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD%20%D1%84%D0%BB%D1%8E%D0%B8%D0%B4",
    #                     "https://b-apteka.ru/search?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
    #                     "https://b-apteka.ru/search?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB",
    #                     "https://b-apteka.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD%20%D1%84%D0%B8%D0%B4%D0%B8%D1%8F",
    #                     "https://b-apteka.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C%20%D0%B0%D1%80%D1%82%D1%80%D0%BE",
    #                     "https://b-apteka.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
    #                     "https://b-apteka.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC%20%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B8%D0%B0%D0%BB%D1%8C",
    #                     "https://b-apteka.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
    #                     "https://b-apteka.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
    #                     "https://b-apteka.ru/search?q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
    #                     "https://b-apteka.ru/search?q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
    #                     "https://b-apteka.ru/search?q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
    #                     "https://b-apteka.ru/search?q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
    #                     "https://b-apteka.ru/search?q=%D0%BE%D1%81%D1%82%20%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BB",
    #                     "https://b-apteka.ru/search?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB",
    #                     "https://b-apteka.ru/search?q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
    #                     "https://b-apteka.ru/search?q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
    #                     "https://b-apteka.ru/search?q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
    #                     "https://b-apteka.ru/search?q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
    #                     "https://b-apteka.ru/search?q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
    #                     "https://b-apteka.ru/search?q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
    #                     "https://b-apteka.ru/search?q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
    #                     "https://b-apteka.ru/search?q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC",
    #                     "https://b-apteka.ru/search?q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
    #                     "https://b-apteka.ru/search?q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
    #                     "https://b-apteka.ru/search?q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
    #                     "https://b-apteka.ru/search?q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
    #                     "https://b-apteka.ru/search?q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
    #                     "https://b-apteka.ru/search?q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
    #                     "https://b-apteka.ru/search?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
    #                     "https://b-apteka.ru/search?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA",
    #                     "https://b-apteka.ru/search?q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
    #                     "https://b-apteka.ru/search?q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF",
    #                     "https://b-apteka.ru/search?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
    #                     "https://b-apteka.ru/search?q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
    #                     "https://b-apteka.ru/search?q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
    #                     "https://b-apteka.ru/search?q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%B4%D0%BE%D0%BD%D0%B0",
    #                     "https://b-apteka.ru/search?q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5%20%D0%B1%D0%B8%D0%BE",
    #                     "https://b-apteka.ru/search?q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4%20%D0%B0%D1%80%D1%82%D1%80%D0%BE",
    #                     "https://b-apteka.ru/search?q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB",
    #                     "https://b-apteka.ru/search?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0%20%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82",
    #                     "https://b-apteka.ru/search?q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
    #                     "https://b-apteka.ru/search?q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
    #                     "https://b-apteka.ru/search?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
    #                     "https://b-apteka.ru/search?q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80%20%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
    #                     "https://b-apteka.ru/search?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
    #                     "https://b-apteka.ru/search?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
    #                     "https://b-apteka.ru/search?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
    #                     "https://b-apteka.ru/search?q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
    #                     "https://b-apteka.ru/search?q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
    #                     "https://b-apteka.ru/search?q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
    #         pages = {}
    #         prep = []
    #
    #         options = webdriver.FirefoxOptions()
    #         options.set_preference("dom.webdriver.enabled", False)
    #         options.headless = True
    #
    #         for i in range(len(linklist)):
    #             try:
    #                 driver = webdriver.Firefox(executable_path=r"C:\Users\Danil\Desktop\Python\Apteka\workers\geckodriver")
    #                 time.sleep(15)
    #                 driver.get(linklist[i])
    #                 print(i)
    #
    #                 with open("seleniumPage.html", "w",  encoding='utf-8') as file:
    #                     file.write(driver.page_source)
    #             except Exception as ex:
    #                 print(ex)
    #             finally:
    #                 driver.close()
    #                 driver.quit()
    #
    #             with open("seleniumPage.html",  encoding='utf-8') as file:
    #                 src = file.read()
    #
    #             soup = BeautifulSoup(src, 'html.parser')
    #             items = soup.find_all("div", class_="search-card__content-area")
    #             if not items:
    #                 print("не туда")
    #
    #             # берем данные с каждой карточки
    #             try:
    #                 for item in items:
    #                     prep.append(
    #                         {
    #                             'title': item.find("div", class_="header-card-search").text.strip(),
    #                             'price': item.find("div", class_="price-search__present").text.strip(),
    #                             'link': linklist[i]
    #                         }
    #                     )
    #             except:
    #                 print("Нет")
    #
    #         print(prep)
    #         with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\farmaimpeks{date}.csv", 'w', newline='',  encoding='utf-8') as file:
    #             writer = csv.writer(file, delimiter=';')
    #             writer.writerow(
    #                 ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
    #                  'Ссылка на препарат', 'Город', 'Цена'])
    #             for item in prep:
    #                 writer.writerow([date, '', item['title'], name, item['link'], 'Ижевск', item['price']])
    # except:
    #     print("error farmaimpeks")

    try:
        class farmakopeika(object):
            URL = "https://farmakopeika.ru/"
            HEADERS = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
            }

            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            name = "Фармакопейка"

            linklist = ["https://farmakopeika.ru/search?query=%D0%B0%D0%B4%D0%B0%D0%BD%D1%82",
                        "https://farmakopeika.ru/search?query=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://farmakopeika.ru/search?query=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6",
                        "https://farmakopeika.ru/search?query=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://farmakopeika.ru/search?query=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE",
                        "https://farmakopeika.ru/search?query=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82",
                        "https://farmakopeika.ru/search?query=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4",
                        "https://farmakopeika.ru/search?query=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
                        "https://farmakopeika.ru/search?query=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB",
                        "https://farmakopeika.ru/search?query=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F",
                        "https://farmakopeika.ru/search?query=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://farmakopeika.ru/search?query=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
                        "https://farmakopeika.ru/search?query=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C",
                        "https://farmakopeika.ru/search?query=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
                        "https://farmakopeika.ru/search?query=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
                        "https://farmakopeika.ru/search?query=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
                        "https://farmakopeika.ru/search?query=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
                        "https://farmakopeika.ru/search?query=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://farmakopeika.ru/search?query=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
                        "https://farmakopeika.ru/search?query=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB",
                        "https://farmakopeika.ru/search?query=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
                        "https://farmakopeika.ru/search?query=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://farmakopeika.ru/search?query=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
                        "https://farmakopeika.ru/search?query=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
                        "https://farmakopeika.ru/search?query=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://farmakopeika.ru/search?query=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
                        "https://farmakopeika.ru/search?query=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
                        "https://farmakopeika.ru/search?query=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC",
                        "https://farmakopeika.ru/search?query=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
                        "https://farmakopeika.ru/search?query=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
                        "https://farmakopeika.ru/search?query=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://farmakopeika.ru/search?query=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://farmakopeika.ru/search?query=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
                        "https://farmakopeika.ru/search?query=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
                        "https://farmakopeika.ru/search?query=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://farmakopeika.ru/search?query=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
                        "https://farmakopeika.ru/search?query=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
                        "https://farmakopeika.ru/search?query=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
                        "https://farmakopeika.ru/search?query=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://farmakopeika.ru/search?query=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC+%D0%B1%D1%83%D1%84%D1%83%D1%81",
                        "https://farmakopeika.ru/search?query=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC",
                        "https://farmakopeika.ru/search?query=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
                        "https://farmakopeika.ru/search?query=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA",
                        "https://farmakopeika.ru/search?query=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://farmakopeika.ru/search?query=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF",
                        "https://farmakopeika.ru/search?query=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
                        "https://farmakopeika.ru/search?query=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
                        "https://farmakopeika.ru/search?query=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
                        "https://farmakopeika.ru/search?query=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%B4%D0%BE%D0%BD%D0%B0",
                        "https://farmakopeika.ru/search?query=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
                        "https://farmakopeika.ru/search?query=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
                        "https://farmakopeika.ru/search?query=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE",
                        "https://farmakopeika.ru/search?query=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://farmakopeika.ru/search?query=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB",
                        "https://farmakopeika.ru/search?query=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82",
                        "https://farmakopeika.ru/search?query=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
                        "https://farmakopeika.ru/search?query=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
                        "https://farmakopeika.ru/search?query=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://farmakopeika.ru/search?query=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
                        "https://farmakopeika.ru/search?query=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
                        "https://farmakopeika.ru/search?query=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
                        "https://farmakopeika.ru/search?query=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                        "https://farmakopeika.ru/search?query=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://farmakopeika.ru/search?query=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
                        "https://farmakopeika.ru/search?query=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
            pages = {}
            prep = []
            for i in range(len(linklist)):
                respone = requests.get(linklist[i])
                html = respone.text
                print(i)

                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all("div", class_="product product_grid")
                if not items:
                    print("не туда")

                # берем данные с каждой карточки
                try:
                    for item in items:
                        prep.append(
                            {
                                'title': item.find("div", class_="product__title").text.strip(),
                                'price': item.find("div", class_="product__price").find("span").text.strip(),
                                'link': linklist[i]
                            }
                        )
                except:
                    print("Нет")

            print(prep)
            with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\farmakopeika_{date}.csv", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'], name, item['link'], 'Омск', item['price']])
    except:
        print("error farmakopeika")

    # try:
    #     class gubernskieApteki(object):
    #         now = datetime.datetime.now()
    #         date = now.strftime("%d-%m-%Y")
    #
    #         URL = "https://24farmacia.ru/"
    #         HEADERS = {
    #             "Accept": "*/*",
    #             "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
    #         }
    #
    #         name = "Губернские аптеки"
    #
    #         linklist = ["https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D0%25B4%25D0%25B0%25D0%25BD%25D1%2582",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D0%25BC%25D0%25B0%25D0%25B2%25D0%25B8%25D1%2581%25D0%25BA%25D0%25BE%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B8%25D1%2581%25D0%25BA",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2582%25D1%2580%25D0%25B8%2520%25D0%25B8%25D0%25BD%25D0%25B6",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B1%25D0%25B5%25D0%25BB%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B1%25D0%25B8%25D0%25BE%25D0%25B2%25D0%25B8%25D1%2581%25D0%25BA%2520%25D0%25BE%25D1%2580%25D1%2582%25D0%25BE",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B1%25D0%25B8%25D0%25BE%25D0%25BF%25D0%25BE%25D1%2580%25D1%2582",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B2%25D0%25B5%25D1%2580%25D1%2581%25D0%25B0%25D0%25BD%2520%25D1%2584%25D0%25BB%25D1%258E%25D0%25B8%25D0%25B4",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B2%25D0%25B8%25D1%2581%25D0%25BA%25D0%25BE%25D0%25BF%25D0%25BB%25D1%258E%25D1%2581",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D0%25B3%25D0%25B0%25D0%25BD%2520%25D1%2584%25D0%25B8%25D0%25B4%25D0%25B8%25D1%258F",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D0%25BE%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D1%2583%25D0%25B0%25D0%25BB%25D1%258C%2520%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D1%2583%25D1%2580%25D0%25BE%25D0%25BC",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D1%2583%25D1%2584%25D0%25BE%25D1%2580%25D0%25BC%2520%25D1%2581%25D0%25B8%25D0%25BD%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BB%25D1%258C",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D1%258E%25D0%25BA%25D1%2581",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BF%25D1%2580%25D0%25BE",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D1%2581%25D1%2582%25D0%25B0%25D1%2582",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D1%2580%25D1%2583%25D0%25B0%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25BE%25D1%2583-%25D0%25BE%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B4%25D0%25B8%25D0%25B0%25D1%2580%25D1%2582",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B4%25D1%258C%25D1%258E%25D1%2580%25D0%25B0%25D0%25BB%25D0%25B0%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B6%25D0%25B0%25D0%25BB%25D0%25B8%25D1%2580%25D0%25B5%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B8%25D0%25BD%25D1%2582%25D1%2580%25D0%25B0%25D0%25B4%25D0%25B6%25D0%25B5%25D0%25BA%25D1%2582",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B8%25D0%25BD%25D1%2582%25D1%2580%25D0%25B0%25D0%25B4%25D0%25B6%25D0%25B5%25D0%25BA%25D1%2582",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BA%25D1%2580%25D0%25B5%25D1%2581%25D0%25BF%25D0%25B8%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BD%25D0%25BE%25D0%25BB%25D1%2582%25D1%2580%25D0%25B5%25D0%25BA%25D1%2581%25D0%25B8%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BE%25D1%2580%25D1%2582%25D0%25BE%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BE%25D1%2581%25D1%2582%2520%25D1%2582%25D0%25B5%25D0%25BD%25D0%25B4%25D0%25BE%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BE%25D1%2581%25D1%2582%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25BB",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BF%25D1%2580%25D0%25BE%25D1%2584%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2581%2520%25D0%25B8%25D0%25BD%25D1%2582%25D1%2580%25D0%25B0",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2580%25D0%25B5%25D0%25B2%25D0%25B8%25D1%2581%25D0%25BA",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2580%25D0%25B5%25D0%25BD%25D0%25B5%25D1%2585%25D0%25B0%25D0%25B2%25D0%25B8%25D1%2581",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2580%25D0%25B8%25D0%25BF%25D0%25B0%25D1%2580%25D1%2582",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2580%25D1%2583%25D1%2581%25D0%25B2%25D0%25B8%25D1%2581%25D0%25BA",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2581%25D0%25B5%25D1%2580%25D1%2582%25D0%25BE%25D0%25B1%25D0%25B5%25D0%25BA",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2581%25D0%25B8%25D0%25BD%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE%25D0%25BB",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2581%25D0%25B8%25D0%25BD%25D0%25BE%25D0%25BA%25D0%25BE%25D1%2580%25D0%25BC",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2581%25D1%2583%25D0%25BF%25D0%25BB%25D0%25B0%25D0%25B7%25D0%25B8%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2581%25D1%2584%25D0%25B5%25D1%2580%25D0%25BE%25D0%25B3%25D0%25B5%25D0%25BB%25D1%258C",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2584%25D0%25B5%25D1%2580%25D0%25BC%25D0%25B0%25D1%2582%25D1%2580%25D0%25BE%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2584%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2581%25D0%25BE%25D1%2582%25D1%2580%25D0%25BE%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25B0%25D0%25B9%25D0%25BC%25D0%25BE%25D0%25B2%25D0%25B8%25D1%2581",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25B0%25D0%25B9%25D0%25BB%25D1%2583%25D0%25B1%25D1%2580%25D0%25B8%25D0%25BA%25D1%2581",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D1%2580%25D0%25BE%25D0%25BD%25D0%25BE%25D1%2582%25D1%2580%25D0%25BE%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%258D%25D1%2583%25D1%2584%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2581%25D0%25B0",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BB%25D0%25B8%25D1%2581",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D0%25BC%25D0%25B5%25D0%25BB%25D0%25BE%25D1%2582%25D0%25B5%25D0%25BA%25D1%2581",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D0%25B5%25D0%25BB%25D0%25BE%25D0%25BA%25D1%2581%25D0%25B8%25D0%25BA%25D0%25B0%25D0%25BC",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE%25D0%25B7%25D0%25B0%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D0%25B5%25D0%25BB%25D0%25BE%25D0%25BA%25D1%2581%25D0%25B8%25D0%25BA%25D0%25B0%25D0%25BC%2520%25D0%25B1%25D1%2583%25D1%2584%25D1%2583%25D1%2581",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%258D%25D0%25BB%25D0%25BE%25D0%25BA%25D1%2581-%25D1%2581%25D0%25BE%25D0%25BB%25D0%25BE%25D1%2584%25D0%25B0%25D1%2580%25D0%25BC",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D0%25BE%25D0%25B2%25D0%25B0%25D1%2581%25D0%25B8%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B5%25D0%25BD%25D0%25B8%25D1%2582%25D1%2580%25D0%25BE%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D0%25B5%25D0%25BB%25D0%25BE%25D1%2584%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2581%2520%25D1%2580%25D0%25BE%25D0%25BC%25D1%2584%25D0%25B0%25D1%2580%25D0%25BC",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D0%25B5%25D0%25BB%25D0%25B1%25D0%25B5%25D0%25BA",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B1%25D0%25B8-%25D0%25BA%25D1%2581%25D0%25B8%25D0%25BA%25D0%25B0%25D0%25BC",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D0%25BB%25D1%2584%25D0%25BB%25D1%2583%25D1%2582%25D0%25BE%25D0%25BF",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25BE%25D0%25BD%25D0%25B4%25D1%2580%25D0%25BE%25D0%25B3%25D0%25B0%25D1%2580%25D0%25B4",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B4%25D1%2580%25D0%25B0%25D1%2581%25D1%2582%25D0%25BE%25D0%25BF",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D1%2583%25D0%25BA%25D0%25BE%25D1%2581%25D0%25B0%25D1%2582",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2580%25D1%2583%25D0%25BC%25D0%25B0%25D0%25BB%25D0%25BE%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B4%25D0%25BE%25D0%25BD%25D0%25B0",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B8%25D0%25BD%25D1%258A%25D0%25B5%25D0%25BA%25D1%2582%25D1%2580%25D0%25B0%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25BE%25D0%25BD%25D0%25B4%25D1%2580%25D0%25BE%25D0%25BB%25D0%25BE%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D1%2582%25D0%25BE%25D0%25B3%25D0%25B8%25D1%2581%25D1%2582%25D0%25B0%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D0%25BC%25D0%25B1%25D0%25B5%25D0%25BD%25D0%25B5%2520%25D0%25B1%25D0%25B8%25D0%25BE",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2581%25D1%2583%25D1%2581%25D1%2582%25D0%25B0%25D0%25B3%25D0%25B0%25D1%2580%25D0%25B4%2520%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D1%2581%25D1%2582%25D1%2580%25D0%25B0%25D0%25B4%25D0%25BE%25D0%25BB",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25BE%25D0%25BD%25D0%25B4%25D1%2580%25D0%25BE%25D0%25B8%25D1%2582%25D0%25B8%25D0%25BD%25D0%25B0%2520%25D1%2581%25D1%2583%25D0%25BB%25D1%258C%25D1%2584%25D0%25B0%25D1%2582",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%258D%25D0%25BB%25D1%258C%25D0%25B1%25D0%25BE%25D0%25BD%25D0%25B0",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25BE%25D0%25BD%25D1%2581%25D0%25B0%25D1%2582",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE%25D0%25B4%25D0%25B6%25D0%25B5%25D0%25BA%25D1%2582",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25B0%25D0%25B2%25D0%25B8%25D1%2580%2520%25D0%25B8%25D0%25BD%25D0%25BA%25D0%25B0%25D0%25BC%25D1%2584%25D0%25B0%25D1%2580%25D0%25BC",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25BE%25D0%25BD%25D0%25B4%25D1%2580%25D0%25BE%25D0%25BA%25D1%2581%25D0%25B8%25D0%25B4",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D1%2580%25D0%25B8%25D0%25BF%25D0%25B0%25D0%25B9%25D0%25B5%25D1%2580",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BE%25D1%2581%25D1%2582%25D0%25B5%25D0%25BE%25D0%25BA%25D0%25BE%25D0%25BB%25D0%25BB",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D0%25BF%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2581%25D0%25B0%25D1%2582%25D1%2580%25D0%25BE%25D0%25BD",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2582%25D1%2580%25D0%25B0%25D1%2583%25D0%25BC%25D0%25B5%25D0%25BB%25D1%258C",
    #                     "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25B0%25D0%25B9%25D0%25BB%25D1%2583%25D0%25B1%25D1%2580%25D0%25B8%25D0%25BA%25D1%2581"]
    #         pages = {}
    #         prep = []
    #         for i in range(len(linklist)):
    #             respone = requests.get(linklist[i])
    #             html = respone.text
    #             print(i)
    #             print(html)
    #
    #             soup = BeautifulSoup(html, 'html.parser')
    #             items = soup.find_all("div", class_="product-card")
    #             if not items:
    #                 print("не туда")
    #
    #             try:
    #                 for item in items:
    #                     prep.append(
    #                         {
    #                             'title': item.find("a", class_="product-card__info-title").text.strip(),
    #                             'price': item.find("div", class_="product-card__price").find("span").text.strip(),
    #                             'link': linklist[i]
    #                         }
    #                     )
    #             except:
    #                 print("Нет в наличии")
    #
    #         print(prep)
    #         with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\gubernskiyApteki_{date}.csv", 'w', newline='', encoding='utf-8') as file:
    #             writer = csv.writer(file, delimiter=';')
    #             writer.writerow(
    #                 ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
    #                  'Ссылка на препарат', 'Город', 'Цена'])
    #             for item in prep:
    #                 writer.writerow([date, '', item['title'], name, item['link'], 'Красноярск', item['price']])
    #
    # except:
    #     print("error gubernskieApteki")

    try:
        class lekoptorg(object):
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
                print(html)

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
            with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\lekopttorg_{date}.csv", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'], name, item['link'], '', item['price']])
    except:
        print("error Lekiptorg")

    try:
        class maksavit(object):
            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            URL = "https://maksavit.ru/"
            HEADERS = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
            }
            cookies = [
                {'name': "Архангельск", 'cookies': {"location_code": "0000110423", "location_selected": "Y"}},
                {'name': "Астрахань", 'cookies': {"location_code": "0000477579", "location_selected": "Y"}},
                {'name': "Брянск", 'cookies': {"location_code": "0000278519", "location_selected": "Y"}},
                {'name': "Владимир", 'cookies': {"location_code": "0000312126", "location_selected": "Y"}},
                {'name': "Волгоград", 'cookies': {"location_code": "0000426112", "location_selected": "Y"}},
                {'name': "Вологда", 'cookies': {"location_code": "0000336617", "location_selected": "Y"}},
                {'name': "Воронеж", 'cookies': {"location_code": "0000293598", "location_selected": "Y"}},
                {'name': "Иваново", 'cookies': {"location_code": "0000121319", "location_selected": "Y"}},
                {'name': "Калуга", 'cookies': {"location_code": "0000147475", "location_selected": "Y"}},
                {'name': "Киров", 'cookies': {"location_code": "0000583577", "location_selected": "Y"}},
                {'name': "Кострома", 'cookies': {"location_code": "0000159128", "location_selected": "Y"}},
                {'name': "Туапсе", 'cookies': {"location_code": "0000424382", "location_selected": "Y"}},
                {'name': "Красноярск", 'cookies': {"location_code": "0000896058", "location_selected": "Y"}},
                {'name': "Курск", 'cookies': {"location_code": "0000168097", "location_selected": "Y"}},
                {'name': "Липецк", 'cookies': {"location_code": "0000177609", "location_selected": "Y"}},
                {'name': "Пушкино", 'cookies': {"location_code": "0000058308", "location_selected": "Y"}},
                {'name': "Мурманск", 'cookies': {"location_code": "0000352775", "location_selected": "Y"}},
                {'name': "Нижний Новгород", 'cookies': {"location_code": "0000600317", "location_selected": "Y"}},
                {'name': "Великий Новгород", 'cookies': {"location_code": "0000377795", "location_selected": "Y"}},
                {'name': "Новосибирск", 'cookies': {"location_code": "0000949228", "location_selected": "Y"}},
                {'name': "Омск", 'cookies': {"location_code": "0000965067", "location_selected": "Y"}},
                {'name': "Орёл", 'cookies': {"location_code": "0000187229", "location_selected": "Y"}},
                {'name': "Великие Луки", 'cookies': {"location_code": "0000363367", "location_selected": "Y"}},
                {'name': "Уфа", 'cookies': {"location_code": "0000728734", "location_selected": "Y"}},
                {'name': "Петрозаводск", 'cookies': {"location_code": "0000330194", "location_selected": "Y"}},
                {'name': "Йошкар-Ола", 'cookies': {"location_code": "0000576828", "location_selected": "Y"}},
                {'name': "Саранск", 'cookies': {"location_code": "0000542813", "location_selected": "Y"}},
                {'name': "Казань", 'cookies': {"location_code": "0000550426", "location_selected": "Y"}},
                {'name': "Рязань", 'cookies': {"location_code": "0000197740", "location_selected": "Y"}},
                {'name': "Смоленск", 'cookies': {"location_code": "0000207393", "location_selected": "Y"}},
                {'name': "Тамбов", 'cookies': {"location_code": "0000220223", "location_selected": "Y"}},
                {'name': "Тула", 'cookies': {"location_code": "0000250453", "location_selected": "Y"}},
                {'name': "Чебоксары", 'cookies': {"location_code": "0000638402", "location_selected": "Y"}},
                {'name': "Ярославль", 'cookies': {"location_code": "0000263227", "location_selected": "Y"}}
            ]

            name = "Максавит"

            linklist = ["https://maksavit.ru/searching/?queryString=%D0%B0%D0%B4%D0%B0%D0%BD%D1%82",
                        "https://maksavit.ru/searching/?queryString=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://maksavit.ru/searching/?queryString=%D0%90%D0%A2%D0%A0%D0%98%20%D0%98%D0%9D%D0%96",
                        "https://maksavit.ru/searching/?queryString=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://maksavit.ru/searching/?queryString=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA%20%D0%BE%D1%80%D1%82%D0%BE",
                        "https://maksavit.ru/searching/?queryString=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82",
                        "https://maksavit.ru/searching/?queryString=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
                        "https://maksavit.ru/searching/?queryString=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB",
                        "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C%20%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
                        "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC",
                        "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
                        "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
                        "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
                        "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
                        "https://maksavit.ru/searching/?queryString=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://maksavit.ru/searching/?queryString=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
                        "https://maksavit.ru/searching/?queryString=%D0%BE%D1%81%D1%82%20%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BD%D0%B8%D0%BB",
                        "https://maksavit.ru/searching/?queryString=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
                        "https://maksavit.ru/searching/?queryString=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://maksavit.ru/searching/?queryString=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
                        "https://maksavit.ru/searching/?queryString=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
                        "https://maksavit.ru/searching/?queryString=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://maksavit.ru/searching/?queryString=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
                        "https://maksavit.ru/searching/?queryString=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
                        "https://maksavit.ru/searching/?queryString=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D1%80%D0%BE%D0%BC",
                        "https://maksavit.ru/searching/?queryString=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
                        "https://maksavit.ru/searching/?queryString=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
                        "https://maksavit.ru/searching/?queryString=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
                        "https://maksavit.ru/searching/?queryString=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
                        "https://maksavit.ru/searching/?queryString=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
                        "https://maksavit.ru/searching/?queryString=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
                        "https://maksavit.ru/searching/?queryString=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://maksavit.ru/searching/?queryString=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC",
                        "https://maksavit.ru/searching/?queryString=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81",
                        "https://maksavit.ru/searching/?queryString=%D0%BC%D0%B5%D0%BB%D1%8C%D0%B1%D0%B5%D0%BA",
                        "https://maksavit.ru/searching/?queryString=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://maksavit.ru/searching/?queryString=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF",
                        "https://maksavit.ru/searching/?queryString=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
                        "https://maksavit.ru/searching/?queryString=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
                        "https://maksavit.ru/searching/?queryString=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
                        "https://maksavit.ru/searching/?queryString=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%B4%D0%BE%D0%BD%D0%B0",
                        "https://maksavit.ru/searching/?queryString=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5%20%D0%B1%D0%B8%D0%BE",
                        "https://maksavit.ru/searching/?queryString=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4%20%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://maksavit.ru/searching/?queryString=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB",
                        "https://maksavit.ru/searching/?queryString=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0%20%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82",
                        "https://maksavit.ru/searching/?queryString=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
                        "https://maksavit.ru/searching/?queryString=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
                        "https://maksavit.ru/searching/?queryString=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80%20%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
                        "https://maksavit.ru/searching/?queryString=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
                        "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
                        "https://maksavit.ru/searching/?queryString=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                        "https://maksavit.ru/searching/?queryString=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://maksavit.ru/searching/?queryString=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
                        "https://maksavit.ru/searching/?queryString=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
            pages = {}

            for cookie in cookies:
                prep = []
                for i in range(len(linklist)):
                    respone = requests.get(linklist[i], cookies=cookie["cookies"])
                    html = respone.text
                    print(html)

                    soup = BeautifulSoup(html, 'html.parser')
                    items = soup.find_all("div", class_="product-card-block")
                    if not items:
                        print("не туда")

                    for item in items:
                        try:
                            prep.append(
                                {
                                    'title': item.find("a", class_="product-card-block__title").find("span").text.strip(),
                                    'price': item.find("div", class_="product-price__current-price").find(
                                        "span").text.strip(),
                                    'link': linklist[i]
                                }
                            )
                        except:
                            print("not find")

                    print(prep)

                with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\Maksavit_{date}.csv", 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow(['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки',
                                     'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
                    for item in prep:
                        writer.writerow([date, '', item['title'], name, item['link'], cookie['name'], item['price']])
    except:
        print("error Maksavit")


    try:
        class monastirev(object):
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
            with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\monastirev{date}.csv", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'] + item['title2'], name, item['link'], 'Москва', item['price']])
    except:
        print("error Monastirev")


    try:
        class neofarm(object):
            url = "https://neopharm.ru/drugs/"
            HEADERS = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"
            }

            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            name = "НеоФарм"

            linklist = ["https://neopharm.ru/search?name=%D0%B0%D0%B4%D0%B0%D0%BD%D1%82",
                        "https://neopharm.ru/search?name=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
                        "https://neopharm.ru/search?name=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://neopharm.ru/search?name=%D0%B0%D1%82%D1%80%D0%B8%20%D0%B8%D0%BD%D0%B6",
                        "https://neopharm.ru/search?name=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://neopharm.ru/search?name=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://neopharm.ru/search?name=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82",
                        "https://neopharm.ru/search?name=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD",
                        "https://neopharm.ru/search?name=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
                        "https://neopharm.ru/search?name=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB",
                        "https://neopharm.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD",
                        "https://neopharm.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://neopharm.ru/search?name=%D0%93%D0%98%D0%90%D0%9B%D0%A3%D0%90%D0%9B%D0%AC%20%D0%90%D0%A0%D0%A2%D0%A0%D0%9E",
                        "https://neopharm.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
                        "https://neopharm.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC",
                        "https://neopharm.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
                        "https://neopharm.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
                        "https://neopharm.ru/search?name=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
                        "https://neopharm.ru/search?name=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
                        "https://neopharm.ru/search?name=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
                        "https://neopharm.ru/search?name=%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
                        "https://neopharm.ru/search?name=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                        "https://neopharm.ru/search?name=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
                        "https://neopharm.ru/search?name=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://neopharm.ru/search?name=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
                        "https://neopharm.ru/search?name=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
                        "https://neopharm.ru/search?name=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
                        "https://neopharm.ru/search?name=%D0%BE%D1%81%D1%82%20%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD",
                        "https://neopharm.ru/search?name=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB",
                        "https://neopharm.ru/search?name=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
                        "https://neopharm.ru/search?name=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://neopharm.ru/search?name=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
                        "https://neopharm.ru/search?name=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
                        "https://neopharm.ru/search?name=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://neopharm.ru/search?name=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
                        "https://neopharm.ru/search?name=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
                        "https://neopharm.ru/search?name=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D1%80%D0%BE%D0%BC",
                        "https://neopharm.ru/search?name=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
                        "https://neopharm.ru/search?name=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
                        "https://neopharm.ru/search?name=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://neopharm.ru/search?name=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://neopharm.ru/search?name=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
                        "https://neopharm.ru/search?name=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
                        "https://neopharm.ru/search?name=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://neopharm.ru/search?name=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
                        "https://neopharm.ru/search?name=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
                        "https://neopharm.ru/search?name=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
                        "https://neopharm.ru/search?name=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://neopharm.ru/search?name=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
                        "https://neopharm.ru/search?name=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC",
                        "https://neopharm.ru/search?name=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD",
                        "https://neopharm.ru/search?name=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
                        "https://neopharm.ru/search?name=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81",
                        "https://neopharm.ru/search?name=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA",
                        "https://neopharm.ru/search?name=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://neopharm.ru/search?name=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF",
                        "https://neopharm.ru/search?name=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
                        "https://neopharm.ru/search?name=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
                        "https://neopharm.ru/search?name=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
                        "https://neopharm.ru/search?name=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://neopharm.ru/search?name=%D0%B4%D0%BE%D0%BD%D0%B0",
                        "https://neopharm.ru/search?name=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
                        "https://neopharm.ru/search?name=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
                        "https://neopharm.ru/search?name=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
                        "https://neopharm.ru/search?name=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5%20%D0%B1%D0%B8%D0%BE",
                        "https://neopharm.ru/search?name=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4%20%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://neopharm.ru/search?name=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB",
                        "https://neopharm.ru/search?name=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0%20%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82",
                        "https://neopharm.ru/search?name=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
                        "https://neopharm.ru/search?name=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
                        "https://neopharm.ru/search?name=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://neopharm.ru/search?name=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80",
                        "https://neopharm.ru/search?name=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
                        "https://neopharm.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
                        "https://neopharm.ru/search?name=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                        "https://neopharm.ru/search?name=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://neopharm.ru/search?name=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
                        "https://neopharm.ru/search?name=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
            pages = {}
            prep = []

            for i in range(len(linklist)):
                respone = requests.get(linklist[i])
                html = respone.text
                print(html)

                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all("div", class_="col-4 col-xs-12 item-card")
                if not items:
                    print("")

                # берем данные с каждой карточки

                for item in items:
                    prep.append(
                        {
                            'title': item.find("div", class_="text").text.strip(),
                            'price': item.find("div", class_="new_price").find("span").text.strip(),
                            'link': linklist[i]
                        }
                    )

            print(prep)
            with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\NeoFarm_{date}.csv", 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'], name, item['link'], "Москва", item['price']])
    except:
        print("error Neofarm")


    try:
        class ozerki(object):
            URL = "https://ozerki.ru/"
            HEADERS = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
            }

            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            name = "Озерки"

            linklist = ["https://ozerki.ru/catalog/?q=%D0%90%D0%B4%D0%B0%D0%BD%D1%82",
                        "https://ozerki.ru/catalog/?q=%D0%90%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%90%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://ozerki.ru/catalog/?q=%D0%90%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6",
                        "https://ozerki.ru/catalog/?q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://ozerki.ru/catalog/?q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE",
                        "https://ozerki.ru/catalog/?q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82",
                        "https://ozerki.ru/catalog/?q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4",
                        "https://ozerki.ru/catalog/?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
                        "https://ozerki.ru/catalog/?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB",
                        "https://ozerki.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F",
                        "https://ozerki.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://ozerki.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
                        "https://ozerki.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C",
                        "https://ozerki.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
                        "https://ozerki.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
                        "https://ozerki.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
                        "https://ozerki.ru/catalog/?q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
                        "https://ozerki.ru/catalog/?q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://ozerki.ru/catalog/?q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
                        "https://ozerki.ru/catalog/?q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB",
                        "https://ozerki.ru/catalog/?q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
                        "https://ozerki.ru/catalog/?q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://ozerki.ru/catalog/?q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
                        "https://ozerki.ru/catalog/?q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
                        "https://ozerki.ru/catalog/?q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://ozerki.ru/catalog/?q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
                        "https://ozerki.ru/catalog/?q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
                        "https://ozerki.ru/catalog/?q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC",
                        "https://ozerki.ru/catalog/?q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
                        "https://ozerki.ru/catalog/?q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
                        "https://ozerki.ru/catalog/?q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
                        "https://ozerki.ru/catalog/?q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
                        "https://ozerki.ru/catalog/?q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
                        "https://ozerki.ru/catalog/?q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
                        "https://ozerki.ru/catalog/?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://ozerki.ru/catalog/?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC",
                        "https://ozerki.ru/catalog/?q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
                        "https://ozerki.ru/catalog/?q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA",
                        "https://ozerki.ru/catalog/?q=%D0%B1%D0%B8+%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://ozerki.ru/catalog/?q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF",
                        "https://ozerki.ru/catalog/?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
                        "https://ozerki.ru/catalog/?q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
                        "https://ozerki.ru/catalog/?q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
                        "https://ozerki.ru/catalog/?q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%B4%D0%BE%D0%BD%D0%B0",
                        "https://ozerki.ru/catalog/?q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE",
                        "https://ozerki.ru/catalog/?q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://ozerki.ru/catalog/?q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB",
                        "https://ozerki.ru/catalog/?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82",
                        "https://ozerki.ru/catalog/?q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
                        "https://ozerki.ru/catalog/?q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
                        "https://ozerki.ru/catalog/?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://ozerki.ru/catalog/?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
                        "https://ozerki.ru/catalog/?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
                        "https://ozerki.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
                        "https://ozerki.ru/catalog/?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                        "https://ozerki.ru/catalog/?q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://ozerki.ru/catalog/?q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
                        "https://ozerki.ru/catalog/?q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]

            prep = []
            for i in range(len(linklist)):
                respone = requests.get(linklist[i])
                html = respone.text
                print(i)

                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all("div", class_="card")
                if not items:
                    print("не туда")

                # берем данные с каждой карточки
                try:
                    for item in items:
                        prep.append(
                            {
                                'title': item.find("a", class_="card__title").find("span").text.strip(),
                                'price': item.find("div", class_="card__price").find("span").text.strip(),
                                'link': linklist[i]
                            }
                        )
                except:
                    print("Нет")

            print(prep)
            with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\ozerki{date}.csv", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'], name, item['link'], 'Москва и МО', item['price']])
    except:
        print("error Ozerki")


    try:
        class poiskLekarstv(object):
            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            URL = "https://www.poisklekarstv.com/"
            HEADERS = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
            }

            # Голые сслыки без городов "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%90%D0%B4%D0%B0%D0%BD%D1%82&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%A5%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%BE%D0%BD%D0%B0&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C&location=", "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=",
            linklist = [
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%90%D0%B4%D0%B0%D0%BD%D1%82&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%A5%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%BE%D0%BD%D0%B0&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%90%D0%B4%D0%B0%D0%BD%D1%82&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%A5%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%BE%D0%BD%D0%B0&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%90%D0%B4%D0%B0%D0%BD%D1%82&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%A5%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%BE%D0%BD%D0%B0&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%90%D0%B4%D0%B0%D0%BD%D1%82&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%A5%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%BE%D0%BD%D0%B0&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%90%D0%B4%D0%B0%D0%BD%D1%82&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%A5%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%BE%D0%BD%D0%B0&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%90%D0%B4%D0%B0%D0%BD%D1%82&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%A5%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%BE%D0%BD%D0%B0&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%90%D0%B4%D0%B0%D0%BD%D1%82&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%A5%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%BE%D0%BD%D0%B0&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%9E%D0%BC%D1%81%D0%BA",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%90%D0%B4%D0%B0%D0%BD%D1%82&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%A5%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%BE%D0%BD%D0%B0&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%90%D0%B4%D0%B0%D0%BD%D1%82&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%A5%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%BE%D0%BD%D0%B0&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%90%D0%B4%D0%B0%D0%BD%D1%82&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%A5%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B8%D0%B0%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%A3%D1%84%D0%B0%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B4%D0%BE%D0%BD%D0%B0&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C&location=%D0%A3%D1%84%D0%B0",
                "https://www.poisklekarstv.com/search?lat=&lng=&q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81&location=%D0%A3%D1%84%D0%B0"]

            for i in range(len(linklist)):
                prep = []
                html = requests.get(linklist[i])
                result = html.text
                print(i)
                # sleep(uniform(0, 1))

                soup = BeautifulSoup(result, "html.parser")
                items = soup.find_all("li", class_="apteka")
                if not items:
                    print("не туда")

                try:
                    for item in items:
                        prep.append(
                            {
                                "Apteka": item.find("ul", class_="list-inline").find("a").text.strip(),
                                "name": item.find("li", itemprop="offers").find("span", itemprop="name").text.strip(),
                                "cost": item.find("span", class_="cost").text.strip(),
                                "link": item.find("strong").find("a").get("href")
                            }
                        )
                except:
                    print("error")

                print(prep)

                citys = []

                if i <= 78:
                    citys.append("Москва")
                elif i > 78 and i <= 156:
                    citys.append("Санкт-Петербург")
                elif i > 156 and i <= 234:
                    citys.append("Новосибирск")
                elif i > 234 and i <= 312:
                    citys.append("Екатеринбург")
                elif i > 312 and i <= 390:
                    citys.append("Нижний Новгород")
                elif i > 390 and i <= 468:
                    citys.append("Челябинск")
                elif i > 468 and i <= 546:
                    citys.append("Омск")
                elif i > 546 and i <= 624:
                    citys.append("Самара")
                elif i > 624 and i <= 702:
                    citys.append("Растов-на-Дону")
                elif i > 702 and i <= 780:
                    citys.append("Уфа")

                with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\Аптечные сети{date}.csv", 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow(['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки',
                                     'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
                    for item in prep:
                        writer.writerow([date, '', item['name'], item["Apteka"], item['link'], citys, item['cost']])
    except:
        print("error PoiskLekarstv")


    try:
        class samsonFarma(object):
            URL = "https://samson-pharma.ru/"
            HEADERS = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
            }

            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            name = "Самсон фарма"

            linklist = ["https://samson-pharma.ru/catalog/?q=%D0%B0%D0%B4%D0%B0%D0%BD%D1%82",
                        "https://samson-pharma.ru/catalog/?q=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://samson-pharma.ru/catalog/?q=%D0%B0%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6",
                        "https://samson-pharma.ru/catalog/?q=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://samson-pharma.ru/catalog/?q=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE",
                        "https://samson-pharma.ru/catalog/?q=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82",
                        "https://samson-pharma.ru/catalog/?q=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4",
                        "https://samson-pharma.ru/catalog/?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
                        "https://samson-pharma.ru/catalog/?q=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB",
                        "https://samson-pharma.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F",
                        "https://samson-pharma.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://samson-pharma.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
                        "https://samson-pharma.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C",
                        "https://samson-pharma.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
                        "https://samson-pharma.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
                        "https://samson-pharma.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
                        "https://samson-pharma.ru/catalog/?q=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
                        "https://samson-pharma.ru/catalog/?q=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://samson-pharma.ru/catalog/?q=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
                        "https://samson-pharma.ru/catalog/?q=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BB",
                        "https://samson-pharma.ru/catalog/?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB",
                        "https://samson-pharma.ru/catalog/?q=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
                        "https://samson-pharma.ru/catalog/?q=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://samson-pharma.ru/catalog/?q=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
                        "https://samson-pharma.ru/catalog/?q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
                        "https://samson-pharma.ru/catalog/?q=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
                        "https://samson-pharma.ru/catalog/?q=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://samson-pharma.ru/catalog/?q=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
                        "https://samson-pharma.ru/catalog/?q=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
                        "https://samson-pharma.ru/catalog/?q=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC",
                        "https://samson-pharma.ru/catalog/?q=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
                        "https://samson-pharma.ru/catalog/?q=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
                        "https://samson-pharma.ru/catalog/?q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
                        "https://samson-pharma.ru/catalog/?q=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
                        "https://samson-pharma.ru/catalog/?q=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
                        "https://samson-pharma.ru/catalog/?q=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
                        "https://samson-pharma.ru/catalog/?q=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://samson-pharma.ru/catalog/?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC",
                        "https://samson-pharma.ru/catalog/?q=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA",
                        "https://samson-pharma.ru/catalog/?q=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://samson-pharma.ru/catalog/?q=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF",
                        "https://samson-pharma.ru/catalog/?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
                        "https://samson-pharma.ru/catalog/?q=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
                        "https://samson-pharma.ru/catalog/?q=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
                        "https://samson-pharma.ru/catalog/?q=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D0%B4%D0%BE%D0%BD%D0%B0",
                        "https://samson-pharma.ru/catalog/?q=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE",
                        "https://samson-pharma.ru/catalog/?q=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://samson-pharma.ru/catalog/?q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB",
                        "https://samson-pharma.ru/catalog/?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82",
                        "https://samson-pharma.ru/catalog/?q=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
                        "https://samson-pharma.ru/catalog/?q=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
                        "https://samson-pharma.ru/catalog/?q=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://samson-pharma.ru/catalog/?q=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
                        "https://samson-pharma.ru/catalog/?q=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
                        "https://samson-pharma.ru/catalog/?q=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
                        "https://samson-pharma.ru/catalog/?q=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                        "https://samson-pharma.ru/catalog/?q=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://samson-pharma.ru/catalog/?q=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
                        "https://samson-pharma.ru/catalog/?q=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
            pages = {}
            prep = []
            for i in range(len(linklist)):
                respone = requests.get(linklist[i])
                html = respone.text
                print(i)

                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all("div", class_="product-card")
                if not items:
                    print("не туда")

                # берем данные с каждой карточки
                try:
                    for item in items:
                        prep.append(
                            {
                                'title': item.find("a", class_="product-card__title").text.strip(),
                                'price': item.find("div", class_="price_cnt_element").text.strip(),
                                'link': linklist[i]
                            }
                        )
                except:
                    print("Нет")

            print(prep)
            with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\SamsonFarma{date}.csv", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'], name, item['link'], '', item['price']])

    except:
        print("error SamsonFarma")


    try:
        class socialApteka(object):
            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            url = "https://social-apteka.ru/catalog/"
            HEADERS = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
            }

            name = "Социальная аптека"

            # citys = ['https://astrahan.', 'https://belgorod.', 'https://volgograd.', 'https://voronezh.', 'https://krasnodar.', 'https://lipeck.', 'https://majkop.', 'https://', 'https://stavropol.',
            linklist = [
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/ameloteks-r-r-d-in-1-5ml-n5-soteks_33449/",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-r-r-dvnutrisust-vved-2ml-2_1549818/",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-plyus-r-r-dvnutrisust-vved-2ml-86_1549819/",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-forte-r-r-dvnutrisust-vved-shpric-3ml-53_29463/",
                "https://astrahan.social-apteka.ru/catalog/kat/armaviskon-hondro-protez-sinovialnoy-jidkosti-3ml-n1-groteks-7_34113316/",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/artogistan-r-r-din-100mgml-2ml-n10-41_28657/",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/genitron-r-r-din-10mgml-15ml-n5-74_27287/",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/gialurom-r-r-vsustav-shpric-15-2ml-n1-90_38239/",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/gialurom-cs-vsustav-shpric-15-3ml-n1-10_23499/",
                "https://astrahan.social-apteka.ru/search_to_go/?q=%D0%94%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/inektran-r-r-din-100mgml-2ml-n10-95_27204/",
                "https://astrahan.social-apteka.ru/catalog/protivovospalitelnye-sredstva-dlya-oporno-dvigatelnogo-apparata/meloksikam-r-r-din-10mgml-15ml-n5-100_8389805/",
                "https://astrahan.social-apteka.ru/catalog/obezbolivayushchie/movalis-amp-15mg-15ml-n5-67_20078/",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/mukosat-amp-10-1ml-n10-84_16578/",
                "https://astrahan.social-apteka.ru/catalog/kat/osteokoll-implantat-kollagen-d-periartikulyarnogo-vved-2ml-n5-guna-70_34085377/",
                "https://astrahan.social-apteka.ru/catalog/kat/pleksatron-kollagen-dvnutrisustav-i-periart-vved-2ml-n5-guna-96_34077275/",
                "https://astrahan.social-apteka.ru/catalog/kat/ripart-long-sr-vo-dzameshch-sinov-jidk-20mgml-2ml-shpric-n1-ingal-70_32534640/",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/ripart-long-sr-vo-dzameshch-sinovialnoy-jidkosti-20mgml-shpric-3ml-n1-rossiya-18_71697/",
                "https://astrahan.social-apteka.ru/catalog/kat/ripart-forte-sr-vo-dlya-zameshcheniya-sinovialnoy-jidkosti-15mgml-shpric-3ml-100_34077342/",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/rumalon-amp-1ml-n10-39_24853/",
                "https://astrahan.social-apteka.ru/catalog/gomeopatiya/traumel-s-amp-22ml-n5-44_11979/",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-1-2ml-n1-77_33430/",
                "https://astrahan.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-15-2ml-n1-38_34995/",
                "https://astrahan.social-apteka.ru/catalog/kat/fleksotron-kross-implantant-din-60mg3ml-sayvijn-bayotek-6_32534636/",
                "https://astrahan.social-apteka.ru/catalog/kat/fleksotron-solo-implant-din-22-22mgml-2ml-sistema-plyus-20_33579271/",
                "https://astrahan.social-apteka.ru/catalog/kat/fleksotron-ultra-implant-din-25-25mgml-48ml-albomed-63_33593771/",
                "https://astrahan.social-apteka.ru/catalog/kat/hronotron-implantat-inekc-gel-dlya-vsust-vved-20mgml-2ml-n1-mastelli-61_33593758/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/ameloteks-r-r-d-in-1-5ml-n5-soteks_33449/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-r-r-dvnutrisust-vved-2ml-2_1549818/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-plyus-r-r-dvnutrisust-vved-2ml-86_1549819/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-forte-r-r-dvnutrisust-vved-shpric-3ml-53_29463/",
                "https://belgorod.social-apteka.ru/catalog/kat/armaviskon-hondro-protez-sinovialnoy-jidkosti-3ml-n1-groteks-7_34113316/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/artogistan-r-r-din-100mgml-2ml-n10-41_28657/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/genitron-r-r-din-10mgml-15ml-n5-74_27287/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/gialurom-r-r-vsustav-shpric-15-2ml-n1-90_38239/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/gialurom-cs-vsustav-shpric-15-3ml-n1-10_23499/",
                "https://belgorod.social-apteka.ru/search_to_go/?q=%D0%94%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/inektran-r-r-din-100mgml-2ml-n10-95_27204/",
                "https://belgorod.social-apteka.ru/catalog/protivovospalitelnye-sredstva-dlya-oporno-dvigatelnogo-apparata/meloksikam-r-r-din-10mgml-15ml-n5-100_8389805/",
                "https://belgorod.social-apteka.ru/catalog/obezbolivayushchie/movalis-amp-15mg-15ml-n5-67_20078/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/mukosat-amp-10-1ml-n10-84_16578/",
                "https://belgorod.social-apteka.ru/catalog/kat/osteokoll-implantat-kollagen-d-periartikulyarnogo-vved-2ml-n5-guna-70_34085377/",
                "https://belgorod.social-apteka.ru/catalog/kat/pleksatron-kollagen-dvnutrisustav-i-periart-vved-2ml-n5-guna-96_34077275/",
                "https://belgorod.social-apteka.ru/catalog/kat/ripart-long-sr-vo-dzameshch-sinov-jidk-20mgml-2ml-shpric-n1-ingal-70_32534640/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/ripart-long-sr-vo-dzameshch-sinovialnoy-jidkosti-20mgml-shpric-3ml-n1-rossiya-18_71697/",
                "https://belgorod.social-apteka.ru/catalog/kat/ripart-forte-sr-vo-dlya-zameshcheniya-sinovialnoy-jidkosti-15mgml-shpric-3ml-100_34077342/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/rumalon-amp-1ml-n10-39_24853/",
                "https://belgorod.social-apteka.ru/catalog/gomeopatiya/traumel-s-amp-22ml-n5-44_11979/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-1-2ml-n1-77_33430/",
                "https://belgorod.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-15-2ml-n1-38_34995/",
                "https://belgorod.social-apteka.ru/catalog/kat/fleksotron-kross-implantant-din-60mg3ml-sayvijn-bayotek-6_32534636/",
                "https://belgorod.social-apteka.ru/catalog/kat/fleksotron-solo-implant-din-22-22mgml-2ml-sistema-plyus-20_33579271/",
                "https://belgorod.social-apteka.ru/catalog/kat/fleksotron-ultra-implant-din-25-25mgml-48ml-albomed-63_33593771/",
                "https://belgorod.social-apteka.ru/catalog/kat/hronotron-implantat-inekc-gel-dlya-vsust-vved-20mgml-2ml-n1-mastelli-61_33593758/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/ameloteks-r-r-d-in-1-5ml-n5-soteks_33449/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-r-r-dvnutrisust-vved-2ml-2_1549818/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-plyus-r-r-dvnutrisust-vved-2ml-86_1549819/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-forte-r-r-dvnutrisust-vved-shpric-3ml-53_29463/",
                "https://volgograd.social-apteka.ru/catalog/kat/armaviskon-hondro-protez-sinovialnoy-jidkosti-3ml-n1-groteks-7_34113316/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/artogistan-r-r-din-100mgml-2ml-n10-41_28657/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/genitron-r-r-din-10mgml-15ml-n5-74_27287/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/gialurom-r-r-vsustav-shpric-15-2ml-n1-90_38239/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/gialurom-cs-vsustav-shpric-15-3ml-n1-10_23499/",
                "https://volgograd.social-apteka.ru/search_to_go/?q=%D0%94%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/inektran-r-r-din-100mgml-2ml-n10-95_27204/",
                "https://volgograd.social-apteka.ru/catalog/protivovospalitelnye-sredstva-dlya-oporno-dvigatelnogo-apparata/meloksikam-r-r-din-10mgml-15ml-n5-100_8389805/",
                "https://volgograd.social-apteka.ru/catalog/obezbolivayushchie/movalis-amp-15mg-15ml-n5-67_20078/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/mukosat-amp-10-1ml-n10-84_16578/",
                "https://volgograd.social-apteka.ru/catalog/kat/osteokoll-implantat-kollagen-d-periartikulyarnogo-vved-2ml-n5-guna-70_34085377/",
                "https://volgograd.social-apteka.ru/catalog/kat/pleksatron-kollagen-dvnutrisustav-i-periart-vved-2ml-n5-guna-96_34077275/",
                "https://volgograd.social-apteka.ru/catalog/kat/ripart-long-sr-vo-dzameshch-sinov-jidk-20mgml-2ml-shpric-n1-ingal-70_32534640/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/ripart-long-sr-vo-dzameshch-sinovialnoy-jidkosti-20mgml-shpric-3ml-n1-rossiya-18_71697/",
                "https://volgograd.social-apteka.ru/catalog/kat/ripart-forte-sr-vo-dlya-zameshcheniya-sinovialnoy-jidkosti-15mgml-shpric-3ml-100_34077342/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/rumalon-amp-1ml-n10-39_24853/",
                "https://volgograd.social-apteka.ru/catalog/gomeopatiya/traumel-s-amp-22ml-n5-44_11979/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-1-2ml-n1-77_33430/",
                "https://volgograd.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-15-2ml-n1-38_34995/",
                "https://volgograd.social-apteka.ru/catalog/kat/fleksotron-kross-implantant-din-60mg3ml-sayvijn-bayotek-6_32534636/",
                "https://volgograd.social-apteka.ru/catalog/kat/fleksotron-solo-implant-din-22-22mgml-2ml-sistema-plyus-20_33579271/",
                "https://volgograd.social-apteka.ru/catalog/kat/fleksotron-ultra-implant-din-25-25mgml-48ml-albomed-63_33593771/",
                "https://volgograd.social-apteka.ru/catalog/kat/hronotron-implantat-inekc-gel-dlya-vsust-vved-20mgml-2ml-n1-mastelli-61_33593758/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/ameloteks-r-r-d-in-1-5ml-n5-soteks_33449/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-r-r-dvnutrisust-vved-2ml-2_1549818/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-plyus-r-r-dvnutrisust-vved-2ml-86_1549819/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-forte-r-r-dvnutrisust-vved-shpric-3ml-53_29463/",
                "https://voronezh.social-apteka.ru/catalog/kat/armaviskon-hondro-protez-sinovialnoy-jidkosti-3ml-n1-groteks-7_34113316/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/artogistan-r-r-din-100mgml-2ml-n10-41_28657/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/genitron-r-r-din-10mgml-15ml-n5-74_27287/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/gialurom-r-r-vsustav-shpric-15-2ml-n1-90_38239/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/gialurom-cs-vsustav-shpric-15-3ml-n1-10_23499/",
                "https://voronezh.social-apteka.ru/search_to_go/?q=%D0%94%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/inektran-r-r-din-100mgml-2ml-n10-95_27204/",
                "https://voronezh.social-apteka.ru/catalog/protivovospalitelnye-sredstva-dlya-oporno-dvigatelnogo-apparata/meloksikam-r-r-din-10mgml-15ml-n5-100_8389805/",
                "https://voronezh.social-apteka.ru/catalog/obezbolivayushchie/movalis-amp-15mg-15ml-n5-67_20078/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/mukosat-amp-10-1ml-n10-84_16578/",
                "https://voronezh.social-apteka.ru/catalog/kat/osteokoll-implantat-kollagen-d-periartikulyarnogo-vved-2ml-n5-guna-70_34085377/",
                "https://voronezh.social-apteka.ru/catalog/kat/pleksatron-kollagen-dvnutrisustav-i-periart-vved-2ml-n5-guna-96_34077275/",
                "https://voronezh.social-apteka.ru/catalog/kat/ripart-long-sr-vo-dzameshch-sinov-jidk-20mgml-2ml-shpric-n1-ingal-70_32534640/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/ripart-long-sr-vo-dzameshch-sinovialnoy-jidkosti-20mgml-shpric-3ml-n1-rossiya-18_71697/",
                "https://voronezh.social-apteka.ru/catalog/kat/ripart-forte-sr-vo-dlya-zameshcheniya-sinovialnoy-jidkosti-15mgml-shpric-3ml-100_34077342/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/rumalon-amp-1ml-n10-39_24853/",
                "https://voronezh.social-apteka.ru/catalog/gomeopatiya/traumel-s-amp-22ml-n5-44_11979/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-1-2ml-n1-77_33430/",
                "https://voronezh.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-15-2ml-n1-38_34995/",
                "https://voronezh.social-apteka.ru/catalog/kat/fleksotron-kross-implantant-din-60mg3ml-sayvijn-bayotek-6_32534636/",
                "https://voronezh.social-apteka.ru/catalog/kat/fleksotron-solo-implant-din-22-22mgml-2ml-sistema-plyus-20_33579271/",
                "https://voronezh.social-apteka.ru/catalog/kat/fleksotron-ultra-implant-din-25-25mgml-48ml-albomed-63_33593771/",
                "https://voronezh.social-apteka.ru/catalog/kat/hronotron-implantat-inekc-gel-dlya-vsust-vved-20mgml-2ml-n1-mastelli-61_33593758/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/ameloteks-r-r-d-in-1-5ml-n5-soteks_33449/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-r-r-dvnutrisust-vved-2ml-2_1549818/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-plyus-r-r-dvnutrisust-vved-2ml-86_1549819/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-forte-r-r-dvnutrisust-vved-shpric-3ml-53_29463/",
                "https://lipeck.social-apteka.ru/catalog/kat/armaviskon-hondro-protez-sinovialnoy-jidkosti-3ml-n1-groteks-7_34113316/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/artogistan-r-r-din-100mgml-2ml-n10-41_28657/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/genitron-r-r-din-10mgml-15ml-n5-74_27287/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/gialurom-r-r-vsustav-shpric-15-2ml-n1-90_38239/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/gialurom-cs-vsustav-shpric-15-3ml-n1-10_23499/",
                "https://lipeck.social-apteka.ru/search_to_go/?q=%D0%94%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/inektran-r-r-din-100mgml-2ml-n10-95_27204/",
                "https://lipeck.social-apteka.ru/catalog/protivovospalitelnye-sredstva-dlya-oporno-dvigatelnogo-apparata/meloksikam-r-r-din-10mgml-15ml-n5-100_8389805/",
                "https://lipeck.social-apteka.ru/catalog/obezbolivayushchie/movalis-amp-15mg-15ml-n5-67_20078/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/mukosat-amp-10-1ml-n10-84_16578/",
                "https://lipeck.social-apteka.ru/catalog/kat/osteokoll-implantat-kollagen-d-periartikulyarnogo-vved-2ml-n5-guna-70_34085377/",
                "https://lipeck.social-apteka.ru/catalog/kat/pleksatron-kollagen-dvnutrisustav-i-periart-vved-2ml-n5-guna-96_34077275/",
                "https://lipeck.social-apteka.ru/catalog/kat/ripart-long-sr-vo-dzameshch-sinov-jidk-20mgml-2ml-shpric-n1-ingal-70_32534640/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/ripart-long-sr-vo-dzameshch-sinovialnoy-jidkosti-20mgml-shpric-3ml-n1-rossiya-18_71697/",
                "https://lipeck.social-apteka.ru/catalog/kat/ripart-forte-sr-vo-dlya-zameshcheniya-sinovialnoy-jidkosti-15mgml-shpric-3ml-100_34077342/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/rumalon-amp-1ml-n10-39_24853/",
                "https://lipeck.social-apteka.ru/catalog/gomeopatiya/traumel-s-amp-22ml-n5-44_11979/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-1-2ml-n1-77_33430/",
                "https://lipeck.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-15-2ml-n1-38_34995/",
                "https://lipeck.social-apteka.ru/catalog/kat/fleksotron-kross-implantant-din-60mg3ml-sayvijn-bayotek-6_32534636/",
                "https://lipeck.social-apteka.ru/catalog/kat/fleksotron-solo-implant-din-22-22mgml-2ml-sistema-plyus-20_33579271/",
                "https://lipeck.social-apteka.ru/catalog/kat/fleksotron-ultra-implant-din-25-25mgml-48ml-albomed-63_33593771/",
                "https://lipeck.social-apteka.ru/catalog/kat/hronotron-implantat-inekc-gel-dlya-vsust-vved-20mgml-2ml-n1-mastelli-61_33593758/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/ameloteks-r-r-d-in-1-5ml-n5-soteks_33449/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-r-r-dvnutrisust-vved-2ml-2_1549818/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-plyus-r-r-dvnutrisust-vved-2ml-86_1549819/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-forte-r-r-dvnutrisust-vved-shpric-3ml-53_29463/",
                "https://krasnodar.social-apteka.ru/catalog/kat/armaviskon-hondro-protez-sinovialnoy-jidkosti-3ml-n1-groteks-7_34113316/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/artogistan-r-r-din-100mgml-2ml-n10-41_28657/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/genitron-r-r-din-10mgml-15ml-n5-74_27287/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/gialurom-r-r-vsustav-shpric-15-2ml-n1-90_38239/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/gialurom-cs-vsustav-shpric-15-3ml-n1-10_23499/",
                "https://krasnodar.social-apteka.ru/search_to_go/?q=%D0%94%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/inektran-r-r-din-100mgml-2ml-n10-95_27204/",
                "https://krasnodar.social-apteka.ru/catalog/protivovospalitelnye-sredstva-dlya-oporno-dvigatelnogo-apparata/meloksikam-r-r-din-10mgml-15ml-n5-100_8389805/",
                "https://krasnodar.social-apteka.ru/catalog/obezbolivayushchie/movalis-amp-15mg-15ml-n5-67_20078/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/mukosat-amp-10-1ml-n10-84_16578/",
                "https://krasnodar.social-apteka.ru/catalog/kat/osteokoll-implantat-kollagen-d-periartikulyarnogo-vved-2ml-n5-guna-70_34085377/",
                "https://krasnodar.social-apteka.ru/catalog/kat/pleksatron-kollagen-dvnutrisustav-i-periart-vved-2ml-n5-guna-96_34077275/",
                "https://krasnodar.social-apteka.ru/catalog/kat/ripart-long-sr-vo-dzameshch-sinov-jidk-20mgml-2ml-shpric-n1-ingal-70_32534640/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/ripart-long-sr-vo-dzameshch-sinovialnoy-jidkosti-20mgml-shpric-3ml-n1-rossiya-18_71697/",
                "https://krasnodar.social-apteka.ru/catalog/kat/ripart-forte-sr-vo-dlya-zameshcheniya-sinovialnoy-jidkosti-15mgml-shpric-3ml-100_34077342/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/rumalon-amp-1ml-n10-39_24853/",
                "https://krasnodar.social-apteka.ru/catalog/gomeopatiya/traumel-s-amp-22ml-n5-44_11979/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-1-2ml-n1-77_33430/",
                "https://krasnodar.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-15-2ml-n1-38_34995/",
                "https://krasnodar.social-apteka.ru/catalog/kat/fleksotron-kross-implantant-din-60mg3ml-sayvijn-bayotek-6_32534636/",
                "https://krasnodar.social-apteka.ru/catalog/kat/fleksotron-solo-implant-din-22-22mgml-2ml-sistema-plyus-20_33579271/",
                "https://krasnodar.social-apteka.ru/catalog/kat/fleksotron-ultra-implant-din-25-25mgml-48ml-albomed-63_33593771/",
                "https://krasnodar.social-apteka.ru/catalog/kat/hronotron-implantat-inekc-gel-dlya-vsust-vved-20mgml-2ml-n1-mastelli-61_33593758/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/ameloteks-r-r-d-in-1-5ml-n5-soteks_33449/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-r-r-dvnutrisust-vved-2ml-2_1549818/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-plyus-r-r-dvnutrisust-vved-2ml-86_1549819/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-forte-r-r-dvnutrisust-vved-shpric-3ml-53_29463/",
                "https://majkop.social-apteka.ru/catalog/kat/armaviskon-hondro-protez-sinovialnoy-jidkosti-3ml-n1-groteks-7_34113316/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/artogistan-r-r-din-100mgml-2ml-n10-41_28657/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/genitron-r-r-din-10mgml-15ml-n5-74_27287/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/gialurom-r-r-vsustav-shpric-15-2ml-n1-90_38239/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/gialurom-cs-vsustav-shpric-15-3ml-n1-10_23499/",
                "https://majkop.social-apteka.ru/search_to_go/?q=%D0%94%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/inektran-r-r-din-100mgml-2ml-n10-95_27204/",
                "https://majkop.social-apteka.ru/catalog/protivovospalitelnye-sredstva-dlya-oporno-dvigatelnogo-apparata/meloksikam-r-r-din-10mgml-15ml-n5-100_8389805/",
                "https://majkop.social-apteka.ru/catalog/obezbolivayushchie/movalis-amp-15mg-15ml-n5-67_20078/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/mukosat-amp-10-1ml-n10-84_16578/",
                "https://majkop.social-apteka.ru/catalog/kat/osteokoll-implantat-kollagen-d-periartikulyarnogo-vved-2ml-n5-guna-70_34085377/",
                "https://majkop.social-apteka.ru/catalog/kat/pleksatron-kollagen-dvnutrisustav-i-periart-vved-2ml-n5-guna-96_34077275/",
                "https://majkop.social-apteka.ru/catalog/kat/ripart-long-sr-vo-dzameshch-sinov-jidk-20mgml-2ml-shpric-n1-ingal-70_32534640/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/ripart-long-sr-vo-dzameshch-sinovialnoy-jidkosti-20mgml-shpric-3ml-n1-rossiya-18_71697/",
                "https://majkop.social-apteka.ru/catalog/kat/ripart-forte-sr-vo-dlya-zameshcheniya-sinovialnoy-jidkosti-15mgml-shpric-3ml-100_34077342/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/rumalon-amp-1ml-n10-39_24853/",
                "https://majkop.social-apteka.ru/catalog/gomeopatiya/traumel-s-amp-22ml-n5-44_11979/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-1-2ml-n1-77_33430/",
                "https://majkop.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-15-2ml-n1-38_34995/",
                "https://majkop.social-apteka.ru/catalog/kat/fleksotron-kross-implantant-din-60mg3ml-sayvijn-bayotek-6_32534636/",
                "https://majkop.social-apteka.ru/catalog/kat/fleksotron-solo-implant-din-22-22mgml-2ml-sistema-plyus-20_33579271/",
                "https://majkop.social-apteka.ru/catalog/kat/fleksotron-ultra-implant-din-25-25mgml-48ml-albomed-63_33593771/",
                "https://majkop.social-apteka.ru/catalog/kat/hronotron-implantat-inekc-gel-dlya-vsust-vved-20mgml-2ml-n1-mastelli-61_33593758/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/ameloteks-r-r-d-in-1-5ml-n5-soteks_33449/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-r-r-dvnutrisust-vved-2ml-2_1549818/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-plyus-r-r-dvnutrisust-vved-2ml-86_1549819/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/armaviskon-forte-r-r-dvnutrisust-vved-shpric-3ml-53_29463/",
                "https://stavropol.social-apteka.ru/catalog/kat/armaviskon-hondro-protez-sinovialnoy-jidkosti-3ml-n1-groteks-7_34113316/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/artogistan-r-r-din-100mgml-2ml-n10-41_28657/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/genitron-r-r-din-10mgml-15ml-n5-74_27287/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/gialurom-r-r-vsustav-shpric-15-2ml-n1-90_38239/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/gialurom-cs-vsustav-shpric-15-3ml-n1-10_23499/",
                "https://stavropol.social-apteka.ru/search_to_go/?q=%D0%94%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/inektran-r-r-din-100mgml-2ml-n10-95_27204/",
                "https://stavropol.social-apteka.ru/catalog/protivovospalitelnye-sredstva-dlya-oporno-dvigatelnogo-apparata/meloksikam-r-r-din-10mgml-15ml-n5-100_8389805/",
                "https://stavropol.social-apteka.ru/catalog/obezbolivayushchie/movalis-amp-15mg-15ml-n5-67_20078/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/mukosat-amp-10-1ml-n10-84_16578/",
                "https://stavropol.social-apteka.ru/catalog/kat/osteokoll-implantat-kollagen-d-periartikulyarnogo-vved-2ml-n5-guna-70_34085377/",
                "https://stavropol.social-apteka.ru/catalog/kat/pleksatron-kollagen-dvnutrisustav-i-periart-vved-2ml-n5-guna-96_34077275/",
                "https://stavropol.social-apteka.ru/catalog/kat/ripart-long-sr-vo-dzameshch-sinov-jidk-20mgml-2ml-shpric-n1-ingal-70_32534640/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/ripart-long-sr-vo-dzameshch-sinovialnoy-jidkosti-20mgml-shpric-3ml-n1-rossiya-18_71697/",
                "https://stavropol.social-apteka.ru/catalog/kat/ripart-forte-sr-vo-dlya-zameshcheniya-sinovialnoy-jidkosti-15mgml-shpric-3ml-100_34077342/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/rumalon-amp-1ml-n10-39_24853/",
                "https://stavropol.social-apteka.ru/catalog/gomeopatiya/traumel-s-amp-22ml-n5-44_11979/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-1-2ml-n1-77_33430/",
                "https://stavropol.social-apteka.ru/catalog/bolezni-sustavov/fermatron-shpric-15-2ml-n1-38_34995/",
                "https://stavropol.social-apteka.ru/catalog/kat/fleksotron-kross-implantant-din-60mg3ml-sayvijn-bayotek-6_32534636/",
                "https://stavropol.social-apteka.ru/catalog/kat/fleksotron-solo-implant-din-22-22mgml-2ml-sistema-plyus-20_33579271/",
                "https://stavropol.social-apteka.ru/catalog/kat/fleksotron-ultra-implant-din-25-25mgml-48ml-albomed-63_33593771/",
                "https://stavropol.social-apteka.ru/catalog/kat/hronotron-implantat-inekc-gel-dlya-vsust-vved-20mgml-2ml-n1-mastelli-61_33593758/"]
            pages = {}
            prep = []
            for i in range(len(linklist)):
                respone = requests.get(linklist[i])
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
                                'title': item.find("h1", id="brand").text.strip(),
                                'price': item.find("span", class_="product-order__price").text.replace(' ', ''),
                                'link': linklist[i],
                                'city': item.find('a', class_='vr-template__link').text.strip()
                            }
                        )
                except:
                    print("")

            print(prep)

            with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\SocialApteka_{date}.csv", 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'], name, item['link'], item["city"], item['price']])
    except:
        print("error SocialApteka")


    try:
        class stolichki(object):
            URL = "https://stolichki.ru/"
            HEADERS = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
            }

            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            name = "Столички"

            linklist = ["https://stolichki.ru/search?name=%D0%90%D0%B4%D0%B0%D0%BD%D1%82",
                        "https://stolichki.ru/search?name=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
                        "https://stolichki.ru/search?name=%D0%90%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://stolichki.ru/search?name=%D0%90%D1%82%D1%80%D0%B8+%D0%B8%D0%BD%D0%B6",
                        "https://stolichki.ru/search?name=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://stolichki.ru/search?name=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA+%D0%BE%D1%80%D1%82%D0%BE",
                        "https://stolichki.ru/search?name=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD+%D1%84%D0%BB%D1%8E%D0%B8%D0%B4",
                        "https://stolichki.ru/search?name=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
                        "https://stolichki.ru/search?name=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB",
                        "https://stolichki.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD+%D1%84%D0%B8%D0%B4%D0%B8%D1%8F",
                        "https://stolichki.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://stolichki.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://stolichki.ru/search?name=%D0%93%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
                        "https://stolichki.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC+%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C",
                        "https://stolichki.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81",
                        "https://stolichki.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE",
                        "https://stolichki.ru/search?name=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82",
                        "https://stolichki.ru/search?name=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
                        "https://stolichki.ru/search?name=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD",
                        "https://stolichki.ru/search?name=%D0%B4%D0%B8%D0%B0%D1%80%D1%82",
                        "https://stolichki.ru/search?name=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                        "https://stolichki.ru/search?name=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD",
                        "https://stolichki.ru/search?name=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://stolichki.ru/search?name=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD",
                        "https://stolichki.ru/search?name=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD",
                        "https://stolichki.ru/search?name=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB",
                        "https://stolichki.ru/search?name=%D0%BE%D1%81%D1%82+%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD",
                        "https://stolichki.ru/search?name=%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB",
                        "https://stolichki.ru/search?name=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D0%B8%D0%BD%D1%82%D1%80%D0%B0",
                        "https://stolichki.ru/search?name=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://stolichki.ru/search?name=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81",
                        "https://stolichki.ru/search?name=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
                        "https://stolichki.ru/search?name=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
                        "https://stolichki.ru/search?name=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA",
                        "https://stolichki.ru/search?name=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB",
                        "https://stolichki.ru/search?name=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D0%BE%D1%80%D0%BC",
                        "https://stolichki.ru/search?name=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
                        "https://stolichki.ru/search?name=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C",
                        "https://stolichki.ru/search?name=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://stolichki.ru/search?name=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://stolichki.ru/search?name=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81",
                        "https://stolichki.ru/search?name=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
                        "https://stolichki.ru/search?name=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                        "https://stolichki.ru/search?name=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0",
                        "https://stolichki.ru/search?name=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
                        "https://stolichki.ru/search?name=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81",
                        "https://stolichki.ru/search?name=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://stolichki.ru/search?name=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD",
                        "https://stolichki.ru/search?name=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC",
                        "https://stolichki.ru/search?name=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD",
                        "https://stolichki.ru/search?name=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
                        "https://stolichki.ru/search?name=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81+%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
                        "https://stolichki.ru/search?name=%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA",
                        "https://stolichki.ru/search?name=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                        "https://stolichki.ru/search?name=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF",
                        "https://stolichki.ru/search?name=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4",
                        "https://stolichki.ru/search?name=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF",
                        "https://stolichki.ru/search?name=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
                        "https://stolichki.ru/search?name=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
                        "https://stolichki.ru/search?name=%D0%B4%D0%BE%D0%BD%D0%B0",
                        "https://stolichki.ru/search?name=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
                        "https://stolichki.ru/search?name=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD",
                        "https://stolichki.ru/search?name=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
                        "https://stolichki.ru/search?name=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5+%D0%B1%D0%B8%D0%BE",
                        "https://stolichki.ru/search?name=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4+%D0%B0%D1%80%D1%82%D1%80%D0%BE",
                        "https://stolichki.ru/search?name=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB",
                        "https://stolichki.ru/search?name=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0+%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82",
                        "https://stolichki.ru/search?name=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0",
                        "https://stolichki.ru/search?name=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82",
                        "https://stolichki.ru/search?name=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82",
                        "https://stolichki.ru/search?name=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80+%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC",
                        "https://stolichki.ru/search?name=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4",
                        "https://stolichki.ru/search?name=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
                        "https://stolichki.ru/search?name=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                        "https://stolichki.ru/search?name=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                        "https://stolichki.ru/search?name=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
                        "https://stolichki.ru/search?name=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
            pages = {}
            prep = []

            options = webdriver.FirefoxOptions()
            options.set_preference("dom.webdriver.enabled", False)
            options.headless = True

            for i in range(len(linklist)):
                try:
                    driver = webdriver.Firefox(executable_path=r"C:\Users\Danil\Desktop\Python\Apteka\workers\geckodriver")
                    time.sleep(15)
                    driver.get(linklist[i])
                    print(i)

                    with open("seleniumPage.html", "w",  encoding='utf-8') as file:
                        file.write(driver.page_source)
                except Exception as ex:
                    print(ex)
                finally:
                    driver.close()
                    driver.quit()

                with open("seleniumPage.html",  encoding='utf-8') as file:
                    src = file.read()

                soup = BeautifulSoup(src, 'html.parser')
                items = soup.find_all("div", class_="product-item")
                if not items:
                    print("не туда")

                try:
                    for item in items:
                        prep.append(
                            {
                                'title': item.find("p", class_="product-title").find("a").text.strip(),
                                'price': item.find("div", class_="product-price").find("p").text.strip(),
                                'link': linklist[i]
                            }
                        )
                except:
                    print("Нет")

            print(prep)
            with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\stolichki{date}.csv", 'w', newline='',  encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'], name, item['link'], 'Москва', item['price']])
    except:
        print("error Stolichki")


    try:
        class zdorovRu(object):
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
                with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\ZdorovRu_{date}.csv", 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow(('Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки',
                                     'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'))
                    for item in prep:
                        writer.writerow([date, '', item['title'], name, item['link'], cookie['name'], item['price']])
    except:
        print("error ZdorovRu")


    try:
        class zhivika(object):
            URL = "https://zhivika.ru/"
            HEADERS = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
            }

            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            name = "Живика"

            linklist = [
                "https://zhivika.ru/search/resultPage?searchString=%D0%90%D0%BC%D0%B5%D0%BB%D0%BE%D%82%D0%B5%D0%BA%D1%81",
                "https://zhivika.ru/search/resultPage?searchString=%D0%90%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD",
                "https://zhivika.ru/search/resultPage?searchString=%D0%90%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD",
                "https://zhivika.ru/search/resultPage?searchString=%D0%92%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81",
                "https://zhivika.ru/search/resultPage?searchString=%D0%93%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD",
                "https://zhivika.ru/search/resultPage?searchString=%D0%93%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80",
                "https://zhivika.ru/search/resultPage?searchString=%D0%93%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC",
                "https://zhivika.ru/search/resultPage?searchString=%D0%94%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD",
                "https://zhivika.ru/search/resultPage?searchString=%D0%98%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD",
                "https://zhivika.ru/search/resultPage?searchString=%D0%9C%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC",
                "https://zhivika.ru/search/resultPage?searchString=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81",
                "https://zhivika.ru/search/resultPage?searchString=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82",
                "https://zhivika.ru/search/resultPage?searchString=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB",
                "https://zhivika.ru/search/resultPage?searchString=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                "https://zhivika.ru/search/resultPage?searchString=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82",
                "https://zhivika.ru/search/resultPage?searchString=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD",
                "https://zhivika.ru/search/resultPage?searchString=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA",
                "https://zhivika.ru/search/resultPage?searchString=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C",
                "https://zhivika.ru/search/resultPage?searchString=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD",
                "https://zhivika.ru/search/resultPage?searchString=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                "https://zhivika.ru/search/resultPage?searchString=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD",
                "https://zhivika.ru/search/resultPage?searchString=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD",
                "https://zhivika.ru/search/resultPage?searchString=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD",
                "https://zhivika.ru/search/resultPage?searchString=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81",
                "https://zhivika.ru/search/resultPage?searchString=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82"]
            pages = {}
            prep = []

            options = webdriver.FirefoxOptions()
            options.set_preference("dom.webdriver.enabled", False)
            options.headless = True

            for i in range(len(linklist)):
                try:
                    driver = webdriver.Firefox(executable_path=r"C:\Users\Danil\Desktop\Python\Apteka\workers\geckodriver")
                    time.sleep(15)
                    driver.get(linklist[i])
                    print(i)

                    with open("seleniumPage.html", "w",  encoding='utf-8') as file:
                        file.write(driver.page_source)
                except Exception as ex:
                    print(ex)
                finally:
                    driver.close()
                    driver.quit()

                with open("seleniumPage.html",  encoding='utf-8') as file:
                    src = file.read()

                soup = BeautifulSoup(src, 'html.parser')
                items = soup.find_all("a", class_="product-tile__item")
                if not items:
                    print("не туда")

                # берем данные с каждой карточки
                try:
                    for item in items:
                        prep.append(
                            {
                                'title': item.find("span", class_="product-tile__item-title").text.strip(),
                                'price': item.find("span", class_="product-tile__item-price--price").text.strip(),
                                'link': linklist[i]
                            }
                        )
                except:
                    print("Нет")

            print(prep)
            with open(rf"C:\Users\A.Shchukin\OneDrive - IT24x7\001. BI\001. PowerBI\03. Парсер цен\01. Исходники от парсера\zhivika{date}.csv", 'w', newline='',  encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'], name, item['link'], 'Живика', item['price']])
    except:
        print("error zhivika")


schedule.every().day.at("00:08").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)