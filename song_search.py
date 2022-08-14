import requests
import lxml.html
from lxml import etree


def parse(url_address):
    api = requests.get(url_address).text
    tree = lxml.html.fromstring(api)
    return tree.xpath('//tr/td[@class="artist_name"]')



def url_maker():
    text = input().split()
    return 'https://amdm.ru/search/?q=' + '+'.join(text)


def main():
    return parse(url_maker())

songlist = main()
k = 0
while True:
    for i in range(k * 5, (k + 1) * 5):
        print(i + 1, songlist[i].text_content(), songlist[i][1].attrib['href'])
    if k != 3:
        if input('Next?(y/n)\n') == 'y':
            k += 1
        else:
            break
    else:
        break
# k = 0
# while True:
#     if __name__ == '__main__':
#         main()
#     if input('More?\n') == 'y':
#         k += 1
#     else:
#         break
