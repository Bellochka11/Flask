import asyncio
from pathlib import Path


async def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        # do some processing with the file contents
        print(f'{f.name} содержит {contents[:7]}...')


async def main():
    # dir_path = Path('/path/to/directory')
    dir_path = Path('.') #путь к текущ каталогу
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()] #итерируемся по файлам в директории если это файл помещаем его в список
    tasks = [asyncio.create_task(process_file(file_path)) for file_path in file_paths] #итерируемся по file_paths и создаем корутину и передаем туда file_path
    await asyncio.gather(*tasks) #запуск корутин одновременно


if __name__ == '__main__':
    asyncio.run(main())