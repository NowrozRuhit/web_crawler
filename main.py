import requests
from bs4 import BeautifulSoup


def book_spider(max_page):
    page = 1
    while page <= max_page:
        # url = 'https://www.olx.in/all-results/?page=' + str(page)
        url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
        website_source_code = requests.get(url)
        plain_text = website_source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.find_all('div', {'class': 'image_container'}):
            href = 'http://books.toscrape.com/catalogue/' + link.a.get('href')
            # print(link.a.img.get('alt'))
            print(href)
            page += 1
            get_single_data(href)


def get_single_data(item_url):
    website_source_code = requests.get(item_url)
    plain_text = website_source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll('div', {'class': 'col-sm-6 product_main'}):
        print(item_name.h1.string)

    for link in soup.findAll('a'):
        href = link.get('href')
        # print(href)


book_spider(1)
print("done")
