import time

import requests
from bs4 import BeautifulSoup
import lxml
import asyncio
import aiohttp

def parsing_odd_12():
    back_post_id = None
    while True:
        URL = "https://www.tpk-tver.ru/studentam-i-obuchyushchimsya/raspisanie-zanyatij.html"
        page_even_1 = requests.get(URL)
        soup_even_1 = BeautifulSoup(page_even_1.text, "lxml")
        post_even_1 = soup_even_1.find("div", id=True, class_="attachmentsList")

        post_id_odd_1 = post_even_1['id']
        if post_id_odd_1 != back_post_id:

            even_class_url_1 = post_even_1.find_all(class_='odd')
            for even_1_1 in even_class_url_1[3:4]:
                even_2_2 = even_1_1.find('td', class_='at_filename')
                even_at_url_1 = even_2_2.find('a', class_='at_url', href=True)['href'].strip()
                ssylka_na_sayt_1 = 'https://www.tpk-tver.ru'
                sylka_plyus_url_odd = ssylka_na_sayt_1 + even_at_url_1
            try:
                return  sylka_plyus_url_odd,even_at_url_1
            except:
                return 'нет', 'Нет'







def parsing_even_1():
    back_post_id = None
    while True:
        URL = "https://www.tpk-tver.ru/studentam-i-obuchyushchimsya/raspisanie-zanyatij.html"
        page_even_1 = requests.get(URL)
        soup_even_1 = BeautifulSoup(page_even_1.text, "lxml")
        post_even_1 = soup_even_1.find("div", id=True, class_="attachmentsList")

        post_id_even_1 = post_even_1['id']
        if post_id_even_1 != back_post_id:

            even_class_url_1 = post_even_1.find_all(class_='even')
            for even_1_1 in even_class_url_1[3:4]:
                even_2_2 = even_1_1.find('td', class_='at_filename')
                even_at_url_1 = even_2_2.find('a', class_='at_url', href=True)['href'].strip()
                ssylka_na_sayt_1 = 'https://www.tpk-tver.ru'
                sylka_plyus_url = ssylka_na_sayt_1 + even_at_url_1
        try:
            return sylka_plyus_url,even_at_url_1
        except:
            return 'нет', 'Нет'

qwerasfzv = 'Шевченко Ефим Андреевич'
def parsing_even_2():
    back_post_id = None
    while True:
        URL = "https://www.tpk-tver.ru/studentam-i-obuchyushchimsya/raspisanie-zanyatij.html"
        page_even_2 = requests.get(URL)
        soup_even_2 = BeautifulSoup(page_even_2.text, "lxml")
        post_even_2 = soup_even_2.find("div", id=True, class_="attachmentsList")

        post_id_even_2 = post_even_2['id']
        if post_id_even_2 != back_post_id:

            even_class_url_2 = post_even_2.find_all(class_='even')
            for even_1_2 in even_class_url_2[4:5]:
                even_2_2 = even_1_2.find('td', class_='at_filename')
                even_at_url_1 = even_2_2.find('a', class_='at_url', href=True)['href'].strip()

                ssylka_na_sayt_2 = 'https://www.tpk-tver.ru'
                sylka_plyus_url_2 = ssylka_na_sayt_2 + even_at_url_1
            try:
                return sylka_plyus_url_2,even_at_url_1
            except:
                return 'нет', 'Нет'


def parsing_odd_1():
    back_post_id = None
    while True:
        URL = "https://www.tpk-tver.ru/studentam-i-obuchyushchimsya/raspisanie-zanyatij.html"
        page_even_1 = requests.get(URL)
        soup_even_1 = BeautifulSoup(page_even_1.text, "lxml")
        post_even_1 = soup_even_1.find("div", id=True, class_="attachmentsList")

        post_id_odd_1 = post_even_1['id']
        if post_id_odd_1 != back_post_id:

            even_class_url_1 = post_even_1.find_all(class_='odd')
            for even_1_1 in even_class_url_1[4:5]:
                even_2_2 = even_1_1.find('td', class_='at_filename')
                even_at_url_1 = even_2_2.find('a', class_='at_url', href=True)['href'].strip()
                ssylka_na_sayt_1 = 'https://www.tpk-tver.ru'
                sylka_plyus_url_odd = ssylka_na_sayt_1 + even_at_url_1
            try:
                return  sylka_plyus_url_odd,even_at_url_1
            except:
                return 'нет', 'Нет'


