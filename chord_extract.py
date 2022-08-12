import requests
import lxml.html


def parse(url_address):
    api = requests.get(url_address)
    tree = lxml.html.document_fromstring(api.text)
    text = tree.xpath('/html/body/div[2]/article/div//div/pre')
    print(text[0].text_content())


url = 'https://amdm.ru/akkordi/la_rue_morgue/150160/sigues_dando_vueltas/'


def main():
    parse(url)


if __name__ == '__main__':
    main()
