from bs4 import BeautifulSoup

def read_text():
    """
    Чтение из файла index.html и преобразовываем с soup
    :return: Возвращает "BeautifulSoup"
    """
    try:
        with open("result.html", "r", encoding="utf-8") as w_file:
            src = w_file.read()
        return BeautifulSoup(src, "lxml")
    except Exception as err:
        print(f"Ошибка чтения из файла. Ошибка {err}")