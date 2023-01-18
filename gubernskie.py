import time
import requests
from bs4 import BeautifulSoup
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# РАБОТАЕТ КАК НАДО

class gubernskieApteki(object):
            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y")

            URL = "https://24farmacia.ru/"
            HEADERS = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
            }

            name = "Губернские аптеки"

            linklist = ["https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D0%25B4%25D0%25B0%25D0%25BD%25D1%2582",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D0%25BC%25D0%25B0%25D0%25B2%25D0%25B8%25D1%2581%25D0%25BA%25D0%25BE%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B8%25D1%2581%25D0%25BA",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2582%25D1%2580%25D0%25B8%2520%25D0%25B8%25D0%25BD%25D0%25B6",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B1%25D0%25B5%25D0%25BB%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B1%25D0%25B8%25D0%25BE%25D0%25B2%25D0%25B8%25D1%2581%25D0%25BA%2520%25D0%25BE%25D1%2580%25D1%2582%25D0%25BE",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B1%25D0%25B8%25D0%25BE%25D0%25BF%25D0%25BE%25D1%2580%25D1%2582",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B2%25D0%25B5%25D1%2580%25D1%2581%25D0%25B0%25D0%25BD%2520%25D1%2584%25D0%25BB%25D1%258E%25D0%25B8%25D0%25B4",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B2%25D0%25B8%25D1%2581%25D0%25BA%25D0%25BE%25D0%25BF%25D0%25BB%25D1%258E%25D1%2581",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D0%25B3%25D0%25B0%25D0%25BD%2520%25D1%2584%25D0%25B8%25D0%25B4%25D0%25B8%25D1%258F",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D0%25BE%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D1%2583%25D0%25B0%25D0%25BB%25D1%258C%2520%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D1%2583%25D1%2580%25D0%25BE%25D0%25BC",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D1%2583%25D1%2584%25D0%25BE%25D1%2580%25D0%25BC%2520%25D1%2581%25D0%25B8%25D0%25BD%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BB%25D1%258C",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D1%258E%25D0%25BA%25D1%2581",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BF%25D1%2580%25D0%25BE",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D1%2581%25D1%2582%25D0%25B0%25D1%2582",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D1%2580%25D1%2583%25D0%25B0%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25BE%25D1%2583-%25D0%25BE%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B4%25D0%25B8%25D0%25B0%25D1%2580%25D1%2582",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B4%25D1%258C%25D1%258E%25D1%2580%25D0%25B0%25D0%25BB%25D0%25B0%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B6%25D0%25B0%25D0%25BB%25D0%25B8%25D1%2580%25D0%25B5%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B8%25D0%25BD%25D1%2582%25D1%2580%25D0%25B0%25D0%25B4%25D0%25B6%25D0%25B5%25D0%25BA%25D1%2582",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B8%25D0%25BD%25D1%2582%25D1%2580%25D0%25B0%25D0%25B4%25D0%25B6%25D0%25B5%25D0%25BA%25D1%2582",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BA%25D1%2580%25D0%25B5%25D1%2581%25D0%25BF%25D0%25B8%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BD%25D0%25BE%25D0%25BB%25D1%2582%25D1%2580%25D0%25B5%25D0%25BA%25D1%2581%25D0%25B8%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BE%25D1%2580%25D1%2582%25D0%25BE%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BE%25D1%2581%25D1%2582%2520%25D1%2582%25D0%25B5%25D0%25BD%25D0%25B4%25D0%25BE%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BE%25D1%2581%25D1%2582%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25BB",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BF%25D1%2580%25D0%25BE%25D1%2584%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2581%2520%25D0%25B8%25D0%25BD%25D1%2582%25D1%2580%25D0%25B0",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2580%25D0%25B5%25D0%25B2%25D0%25B8%25D1%2581%25D0%25BA",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2580%25D0%25B5%25D0%25BD%25D0%25B5%25D1%2585%25D0%25B0%25D0%25B2%25D0%25B8%25D1%2581",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2580%25D0%25B8%25D0%25BF%25D0%25B0%25D1%2580%25D1%2582",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2580%25D1%2583%25D1%2581%25D0%25B2%25D0%25B8%25D1%2581%25D0%25BA",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2581%25D0%25B5%25D1%2580%25D1%2582%25D0%25BE%25D0%25B1%25D0%25B5%25D0%25BA",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2581%25D0%25B8%25D0%25BD%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE%25D0%25BB",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2581%25D0%25B8%25D0%25BD%25D0%25BE%25D0%25BA%25D0%25BE%25D1%2580%25D0%25BC",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2581%25D1%2583%25D0%25BF%25D0%25BB%25D0%25B0%25D0%25B7%25D0%25B8%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2581%25D1%2584%25D0%25B5%25D1%2580%25D0%25BE%25D0%25B3%25D0%25B5%25D0%25BB%25D1%258C",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2584%25D0%25B5%25D1%2580%25D0%25BC%25D0%25B0%25D1%2582%25D1%2580%25D0%25BE%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2584%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2581%25D0%25BE%25D1%2582%25D1%2580%25D0%25BE%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25B0%25D0%25B9%25D0%25BC%25D0%25BE%25D0%25B2%25D0%25B8%25D1%2581",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25B0%25D0%25B9%25D0%25BB%25D1%2583%25D0%25B1%25D1%2580%25D0%25B8%25D0%25BA%25D1%2581",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D1%2580%25D0%25BE%25D0%25BD%25D0%25BE%25D1%2582%25D1%2580%25D0%25BE%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%258D%25D1%2583%25D1%2584%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2581%25D0%25B0",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BB%25D0%25B8%25D1%2581",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D0%25BC%25D0%25B5%25D0%25BB%25D0%25BE%25D1%2582%25D0%25B5%25D0%25BA%25D1%2581",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D0%25B5%25D0%25BB%25D0%25BE%25D0%25BA%25D1%2581%25D0%25B8%25D0%25BA%25D0%25B0%25D0%25BC",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE%25D0%25B7%25D0%25B0%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D0%25B5%25D0%25BB%25D0%25BE%25D0%25BA%25D1%2581%25D0%25B8%25D0%25BA%25D0%25B0%25D0%25BC%2520%25D0%25B1%25D1%2583%25D1%2584%25D1%2583%25D1%2581",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%258D%25D0%25BB%25D0%25BE%25D0%25BA%25D1%2581-%25D1%2581%25D0%25BE%25D0%25BB%25D0%25BE%25D1%2584%25D0%25B0%25D1%2580%25D0%25BC",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D0%25BE%25D0%25B2%25D0%25B0%25D1%2581%25D0%25B8%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B5%25D0%25BD%25D0%25B8%25D1%2582%25D1%2580%25D0%25BE%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D0%25B5%25D0%25BB%25D0%25BE%25D1%2584%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2581%2520%25D1%2580%25D0%25BE%25D0%25BC%25D1%2584%25D0%25B0%25D1%2580%25D0%25BC",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D0%25B5%25D0%25BB%25D0%25B1%25D0%25B5%25D0%25BA",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B1%25D0%25B8-%25D0%25BA%25D1%2581%25D0%25B8%25D0%25BA%25D0%25B0%25D0%25BC",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D0%25BB%25D1%2584%25D0%25BB%25D1%2583%25D1%2582%25D0%25BE%25D0%25BF",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25BE%25D0%25BD%25D0%25B4%25D1%2580%25D0%25BE%25D0%25B3%25D0%25B0%25D1%2580%25D0%25B4",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B4%25D1%2580%25D0%25B0%25D1%2581%25D1%2582%25D0%25BE%25D0%25BF",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BC%25D1%2583%25D0%25BA%25D0%25BE%25D1%2581%25D0%25B0%25D1%2582",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2580%25D1%2583%25D0%25BC%25D0%25B0%25D0%25BB%25D0%25BE%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B4%25D0%25BE%25D0%25BD%25D0%25B0",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B8%25D0%25BD%25D1%258A%25D0%25B5%25D0%25BA%25D1%2582%25D1%2580%25D0%25B0%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25BE%25D0%25BD%25D0%25B4%25D1%2580%25D0%25BE%25D0%25BB%25D0%25BE%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D1%2582%25D0%25BE%25D0%25B3%25D0%25B8%25D1%2581%25D1%2582%25D0%25B0%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D0%25BC%25D0%25B1%25D0%25B5%25D0%25BD%25D0%25B5%2520%25D0%25B1%25D0%25B8%25D0%25BE",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2581%25D1%2583%25D1%2581%25D1%2582%25D0%25B0%25D0%25B3%25D0%25B0%25D1%2580%25D0%25B4%2520%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D1%2581%25D1%2582%25D1%2580%25D0%25B0%25D0%25B4%25D0%25BE%25D0%25BB",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25BE%25D0%25BD%25D0%25B4%25D1%2580%25D0%25BE%25D0%25B8%25D1%2582%25D0%25B8%25D0%25BD%25D0%25B0%2520%25D1%2581%25D1%2583%25D0%25BB%25D1%258C%25D1%2584%25D0%25B0%25D1%2582",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%258D%25D0%25BB%25D1%258C%25D0%25B1%25D0%25BE%25D0%25BD%25D0%25B0",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25BE%25D0%25BD%25D1%2581%25D0%25B0%25D1%2582",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25BE%25D0%25B4%25D0%25B6%25D0%25B5%25D0%25BA%25D1%2582",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B0%25D1%2580%25D1%2582%25D1%2580%25D0%25B0%25D0%25B2%25D0%25B8%25D1%2580%2520%25D0%25B8%25D0%25BD%25D0%25BA%25D0%25B0%25D0%25BC%25D1%2584%25D0%25B0%25D1%2580%25D0%25BC",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25BE%25D0%25BD%25D0%25B4%25D1%2580%25D0%25BE%25D0%25BA%25D1%2581%25D0%25B8%25D0%25B4",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25B3%25D0%25B8%25D0%25B0%25D0%25BB%25D1%2580%25D0%25B8%25D0%25BF%25D0%25B0%25D0%25B9%25D0%25B5%25D1%2580",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BE%25D1%2581%25D1%2582%25D0%25B5%25D0%25BE%25D0%25BA%25D0%25BE%25D0%25BB%25D0%25BB",
                        "https://24farmacia.ru/apteki/search/?q=%25D0%25BF%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2581%25D0%25B0%25D1%2582%25D1%2580%25D0%25BE%25D0%25BD",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2582%25D1%2580%25D0%25B0%25D1%2583%25D0%25BC%25D0%25B5%25D0%25BB%25D1%258C",
                        "https://24farmacia.ru/apteki/search/?q=%25D1%2585%25D0%25B0%25D0%25B9%25D0%25BB%25D1%2583%25D0%25B1%25D1%2580%25D0%25B8%25D0%25BA%25D1%2581"]
            pages = {}
            prep = []
            for i in range(len(linklist)):
                respone = requests.get(linklist[i])
                html = respone.text
                print(i)
                print(html)

                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all("div", class_="product-card")
                if not items:
                    print("не туда")

                try:
                    for item in items:
                        prep.append(
                            {
                                'title': item.find("a", class_="product-card__info-title").text.strip(),
                                'price': item.find("div", class_="product-card__price").find("span").text.strip(),
                                'link': linklist[i]
                            }
                        )
                except:
                    print("Нет в наличии")

            print(prep)
            with open(rf"C:\Users\danil\OneDrive\Документы\Python\Аптечка\Результаты парсинга\gubernskiyApteki_{date}.csv", 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
                     'Ссылка на препарат', 'Город', 'Цена'])
                for item in prep:
                    writer.writerow([date, '', item['title'], name, item['link'], 'Красноярск', item['price']])