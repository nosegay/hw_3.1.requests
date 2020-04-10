import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


usage = '''
Скрипт для перевода текстов на русский язык.
Используются только позиционные аргументы, передаваемые в следующем порядке:
- Путь к файлу с текстом;
- Путь к файлу с результатом;
- Язык с которого перевести;
- Язык на который перевести (по-умолчанию русский).
'''


def translate_it(text, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param from_lang, to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'{from_lang}-{to_lang}',
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически о
# пределенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))


def translate_txt(input_file, output_file, from_lang, to_lang='ru'):
    print(f'Перевод файла {input_file}...')

    with open(input_file, 'r', encoding='utf-8') as fp:
        data = fp.read()

    with open(output_file, 'w', encoding='utf-8') as fp:
        fp.write(translate_it(data, from_lang, to_lang))

    print(f'Файл {input_file} переведен. Результат в файле {output_file}')


if __name__ == '__main__':
    translate_txt('DE.txt', 'de-ru.txt', 'de')
    translate_txt('ES.txt', 'es-ru.txt', 'es')
    translate_txt('FR.txt', 'fr-ru.txt', 'fr')

    # translate_txt('DE.txt', 'de-en.txt', 'de', 'en')
