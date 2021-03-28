'''
В нашей школе мы не можем разглашать персональные данные пользователей, но
чтобы преподаватель и ученик смогли объяснить нашей поддержке, кого они имеют
в виду (у преподавателей, например, часто учится несколько Саш), мы генерируем
пользователям уникальные и легко произносимые имена. Имя у нас состоит из
прилагательного, имени животного и двузначной цифры. В итоге получается,
например, "Перламутровый лосось 77". Для генерации таких имен мы и решали
следующую задачу:
Получить с русской википедии список всех животных (Категория:Животные по
алфавиту) и вывести количество животных на каждую букву алфавита. Результат
должен получиться в следующем виде:
А: 642
Б: 412
В:....

'''

from requests import get
from pyquery import PyQuery
from urllib.parse import urljoin

alphabet = "АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ"

def walk_pages():
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    names = set()
    u = url
    not_in_alpha_count = 0
    while u:
        r = get(u)
        assert r.ok
        d = PyQuery(r.text)
        for a in d('#mw-pages a'):
            href = PyQuery(a).attr('href')
            if 'pagefrom' in href:
                u = urljoin(u, href)
                break
        else:
            raise Exception("next page not found")
        for a in d("#mw-pages li a"):
            name = PyQuery(a).text()
            assert name
            letter = name[0].upper()
            if letter not in alphabet:
                not_in_alpha_count += 1
                if not_in_alpha_count > 10:
                    u = None
                    break
                else:
                    continue
            else:
                not_in_alpha_count = 0    
            names.add(name)
    return names

def histogram(list, sorted_keys=None):
    histogram = {}
    for o in list:
        letter = o[0].upper()
        histogram[letter] = histogram.get(letter, 0) + 1
    for letter in sorted_keys or sorted(histogram.keys()):
        value = histogram.get(letter, 0)
        print(f'{letter}: {value}')

histogram(walk_pages(), sorted_keys=alphabet)
