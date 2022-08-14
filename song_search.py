import requests
import lxml.html
from lxml import etree


def parse(url_address):
    api = requests.get(url_address).text
    tree = lxml.html.fromstring(api)
    songlist = tree.xpath('//tr/td[@class="artist_name"]')
    for i in range(5):
        print(songlist[i].text_content(), songlist[i])






url = 'https://amdm.ru/search/?q=пачка+сигарет'


def main():
    return parse(url)


if __name__ == '__main__':
    main()
