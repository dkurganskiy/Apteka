import requests
from bs4 import BeautifulSoup
import csv
import datetime
from random import choice
from time import sleep
from random import uniform


URL = "https://aptekiplus.ru/"


useragents = open('../workers/useragent.txt').read().split('\n')
proxies = open('../workers/proxy').read().split('\n')


now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")


name = " Имплозия"


linklist = ["https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D0%B4%D0%B0%D0%BD%D1%82/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%81%D0%BA/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B1%D0%B5%D0%BB%D0%B0%D1%80%D1%82%D1%80%D0%BE/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B1%D0%B8%D0%BE%D0%B2%D0%B8%D1%81%D0%BA%20%D0%BE%D1%80%D1%82%D0%BE/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B1%D0%B8%D0%BE%D0%BF%D0%BE%D1%80%D1%82/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B2%D0%B5%D1%80%D1%81%D0%B0%D0%BD%20%D1%84%D0%BB%D1%8E%D0%B8%D0%B4/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D0%BF%D0%BB%D1%8E%D1%81/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B2%D0%B8%D1%81%D0%BA%D0%BE%D1%81%D0%B8%D0%BB/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B3%D0%B8%D0%B0%D0%BB%D0%B3%D0%B0%D0%BD%20%D1%84%D0%B8%D0%B4%D0%B8%D1%8F/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B3%D0%B8%D0%B0%D0%BB%D0%BE%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D0%B0%D0%BB%D1%8C%20%D0%B0%D1%80%D1%82%D1%80%D0%BE/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%80%D0%BE%D0%BC/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B3%D0%B8%D0%B0%D0%BB%D1%83%D1%84%D0%BE%D1%80%D0%BC%20%D1%81%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D0%BB%D1%8C/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B3%D0%B8%D0%B0%D0%BB%D1%8E%D0%BA%D1%81/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B3%D0%B8%D0%B0%D0%BF%D1%80%D0%BE/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B3%D0%B8%D0%B0%D1%81%D1%82%D0%B0%D1%82/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B3%D0%B8%D1%80%D1%83%D0%B0%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B3%D0%BE%D1%83-%D0%BE%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B4%D0%B8%D0%B0%D1%80%D1%82/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B4%D1%8C%D1%8E%D1%80%D0%B0%D0%BB%D0%B0%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B6%D0%B0%D0%BB%D0%B8%D1%80%D0%B5%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B8%D0%BD%D1%82%D1%80%D0%B0%D0%B4%D0%B6%D0%B5%D0%BA%D1%82/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BA%D1%80%D0%B5%D1%81%D0%BF%D0%B8%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BD%D0%BE%D0%BB%D1%82%D1%80%D0%B5%D0%BA%D1%81%D0%B8%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BE%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D0%B0%D0%BB/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BE%D1%81%D1%82%20%D1%82%D0%B5%D0%BD%D0%B4%D0%BE%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BE%D1%81%D1%82%D0%B5%D0%BD%D0%B8%D0%BB/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BF%D1%80%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D0%B8%D0%BD%D1%82%D1%80%D0%B0/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%80%D0%B5%D0%B2%D0%B8%D1%81%D0%BA/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%80%D0%B5%D0%BD%D0%B5%D1%85%D0%B0%D0%B2%D0%B8%D1%81/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%80%D0%B8%D0%BF%D0%B0%D1%80%D1%82/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%80%D1%83%D1%81%D0%B2%D0%B8%D1%81%D0%BA/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%81%D0%B5%D1%80%D1%82%D0%BE%D0%B1%D0%B5%D0%BA/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%81%D0%B8%D0%BD%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%BB/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%81%D0%B8%D0%BD%D0%BE%D0%BA%D1%80%D0%BE%D0%BC/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%81%D1%83%D0%BF%D0%BB%D0%B0%D0%B7%D0%B8%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%81%D1%84%D0%B5%D1%80%D0%BE%D0%B3%D0%B5%D0%BB%D1%8C/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%84%D0%B5%D1%80%D0%BC%D0%B0%D1%82%D1%80%D0%BE%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%BE%D1%82%D1%80%D0%BE%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%85%D0%B0%D0%B9%D0%BC%D0%BE%D0%B2%D0%B8%D1%81/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%85%D1%80%D0%BE%D0%BD%D0%BE%D1%82%D1%80%D0%BE%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%8D%D1%83%D1%84%D0%BB%D0%B5%D0%BA%D1%81%D0%B0/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BC%D0%BE%D0%B2%D0%B0%D0%BB%D0%B8%D1%81/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D0%BC%D0%B5%D0%BB%D0%BE%D1%82%D0%B5%D0%BA%D1%81/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BC%D0%B5%D0%BB%D0%BE%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%8D%D0%BB%D0%BE%D0%BA%D1%81-%D1%81%D0%BE%D0%BB%D0%BE%D1%84%D0%B0%D1%80%D0%BC/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BC%D0%BE%D0%B2%D0%B0%D1%81%D0%B8%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B3%D0%B5%D0%BD%D0%B8%D1%82%D1%80%D0%BE%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BC%D0%B5%D0%BB%D0%BE%D1%84%D0%BB%D0%B5%D0%BA%D1%81%20%D1%80%D0%BE%D0%BC%D1%84%D0%B0%D1%80%D0%BC/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BC%D0%B5%D0%BB%D0%B1%D0%B5%D0%BA/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B1%D0%B8-%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%D0%BC/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D0%BB%D1%84%D0%BB%D1%83%D1%82%D0%BE%D0%BF/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B3%D0%B0%D1%80%D0%B4/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B4%D1%80%D0%B0%D1%81%D1%82%D0%BE%D0%BF/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BC%D1%83%D0%BA%D0%BE%D1%81%D0%B0%D1%82/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%80%D1%83%D0%BC%D0%B0%D0%BB%D0%BE%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B4%D0%BE%D0%BD%D0%B0/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%82%D1%80%D0%B0%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BB%D0%BE%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D1%80%D1%82%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5%20%D0%B1%D0%B8%D0%BE/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D0%BC%D0%B1%D0%B5%D0%BD%D0%B5%20%D0%B1%D0%B8%D0%BE/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%81%D1%83%D1%81%D1%82%D0%B0%D0%B3%D0%B0%D1%80%D0%B4%20%D0%B0%D1%80%D1%82%D1%80%D0%BE/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D1%80%D1%82%D1%80%D0%B0%D0%B4%D0%BE%D0%BB/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D1%82%D0%B8%D0%BD%D0%B0%20%D1%81%D1%83%D0%BB%D1%8C%D1%84%D0%B0%D1%82/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%8D%D0%BB%D1%8C%D0%B1%D0%BE%D0%BD%D0%B0/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%85%D0%BE%D0%BD%D1%81%D0%B0%D1%82/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B4%D0%B6%D0%B5%D0%BA%D1%82/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B0%D1%80%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%80%20%D0%B8%D0%BD%D0%BA%D0%B0%D0%BC%D1%84%D0%B0%D1%80%D0%BC/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%85%D0%BE%D0%BD%D0%B4%D1%80%D0%BE%D0%BA%D1%81%D0%B8%D0%B4/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%B3%D0%B8%D0%B0%D0%BB%D1%80%D0%B8%D0%BF%D0%B0%D0%B9%D0%B5%D1%80/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BE%D1%81%D1%82%D0%B5%D0%BE%D0%BA%D0%BE%D0%BB%D0%BB/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D0%BF%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D1%82%D1%80%D0%BE%D0%BD/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%82%D1%80%D0%B0%D1%83%D0%BC%D0%B5%D0%BB%D1%8C/", "https://aptekiplus.ru/search/%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/%D1%85%D0%B0%D0%B9%D0%BB%D1%83%D0%B1%D1%80%D0%B8%D0%BA%D1%81/"]
pages = {}
prep = []
for i in range(len(linklist)):
    proxy = {'http': 'http://' + choice(proxies)}
    useragent = {'User-Agents': choice(useragents)}
    sleep(15)
    respone = requests.get(linklist[i], proxies=proxy, headers=useragent)
    html = respone.text
    print(i)
    print(proxy)
    print(html)


    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("li", class_="")
    if not items:
        print("не туда")


    # берем данные с каждой карточки
    try:
        for item in items:
            prep.append(
                {
                'title': item.find("div", class_="search-title-wrap").find("a").text.strip(),
                'price': item.find("div", class_="active-price").text.strip(),
                'link': linklist[i]
                }
            )
    except:
        print("Нет")


print(prep)
with open(f"imploziya{date}.csv", 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
    for item in prep:
        writer.writerow([date, '', item['title'], name, item['link'], 'Москва', item['price']])


# Пока не понял, что за деф