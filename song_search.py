import requests
import lxml.html


def parse(url_address):
    # Подготовка списка песен
    api = requests.get(url_address).text
    tree = lxml.html.fromstring(api)
    return tree.xpath('//tr/td[@class="artist_name"]')


def url_maker():
    # Создание поисковой ссылки
    text = input().split()
    return 'https://amdm.ru/search/?q=' + '+'.join(text)


def listpart_print(songlist, k):
    # Вывод 5 строк из списка песен
    for i in range(len(songlist)):
        print((i + 1) + (k * 5), songlist[i].text_content(), songlist[i][1].attrib['href'])
    print('here')

def list_print(songlist):
    # Вывод списка песен
    if len(songlist) == 0:
        return 'Ничего не найдено'
    for k in range(len(songlist) // 5):
        listpart_print(songlist[k * 5:(k + 1) * 5], k)
        if k != (len(songlist) // 5 - 1):
            if input('Загрузить еще?\n') == 'n':
                break
    if len(songlist) % 5:
        listpart_print(songlist[len(songlist) // 5 * 5: len(songlist)], len(songlist) // 5)


songlist = parse(url_maker())
print(list_print(songlist))
