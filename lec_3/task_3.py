import multiprocessing #модуль для большого колва процессов
import time


def worker(num):
    print(f"Запущен процесс {num}")
    time.sleep(3)
    print(f"Завершён процесс {num}")


if __name__ == '__main__': # 5 процессов
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join() # ждем пока очередной процесс завершится

    # for p in processes:
    #     p.start()
    #     p.join() # ждем пока очередной процесс завершится

    print("Все процессы завершили работу")