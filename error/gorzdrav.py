import requests
from bs4 import BeautifulSoup
import csv
import datetime

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")

HOST = "https://gorzdrav.org/"
URL = "https://gorzdrav.org/category/lekarstva/"
HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"
}
cookies = [
    {"JSESSIONID": "CD75B5B37C542ACFB2251467A6B82846.accstorefront-847bfd87d6-2b4g5; gorzdrav-cart=cfc2d0fd-b373-4466-b9ae-62bd4c6edc8b; ROUTE=.accstorefront-847bfd87d6-2b4g5"},
]


name = "Горздрав"


linklist = ["https://gorzdrav.org/p/ameloteks-rr-dlja-v-m-vvedenija-amp-1-5ml-n5-29653/", "https://gorzdrav.org/p/armaviskon-1-sredstvo-dlja-vnutrisustavnogo-vvedenija-shpric-2-ml-2-sht-332100/", "https://gorzdrav.org/p/armaviskon-protez-sinov-zhti-shpric-12ml-198425/", "https://gorzdrav.org/p/armaviskon-forte-protez-sinovinalnoj-zhidkosti-shpric-d-sustavn-vveden-2-3-3ml-205057/", "https://gorzdrav.org/p/artogistan-rr-d-v-m-vv-0-1-ml-2ml-10-198442/", "https://gorzdrav.org/p/viskopljus-protez-sinovialnoj-zhidkosti-2ml-shpric-58554/", "https://gorzdrav.org/p/viskopljus-protez-sinovialnoj-zhidkosti-2ml-shpric-58554/", "https://gorzdrav.org/p/gialurom-rr-v-sust-vved-shpric-1-5-2ml-n1-52647/", "https://gorzdrav.org/p/gialurom-cs-rr-60mg-3ml-90mg-3ml-shpric-3ml-n1-61601/", "https://gorzdrav.org/p/djuralan-implantant-vjazkouprugij-steril-shpric-25980/", "https://gorzdrav.org/p/djuralan-implantant-vjazkouprugij-steril-shpric-25980/", "https://gorzdrav.org/p/ameloteks-rr-dlja-v-m-vvedenija-amp-1-5ml-n5-29653/", "https://gorzdrav.org/p/movalis-rr-d-in-15mg-1-5ml-amp-1-5ml-n5-49222/", "https://gorzdrav.org/p/mukosat-rr-d-in-amp-1ml-n10-52925/", "https://gorzdrav.org/p/osteokoll-implantat-kollagensoder-d-periartikuljarnogo-vveden-2ml-n5-300687/", "https://gorzdrav.org/p/pleksatron-implantat-kollagensoder-d-vnutrisustavn-i-periartikuljarnogo-vveden-2ml-n5-300686/", "https://gorzdrav.org/p/ripart-long-protez-shpric-d-s-vv-2-3ml1-206895/", "https://gorzdrav.org/p/ripart-forte-protez-sinovinalnoj-zhidkosti-shpric-d-sustavn-vveden-1-5-15mg-ml-3ml-n1-252004/", "https://gorzdrav.org/p/rumalon-rr-d-in-amp-1ml-n10-9082/", "https://gorzdrav.org/p/traumel-s-rr-d-in-2-2ml-n5-10304/", "https://gorzdrav.org/p/fermatron-rr-d-in-20mg-2ml-2ml-n1-23783/", "https://gorzdrav.org/p/fermatron-pljus-protez-sinovialnoj-zhti-1-5-2ml-40913/", "https://gorzdrav.org/p/fermatron-s-prot-d-in-2-3-69mg-3ml-1-51987/", "https://gorzdrav.org/p/fermatron-pljus-protez-sinovialnoj-zhti-1-5-2ml-40913/", "https://gorzdrav.org/p/fleksotron-solo-protez-sinovinalnoj-zhidkosti-shpric-d-vnutrisustavn-vveden-2-2-22mg-ml-2ml-n1-300684/", "https://gorzdrav.org/p/fleksotron-ultra-protez-sinovinalnoj-zhidkosti-shpric-d-vnutrisustavn-vveden-2-5-25mg-ml-4-8ml-n1-300683/", "https://gorzdrav.org/p/khronotron-implantat-na-osnove-polinukleot-d-vnutrisustavn-vveden-20mg-ml-2ml-n1-300685/", "https://gorzdrav.org/p/versan-protez-fljuid-2-5ml-1shpric-61504/", "https://gorzdrav.org/p/suplazin-protez-sinovinalnoj-zhidkosti-shpric-d-sustavn-vveden-20mg-2ml-19885/", "https://gorzdrav.org/p/intradzhekt-sredstvo-dlja-zameshhenija-sinovialnoj-zhidkosti-2-2-2ml-n1-shpric-252087/"]
pages = {}

for cookie in cookies:
    prep = []
    for i in range(len(linklist)):
        respone = requests.get(linklist[i], cookies=cookie)
        html = respone.text
        print(html)


        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all("div")
        if not items:
            print("не туда")

        try:
            for item in items:
                prep.append(
                    {
                    'title': item.find("div", class_="c-product__info").text.strip(),
                    'price': item.find("div", class_="c-product__specs-main").find("span", class_="js-price-value").text.strip(),
                    'link': linklist[i],
                    'name': item.find("span", class_="b-login-link i-fw-b").text.strip()
                    }
                )
        except:
            print("Нет в наличии")


    print(prep)
    with open(f"gorzdrav_{date}.csv", 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Дата', 'Наименование препарата как у нас', 'Наименование препарата как у аптеки', 'Наименование АС', 'Ссылка на препарат', 'Город', 'Цена'])
        for item in prep:
            writer.writerow([date, '', item['title'], name, item['link'], item['name'], item['price']])

# как надо по поиску, но допилить по новому списку
