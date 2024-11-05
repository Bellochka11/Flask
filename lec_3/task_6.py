import asyncio # МОДУЛЬ ДЛЯ АСИНХРОННОГО ИНПУТ АУТПУТ ВВОД ВЫВОД ДАННЫХ

#3 АСИНХРОННЫХ ФУНКЦИЙ КАРУТИН

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(1) # await - я могу сейчас подождать. другие карутины могут импользовать ресурсы процесса и потока для выполнения своих действий


async def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        print(letter)
        await asyncio.sleep(0.5) #за 0.5 секунд карутина может отдать свои ресурсы другим карутинам для выполнения задач

async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())
    await task1 #запускаем 1 карутину если она готова подождать запускаем вторую
    await task2

asyncio.run(main()) #создаем цикл событий