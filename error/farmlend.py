import requests
from bs4 import BeautifulSoup
import csv
import datetime
from random import choice
from time import sleep
from random import uniform


now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")


useragents = open('../workers/useragent.txt').read().split('\n')
proxies = open('../workers/proxy').read().split('\n')


HOST = "https://farmlend.ru/"
URL = "https://farmlend.ru/moskva/product/"

cookies = [
    {"fl_tk": "584f150d81e315bf81e2aedb1441bf6dc08cd0beb2dfe8587dca45a1aadbf30fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22fl_tk%22%3Bi%3A1%3Bs%3A32%3A%22-SKahtwCrYJepqS7zAvGW7MFxhs-AmhR%22%3B%7D; advanced-frontend_v3=l6vspcfaoc131rdetjs6ofc8i5; viewedProductsIds=19b41f2a1b73416f362a0ed91fdffd90cc4d48d3821f19b81aa6806fe9497088a%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22viewedProductsIds%22%3Bi%3A1%3Ba%3A1%3A%7Bi%3A0%3Bi%3A41816%3B%7D%7D; _csrf-frontend=3b9e21f57f3fcdf61fa7cd043293cb299f123003058dbbab0102f3c59792453ba%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22WI2ycHQwHtxO48velOTtDvjY4aD31bbP%22%3B%7D; fillplaceVisible=true; lastCartProductsIds=a%3A0%3A%7B%7D"},
    {"fl_tk": "584f150d81e315bf81e2aedb1441bf6dc08cd0beb2dfe8587dca45a1aadbf30fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22fl_tk%22%3Bi%3A1%3Bs%3A32%3A%22-SKahtwCrYJepqS7zAvGW7MFxhs-AmhR%22%3B%7D; advanced-frontend_v3=l6vspcfaoc131rdetjs6ofc8i5; viewedProductsIds=19b41f2a1b73416f362a0ed91fdffd90cc4d48d3821f19b81aa6806fe9497088a%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22viewedProductsIds%22%3Bi%3A1%3Ba%3A1%3A%7Bi%3A0%3Bi%3A41816%3B%7D%7D; _csrf-frontend=3b9e21f57f3fcdf61fa7cd043293cb299f123003058dbbab0102f3c59792453ba%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22WI2ycHQwHtxO48velOTtDvjY4aD31bbP%22%3B%7D; fillplaceVisible=true; lastCartProductsIds=a%3A0%3A%7B%7D"},
    {"fl_tk": "584f150d81e315bf81e2aedb1441bf6dc08cd0beb2dfe8587dca45a1aadbf30fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22fl_tk%22%3Bi%3A1%3Bs%3A32%3A%22-SKahtwCrYJepqS7zAvGW7MFxhs-AmhR%22%3B%7D; advanced-frontend_v3=l6vspcfaoc131rdetjs6ofc8i5; viewedProductsIds=19b41f2a1b73416f362a0ed91fdffd90cc4d48d3821f19b81aa6806fe9497088a%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22viewedProductsIds%22%3Bi%3A1%3Ba%3A1%3A%7Bi%3A0%3Bi%3A41816%3B%7D%7D; _csrf-frontend=3b9e21f57f3fcdf61fa7cd043293cb299f123003058dbbab0102f3c59792453ba%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22WI2ycHQwHtxO48velOTtDvjY4aD31bbP%22%3B%7D; fillplaceVisible=true; lastCartProductsIds=a%3A0%3A%7B%7D"},
    {"fl_tk": "584f150d81e315bf81e2aedb1441bf6dc08cd0beb2dfe8587dca45a1aadbf30fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22fl_tk%22%3Bi%3A1%3Bs%3A32%3A%22-SKahtwCrYJepqS7zAvGW7MFxhs-AmhR%22%3B%7D; advanced-frontend_v3=l6vspcfaoc131rdetjs6ofc8i5; viewedProductsIds=19b41f2a1b73416f362a0ed91fdffd90cc4d48d3821f19b81aa6806fe9497088a%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22viewedProductsIds%22%3Bi%3A1%3Ba%3A1%3A%7Bi%3A0%3Bi%3A41816%3B%7D%7D; _csrf-frontend=3b9e21f57f3fcdf61fa7cd043293cb299f123003058dbbab0102f3c59792453ba%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22WI2ycHQwHtxO48velOTtDvjY4aD31bbP%22%3B%7D; fillplaceVisible=true; lastCartProductsIds=a%3A0%3A%7B%7D"},

]


name = "Фармленд"


linklist = ["https://farmlend.ru/moskva/product/41816", "https://farmlend.ru/moskva/product/283583", "https://farmlend.ru/moskva/product/283584", "https://farmlend.ru/moskva/product/286118", "https://farmlend.ru/moskva/product/324731", "https://farmlend.ru/moskva/product/286514", "https://farmlend.ru/moskva/product/286514", "https://farmlend.ru/moskva/product/305382", "https://farmlend.ru/moskva/product/75634", "https://farmlend.ru/moskva/product/235379", "https://farmlend.ru/moskva/product/1297", "https://farmlend.ru/moskva/product/273404", "https://farmlend.ru/moskva/product/294351", "https://farmlend.ru/moskva/product/212427", "https://farmlend.ru/moskva/product/304543", "https://farmlend.ru/moskva/product/304543", "https://farmlend.ru/moskva/product/324244", "https://farmlend.ru/moskva/product/309575", "https://farmlend.ru/moskva/product/244288", "https://farmlend.ru/moskva/product/31327", "https://farmlend.ru/moskva/product/31852", "https://farmlend.ru/moskva/product/31853", "https://farmlend.ru/moskva/product/31852", "https://farmlend.ru/moskva/product/324779", "https://farmlend.ru/moskva/product/323021", "https://farmlend.ru/moskva/product/324779", "https://farmlend.ru/moskva/product/322459"]
pages = {}

for cookie in cookies:
    prep = []
    for i in range(len(linklist)):
        proxy = {'http': 'http://' + choice(proxies)}
        useragent = {'User-Agents': choice(useragents)}
        respone = requests.get(linklist[i], cookies=cookie, headers=useragent, proxies=proxy)
        html = respone.text
        print(html)


        soup = BeautifulSoup(html, 'html.parser')
        items = soup.select("div", class_="container-fluid")
        if not items:
            print("не туда")

        try:
            for item in items:
                prep.append(
                    {
                    'title': item.find("h1", class_="title").text.strip(),
                    'price': item.find("div", class_="f-col-3").find("span").text.strip(),
                    'link': linklist[i]
                    }
                )
        except:
            print("Нет в наличии")

        sleep(uniform(0, 2))

    print(prep)
    with open(f"farmlend_{date}.csv", 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
        for item in prep:
            writer.writerow([date, '', item['title'], name, item['link'], '', item['price']])

#  Тех работы, запилить по поиску после ТР