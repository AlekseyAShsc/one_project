import reader_url_saved_text as RU
import read_text_in_soup as RT
import cross as CR
import save_primenimosti_xlsx as SPX

def number_of_details_page():
    soup = RT.read_text()
    how_many_pages_with_a_detail = soup.find_all('div', class_='catalog_item_title')
    #how_many_pages_with_a_detail = soup.find_all('div', class_ = 'catalog_item_title_wrap')
    len_how_many_pages_with_a_detail = len(how_many_pages_with_a_detail)
    if len_how_many_pages_with_a_detail == 0:
        one_pages_details = soup.find_all('div', class_='catalog_group_title')
        print(type(soup))
        print(type(one_pages_details))
        if one_pages_details != '':
            nomer_na_stranice = one_pages_details[0].text.strip()
            print(f"Одна деталь на странице = |{nomer_na_stranice}|")
            # ----- Сохраняем кроссы из сохраненной станицы
            SPX.save_dannix_detali(nomer_na_stranice, CR.filter_kross(soup))
            # ----- Вывоодим в окно информацию о сохранении страницы
            return
        else:
            print(f"Страница пуста = {one_pages_details}")
            # ----- Вводим в окне что нет такой детали
    elif len_how_many_pages_with_a_detail > 1:
        # перебираем все детали на листе
        for href in how_many_pages_with_a_detail:
            url = (f"https://voltag.ru{href.find('a').get('href')}") # Формируем адрес старницы детали
            nomer_na_stranice = href.find('h2').text # Дерем номер детали на странице
            RU.reader_url_saved_text_url(url) # Сохраняем страницу в текстовый файл
            soup_w = RT.read_text() # Читаем из текстового фйла и делаем суп
            SPX.save_dannix_detali(nomer_na_stranice, CR.filter_kross(soup_w)) # Сохраняем данные в exel файл
        # ----- Вывоодим в окно информацию о сохраненых страницах
        return #подумать

def main(nomer):
    #RU.reader_url_saved_text_nomer(nomer)
    number_of_details_page()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nomer = 'DRS5930'
    # 'div', class = 'catalog_item_title_wrap'
    main(nomer)
