import re
import read_text_in_soup as RS
from bs4 import BeautifulSoup

# фильтрация названия модели
def filter_nomer_grout(soup):
    nomer_grout = ''.join(soup.find('div', class_='catalog_group_title').text.split())
    # можно сделать разбор номера
    # St - стартер, Al - генератор.
    # 3-я буква конструктив B - Bosch, V-Valeo, N-Denso, Q-China, W-Saafuji, R-Russia ....
    return nomer_grout

# Пытаемся найти каталог по номеру
def find_katalog_is_nomer(soup, nomer_grout):
    quotes_kross = soup.find('div', class_='catalog_group_crosslist_info')
    print(f'ищим каталог группы - {nomer_grout}')
    vxosdenie_nomera = quotes_kross.find_all(string = (re.compile(nomer_grout)))
    print("vxosdenie_nomera", vxosdenie_nomera)
    if vxosdenie_nomera == []:
        katalog = "неопредело"
    else:
        for n in vxosdenie_nomera:
            katalog = n.find_previous("tr").find("td").text
            print(f'поиск предыдущего тега - {n} = {katalog}')
        #td
        print(katalog)
    return katalog

# Формирование параметров детали
def filter_param(soup):
    quotes_param = soup.find('div', class_='catalog_group_params').find('tbody')
    table_param = []
    # Create a for loop to fill mydata
    for table_row_param in quotes_param.find_all('tr'):
        table_row_separated_param = table_row_param.find_all('td')
        table_row_separated_param_sets = [cell_param.text.replace(u'\xa0', u' ') for cell_param in table_row_separated_param]
        table_param.append(table_row_separated_param_sets)

    return table_param

# фильтрация данных кроссов
def filter_kross(soup):
    quotes_kross = soup.find('div', class_='catalog_group_crosslist_info')

    # форматирование данных кроссов cross
    cross = {}
    katal = 'Zero'
    for td in quotes_kross.find_all('td'):
        znac = td.text.strip()
        if str(td).find('mnfr') == -1:
            if len(znac.split(', ')) == 1:
                cross[katal] = znac
            else:
                for td1 in (znac.split(', ')):
                    cross.setdefault(katal, []).append(td1)
        else:
            if znac == '':
                katal = 'Zero'
            else:
                katal = znac
    return cross

if __name__ == '__main__':
    soup = RS.read_text()
    nomer_grout = 'HAZ0020'
    print(*filter_param(soup))
    # print(find_katalog_is_nomer(soup, nomer_grout))
