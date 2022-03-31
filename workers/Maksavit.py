import requests
from bs4 import BeautifulSoup
import csv
import datetime
import schedule
import time



def job():
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


    linklist = ["https://maksavit.ru/searching/?queryString=%D0%B0%D0%B4%D0%B0%D0%BD%D1%82", "https://maksavit.ru/searching/?queryString=%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA", "https://maksavit.ru/searching/?queryString=%D0%90%D0%A2%D0%A0%D0%98%20%D0%98%D0%9D%D0%96", "https://maksavit.ru/searching/?queryString=%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE", "https://maksavit.ru/searching/?queryString=%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA%20%D0%BE%D1%80%D1%82%D0%BE", "https://maksavit.ru/searching/?queryString=%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82", "https://maksavit.ru/searching/?queryString=%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81", "https://maksavit.ru/searching/?queryString=%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB", "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C%20%D0%B0%D1%80%D1%82%D1%80%D0%BE", "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC", "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC", "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81", "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE", "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82", "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%B4%D0%B8%D0%B0%D1%80%D1%82", "https://maksavit.ru/searching/?queryString=%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82", "https://maksavit.ru/searching/?queryString=%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB", "https://maksavit.ru/searching/?queryString=%D0%BE%D1%81%D1%82%20%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BD%D0%B8%D0%BB", "https://maksavit.ru/searching/?queryString=%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D0%B8%D0%BD%D1%82%D1%80%D0%B0", "https://maksavit.ru/searching/?queryString=%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA", "https://maksavit.ru/searching/?queryString=%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81", "https://maksavit.ru/searching/?queryString=%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82", "https://maksavit.ru/searching/?queryString=%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA", "https://maksavit.ru/searching/?queryString=%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA", "https://maksavit.ru/searching/?queryString=%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB", "https://maksavit.ru/searching/?queryString=%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D1%80%D0%BE%D0%BC", "https://maksavit.ru/searching/?queryString=%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD", "https://maksavit.ru/searching/?queryString=%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C", "https://maksavit.ru/searching/?queryString=%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD", "https://maksavit.ru/searching/?queryString=%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD", "https://maksavit.ru/searching/?queryString=%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81", "https://maksavit.ru/searching/?queryString=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81", "https://maksavit.ru/searching/?queryString=%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD", "https://maksavit.ru/searching/?queryString=%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0", "https://maksavit.ru/searching/?queryString=%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81", "https://maksavit.ru/searching/?queryString=%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81", "https://maksavit.ru/searching/?queryString=%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC", "https://maksavit.ru/searching/?queryString=%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD", "https://maksavit.ru/searching/?queryString=%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC", "https://maksavit.ru/searching/?queryString=%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81", "https://maksavit.ru/searching/?queryString=%D0%BC%D0%B5%D0%BB%D1%8C%D0%B1%D0%B5%D0%BA", "https://maksavit.ru/searching/?queryString=%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC", "https://maksavit.ru/searching/?queryString=%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF", "https://maksavit.ru/searching/?queryString=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4", "https://maksavit.ru/searching/?queryString=%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF", "https://maksavit.ru/searching/?queryString=%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82", "https://maksavit.ru/searching/?queryString=%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%B4%D0%BE%D0%BD%D0%B0", "https://maksavit.ru/searching/?queryString=%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD", "https://maksavit.ru/searching/?queryString=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD", "https://maksavit.ru/searching/?queryString=%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5%20%D0%B1%D0%B8%D0%BE", "https://maksavit.ru/searching/?queryString=%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4%20%D0%B0%D1%80%D1%82%D1%80%D0%BE", "https://maksavit.ru/searching/?queryString=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB", "https://maksavit.ru/searching/?queryString=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0%20%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82", "https://maksavit.ru/searching/?queryString=%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0", "https://maksavit.ru/searching/?queryString=%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82", "https://maksavit.ru/searching/?queryString=%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B2%D0%B8%D1%80%20%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC", "https://maksavit.ru/searching/?queryString=%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4", "https://maksavit.ru/searching/?queryString=%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80", "https://maksavit.ru/searching/?queryString=%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB", "https://maksavit.ru/searching/?queryString=%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD", "https://maksavit.ru/searching/?queryString=%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C", "https://maksavit.ru/searching/?queryString=%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81"]
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
                        'price': item.find("div", class_="product-price__current-price").find("span").text.strip(),
                        'link': linklist[i]
                        }
                    )
                except:
                    print("not find")


            print(prep)


        with open(f"Maksavit_{date}.csv", 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
            for item in prep:
                writer.writerow([date, '', item['title'], name, item['link'], cookie['name'], item['price']])

schedule.every().day.at("12:21").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)


# Выводит по поиску все.