def parsing_odd_2():
    back_post_id = None
    while True:
        URL = "https://www.tpk-tver.ru/studentam-i-obuchyushchimsya/raspisanie-zanyatij.html"
        page_even_1 = requests.get(URL)
        soup_even_1 = BeautifulSoup(page_even_1.text, "lxml")
        post_even_1 = soup_even_1.find("div", id=True, class_="attachmentsList")

        post_id_odd_2 = post_even_1['id']
        if post_id_odd_2 != back_post_id:

            even_class_url_1 = post_even_1.find_all(class_='odd')
            for even_1_1 in even_class_url_1[5:6]:
                even_2_2 = even_1_1.find('td', class_='at_filename')
                even_at_url_1 = even_2_2.find('a', class_='at_url', href=True)['href'].strip()
                ssylka_na_sayt_1 = 'https://www.tpk-tver.ru'
                sylka_plyus_url_odd_2 = ssylka_na_sayt_1 + even_at_url_1
            try:
                return sylka_plyus_url_odd_2,even_at_url_1
            except:
                return 'нет', 'Нет'


def parsing_odd_3():
    back_post_id = None
    while True:
        URL = "https://www.tpk-tver.ru/studentam-i-obuchyushchimsya/raspisanie-zanyatij.html"
        page_even_1 = requests.get(URL)
        soup_even_1 = BeautifulSoup(page_even_1.text, "lxml")
        post_even_1 = soup_even_1.find("div", id=True, class_="attachmentsList")

        post_id_odd_2 = post_even_1['id']
        if post_id_odd_2 != back_post_id:

            even_class_url_1 = post_even_1.find_all(class_='odd')
            for even_1_1 in even_class_url_1[6:7]:
                even_2_2 = even_1_1.find('td', class_='at_filename')
                even_at_url_1 = even_2_2.find('a', class_='at_url', href=True)['href'].strip()
                ssylka_na_sayt_1 = 'https://www.tpk-tver.ru'
                sylka_plyus_url_odd_2 = ssylka_na_sayt_1 + even_at_url_1
            try:
                return sylka_plyus_url_odd_2,even_at_url_1
            except:
                return 'нет', 'Нет'




def parsing_even_3():
    back_post_id = None
    while True:
        URL = "https://www.tpk-tver.ru/studentam-i-obuchyushchimsya/raspisanie-zanyatij.html"
        page_even_2 = requests.get(URL)
        soup_even_2 = BeautifulSoup(page_even_2.text, "lxml")
        post_even_2 = soup_even_2.find("div", id=True, class_="attachmentsList")

        post_id_even_2 = post_even_2['id']
        if post_id_even_2 != back_post_id:

            even_class_url_2 = post_even_2.find_all(class_='even')
            for even_1_2 in even_class_url_2[5:6]:
                even_2_2 = even_1_2.find('td', class_='at_filename')
                even_at_url_1 = even_2_2.find('a', class_='at_url', href=True)['href'].strip()

                ssylka_na_sayt_2 = 'https://www.tpk-tver.ru'
                sylka_plyus_url_2 = ssylka_na_sayt_2 + even_at_url_1
            try:
                return sylka_plyus_url_2,even_at_url_1
            except:
                return 'нет', 'Нет'


def parsing():
        start = time.time()
        back_post_id = None

        URL = "https://www.rbc.ru/short_news"

        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")
        post = soup.find("div", class_="l-row js-news-feed-list")
        post1 = post.find('div', class_='js-news-feed-item js-yandex-counter', id= True)
        post_id = post1['id']
        if post_id != back_post_id:
            c = post1.find("div", class_="item__wrap l-col-center")
            url = c.find('a', class_='item__link', href=True)["href"].strip()
            tex = c.find('span', class_ ='item__title rm-cm-item-text').text.strip()
            end = time.time()
            qwe = round(end - start, 2)
            return tex, url, qwe
        else:
            return None, post_id

def parsing_odd_1221():
    back_post_id = None
    while True:
        URL = "https://www.tpk-tver.ru/sotrudnikam/meropriyatiya.html"
        page_even_2 = requests.get(URL)
        soup_even_2 = BeautifulSoup(page_even_2.text, "lxml")
        post_even_2 = soup_even_2.find("div", id=True, class_="attachmentsList")

        post_id_even_2 = post_even_2['id']
        if post_id_even_2 != back_post_id:

            even_class_url_2 = post_even_2.find_all(class_='even')
            for even_1_2 in even_class_url_2:
                even_2_2 = even_1_2.find('td', class_='at_filename')
                even_at_url_1 = even_2_2.find('a', class_='at_url', href=True)['href'].strip()

                ssylka_na_sayt_2 = 'https://www.tpk-tver.ru'
                sylka_plyus_url_2 = ssylka_na_sayt_2 + even_at_url_1
            try:
                return sylka_plyus_url_2
            except:
                return 'нет', 'Нет'





































































































































































































































































a = 'Шевченко Ефим Андреевич'

