import requests
import lxml.html


def url_maker(text):
    # Создание поисковой ссылки
    text = text.split()
    return 'https://amdm.ru/search/?q=' + '+'.join(text)


def listmake(text):
    # Подготовка списка песен
    url_address = url_maker(text)
    api = requests.get(url_address).text
    tree = lxml.html.fromstring(api)
    return tree.xpath('//tr/td[@class="artist_name"]')


def listpart_print(songlist, k):
    # Вывод 5 строк из списка песен
    partlist = ['{}. {}'.format((i + 1) + (k * 5), songlist[i].text_content()) for i in range(len(songlist))]
    return partlist # , songlist[i][1].attrib['href'])


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


def main(text_message):
    songlist = listmake(text_message)
    return list_print(songlist)


if __name__ == '__main__':
    main()
