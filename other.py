from bs4 import BeautifulSoup
import pandas as pd

# with open('loto.txt', 'r', encoding='utf-8') as my_file:

with open('loto_arhiv.html', 'r', encoding='utf-8') as my_file:
    rus_txt = my_file.read()
result = BeautifulSoup(rus_txt, "lxml")
tads_arhiv = result.find('div', class_='data drawings_data')
rezultat = tads_arhiv.find_all('div', class_='month')
tabl_result = []
for month in rezultat:
    year = month.find('div', class_='date').text.split(',')[1]
    for tiraz in month.find_all('div', class_='main'):
        draw_data = tiraz.find('div', class_='draw_date').text + year
        draw = tiraz.find('div', class_='draw').text.replace('\n', '')
        try:
            numbers = list(map(int, tiraz.find('span', class_='zone').text.split()))
        except Exception:
            numbers = tiraz.find('span', class_='zone').text
            if "Все билеты выиграли" == numbers:
                numbers = [0]
        super_prize = int(''.join(tiraz.find('div', class_='jackpot_wrapper').text.split()))
        for cifra in numbers:
            tabl_result.append([draw_data, draw, cifra, super_prize])

df = pd.DataFrame(tabl_result, columns=['Дата', 'Тираж', 'Невыпавшие числа', 'Призовой фонд'])
counts_cifra = df['Невыпавшие числа'].value_counts()
dict_count_cifra = counts_cifra.to_dict()
counts_cifra.to_excel('sort.xlsx')
sorted_dict_count_cifra = sorted(dict_count_cifra.items())
print(sorted_dict_count_cifra)
# for nomer, count in counts_cifra:
#     print(f'nomer={nomer}, count={count}')
# print(counts_cifra)
# print(sorted(counts_cifra))

#Через словарь: my_df = pd.DataFrame({'id': [1, 2, 3], 'name': ['Bob', 'Alice', 'Scott'], 'age': [21, 15, 30]})
# Через вложенные списки: df = pd.DataFrame([[1,'Bob', 21], [2,'Alice', 15], [3,'Scott', 30]], columns = ['id','name', 'age'])