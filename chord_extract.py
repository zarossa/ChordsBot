import requests
import lxml.html


def parse(url_address):
    api = requests.get(url_address)
    tree = lxml.html.fromstring(api.text)
    text = tree.xpath('/html/body/div[2]/article/div//div/pre')
    return text[0].text_content().replace('\t', '            ')


url = 'https://amdm.ru/akkordi/5nizza/11554/pyatnica/'


def main():
    return parse(url)


if __name__ == '__main__':
    main()
