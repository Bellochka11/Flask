import requests #модуль
import time
#СИНХРОННОЕ

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]

start_time = time.time()

for url in urls:
    response = requests.get(url) #скачиваем инфу по адресу url
    filename = 'sync_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html' # html файл с префиксом sync_ для синхронной загрузки
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text) #записываем инфу в файл
    print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")