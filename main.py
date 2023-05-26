import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

URL = 'https://reestr.rgr.ru/rejting-agentstv-v-reestre/'

page = requests.get(URL)

# with open('saveagent.html', 'w') as file:
#     file.write(page.text)
#
new_url = urlparse(URL)

with open('saveagent.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

table_ = soup.table


def show_child(tbl):
    for child in tbl.children:
        yield child.find('a').get('href')


go_ahead = new_url._replace(path=next(show_child(table_))).geturl()
new_page = requests.get(go_ahead)

with open('savecart.html') as file:
    new_soup = BeautifulSoup(file, 'html.parser')


def get_cart():
    cart = {}

    cart['address'] = new_soup.find('div', class_='offices').find('address').string
