import threading #модуль отвечающий за работу с потоками
import time


def worker(num):
    print(f"Начало работы потока {num}")
    time.sleep(3)
    print(f"Конец работы потока {num}")

threads = []
for i in range(5): #5 потоков
    t = threading.Thread(target=worker, args=(i, )) # worker будет рабротать внутри потока args=(i, ) функция получает в кач ве аргумента i
    threads.append(t)
    t.start()

# for t in threads:
#     t.join()

for t in threads:
    # t.start()
    t.join()

print("Все потоки завершили работу")