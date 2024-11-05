import asyncio
import aiohttp
import time

#АСИНХРОННОЕ
urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]

async def download(url):
    async with aiohttp.ClientSession() as session: #сессия с клиентом
        async with session.get(url) as response: #получаем информацию по адресу
            text = await response.text()
            filename = 'asyncio_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url)) # подготовка карутин
        tasks.append(task)
    await asyncio.gather(*tasks) #выполняем вместе 5 задач карутин асинхронно
    
start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop() #цикл событий
    loop.run_until_complete(main()) #запусаем карутину мэйн пока она не будет завершена