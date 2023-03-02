import reader_url_saved_text as RU
import read_text_in_soup as RT


def number_of_details_page():
    soup = RT.read_text()
    how_many_pages_with_a_detail = soup.find_all('div', class_='catalog_item_title')
    #how_many_pages_with_a_detail = soup.find_all('div', class_ = 'catalog_item_title_wrap')
    len_how_many_pages_with_a_detail = len(how_many_pages_with_a_detail)
    if len_how_many_pages_with_a_detail == 0:
        one_pages_details = soup.find_all('div', class_='catalog_group_title')
        if one_pages_details != '':
            print(f"Одна деталь на странице = {one_pages_details}")
            return
        else:
            print(f"Страница пуста = {one_pages_details}")
    elif len_how_many_pages_with_a_detail > 1:
        print(len_how_many_pages_with_a_detail)
        return #подумать
    # print(len(how_many_pages_with_a_detail))
    # print([texts.find('h2').text for texts in how_many_pages_with_a_detail])

def main(nomer):
    #RU.reader_url_saved_text_nomer(nomer)
    number_of_details_page()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nomer = 'DRS5930'
    # 'div', class = 'catalog_item_title_wrap'
    main(nomer)
