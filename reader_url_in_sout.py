import requests
from bs4 import BeautifulSoup


def reader_nomer_in_BS(nomer_detali):
    """
    Чтение страница на вольтаже по номеру и сохранение страницы в файл
    nomer_detali - номер по которому ищим на сайте вольтаж данные
    """
    try:
        cookies = {
            '_ym_uid': '15790767129862584',
            'PHPSESSID': 'x50GLYxpTJJeFzrHf7RxbKs8mrEsSVwm',
            'BITRIX_SM_USER_TRACK_ID': '4402201',
            'BX_USER_ID': 'd3103bd08dbb6eb33f91fe2b32d8698e',
            '__utmc': '197302824',
            '_ym_d': '1665215935',
            'BITRIX_SM_SALE_UID': '123596535',
            '__utmz': '197302824.1674453292.13.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
            'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1677185940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
            '_ym_isad': '2',
            '__utma': '197302824.157177916.1658565164.1677129465.1677148027.30',
            '_ym_visorc': 'w',
            '__utmt': '1',
            '__utmb': '197302824.4.10.1677148027',
        }

        headers = {
            'authority': 'voltag.ru',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'cookie': '_ym_uid=15790767129862584; PHPSESSID=x50GLYxpTJJeFzrHf7RxbKs8mrEsSVwm; BITRIX_SM_USER_TRACK_ID=4402201; BX_USER_ID=d3103bd08dbb6eb33f91fe2b32d8698e; __utmc=197302824; _ym_d=1665215935; BITRIX_SM_SALE_UID=123596535; __utmz=197302824.1674453292.13.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1677185940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_isad=2; __utma=197302824.157177916.1658565164.1677129465.1677148027.30; _ym_visorc=w; __utmt=1; __utmb=197302824.4.10.1677148027',
            'referer': 'https://voltag.ru/',
            'sec-ch-ua': '"Opera";v="95", "Chromium";v="109", "Not;A=Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0 (Edition Yx)',
        }

        params = {
            'q': nomer_detali,
        }

        text_html = requests.get('https://voltag.ru/catalog/list/', params=params, cookies=cookies, headers=headers)
    except Exception:
        print(f"Ошибка при чтении страницы на сайте по номеру - {nomer_detali}")
    try:
        result = BeautifulSoup(text_html.text, "lxml")
    except Exception:
        print(f"Ошибка при формировании BS")
    return result


def reader_url_in_BS(url):
    """
    :param url: адрес страницы с которой парсятся данные
    :return: не возвращает ничего, данные сохранятся в файл "index.html"
    функция скачивания и записи данных с сайта в файл
    """
    try:
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
        }
        reg = requests.get(url, headers=headers)
        text_html = reg.text
    except Exception:
        print(f"Ошибка при чтении страницы {url}")
    try:
        result = BeautifulSoup(text_html, "lxml")
    except Exception:
        print(f"Ошибка при формировании BS")
    return result


if __name__ == '__main__':
    pass
