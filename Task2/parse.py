import requests
from bs4 import BeautifulSoup
import fake_useragent
import csv

user = fake_useragent.UserAgent().random
headers = {
    'user-agent': user
}

def get_html(url):
    r = requests.get(url, headers=headers)
    return r

def get_content(html):
    catalog = []
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-card')
    for i in items:
        price = i.find('span', class_='product-price__value').get_text()
        price = price.replace('₽', '').replace(' ', '')
        name = i.find('div', class_='product-card__title').get_text().strip()
        author = i.find('div', class_='product-card__author').get_text().strip()
        author = author[:-3]
        status = i.find('span', class_='js__card_button_text').get_text()
        catalog.append({
            'name': name,
            'author': author,
            'price': price,
            'status': status
        })
    return catalog

def save_file(items, path):
    with open(path, 'w', encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Название книги', 'Автор', 'Цена', 'Способ заказа'])
        for item in items:
            writer.writerow([item['name'], item['author'], item['price'], item['status']])



def parse():
    for URL in ['https://www.chitai-gorod.ru/catalog/books/psikhologiya-9530/']:
        html = get_html(URL)
        if html.status_code == 200:
            html = get_content(html.text)
        else:
            print('Error')
        filename = 'parser.csv'
        save_file(html, filename)


if __name__ == '__main__':
    parse()
