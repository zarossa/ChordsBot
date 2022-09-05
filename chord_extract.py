import requests
import lxml.html


def parse(url):
    api = requests.get(url)
    tree = lxml.html.fromstring(api.text)
    text = tree.xpath('/html/body/div[2]/article/div//div/pre')
    return text[0].text_content().replace('\t', '            ')


def main(url):
    return parse(url)


if __name__ == '__main__':
    main()
