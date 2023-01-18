import time
import requests
from bs4 import BeautifulSoup
import csv
import datetime
from selenium import webdriver
import schedule
import random

# РАБОТАЕТ ВЕРНО НО САЙТ БЛОКИРУЕТ ПОСЛЕ НЕСКОЛЬКИХ ИТЕРАЦИЙ ЦИКЛА

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")

HOST = "https://apteka.ru/"
URL = "https://apteka.ru/product/"
agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (X11; Linux i686; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Linux x86_64; rv:85.0) Gecko/20100102 Firefox/90.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 OPR/77.0.4054.254",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 OPR/77.0.4054.254",
]

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    "sec-ch-ua-mobile": "?0",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
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
    respone = requests.get(linklist[i], headers=headers)
    html = respone.text
    print(html)
    time.sleep(random.uniform(1, 6))


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
with open(rf"C:\Users\danil\OneDrive\Документы\Python\Аптечка\Результаты парсинга\AptekaRu_{date}.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        ['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС',
         'Ссылка на препарат', 'Город', 'Цена'])
    for item in prep:
        writer.writerow([date, '', item['title'], name, item['link'], 'Москва', item['price']])