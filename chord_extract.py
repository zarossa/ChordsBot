import requests
import lxml.html
import re


def parse(url):
    api = requests.get(url)
    tree = lxml.html.fromstring(api.text)
    text = tree.xpath('/html/body/div[2]/article/div//div/pre')
    return text[0].text_content().replace('\t', '            ')


def splitter(text):
    new_text = []
    for i in range(len(text) // 4096):
        splitter = text.rfind('\n', 0, 4096)
        new_text.append(text[:splitter])
        text = text[splitter + 1:]
    new_text.append(text)
    return new_text


def main(url):
    return parse(url)


if __name__ == '__main__':
    main()
