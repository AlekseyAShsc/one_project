import sys
import reader_url_saved_text as RU
import read_text_in_soup as RT
import cross as CR
import save_primenimosti_xlsx as SPX
from main_window_voltage import *

def number_of_details_page():
    soup = RT.read_text()
    how_many_pages_with_a_detail = soup.find_all('div', class_='catalog_item_title')
    #how_many_pages_with_a_detail = soup.find_all('div', class_ = 'catalog_item_title_wrap')
    len_how_many_pages_with_a_detail = len(how_many_pages_with_a_detail)
    if len_how_many_pages_with_a_detail == 0:
        one_pages_details = soup.find_all('div', class_='catalog_group_title')
        print(type(soup))
        print(type(one_pages_details))
        if len(one_pages_details) != 0:
            nomer_na_stranice = one_pages_details[0].text.strip()
            print(f"Одна деталь на странице = |{nomer_na_stranice}|")
            # ----- Сохраняем кроссы из сохраненной станицы
            ui.label.setText(SPX.save_dannix_detali(nomer_na_stranice, CR.filter_kross(soup)))
            ui.label_2.setText(f"Одна деталь на странице = |{nomer_na_stranice}|")
            # ----- Выводим в окно информацию о сохранении страницы
            return
        else:
            print(f"Страница пуста = {one_pages_details}")
            # ----- Вводим в окне что нет такой детали
            ui.label.setText(f"Страницы с таким номером нет!")
    elif len_how_many_pages_with_a_detail > 1:
        # список номеров деталей
        list_number_details = []
        text_soobshchenie = []
        # перебираем все детали на листе
        for href in how_many_pages_with_a_detail:
            url = (f"https://voltag.ru{href.find('a').get('href')}") # Формируем адрес старницы детали
            nomer_na_stranice = href.find('h2').text # Берем номер детали на странице
            RU.reader_url_saved_text_url(url) # Сохраняем страницу в текстовый файл
            soup_w = RT.read_text() # Читаем из текстового фйла и делаем суп
            text_soobshchenie.append(SPX.save_dannix_detali(nomer_na_stranice, CR.filter_kross(soup_w))) # Сохраняем данные в exel файл
            list_number_details.append(nomer_na_stranice)

        # ----- Вывоодим в окно информацию о сохраненых страницах
        ui.label_2.setText(f"Страницы с такими номероми - |{list(list_number_details)}| сохранены")
        text = '\n'.join(f'{chn}' for chn in text_soobshchenie)
        ui.label.setText(f"{text}")
        return #подумать

def main(nomer):
    nomer=ui.LE_input_nomer.text()
    print(nomer)
    RU.reader_url_saved_text_nomer(nomer)
    number_of_details_page()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # nomer = 'DRS5930'
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.B_Search.clicked.connect(main)
    ui.B_exit.clicked.connect(sys.exit)
    # MainWindow.keyPressEvent(ui.QKeyEvent.key_event_text)
    sys.exit(app.exec_())
